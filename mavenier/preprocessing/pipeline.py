"""Coordinate Markdown loading, Docling chunking, extraction, and JSONL output."""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any

from mavenier.preprocessing.content_classifier import classify_chunk_content
from mavenier.preprocessing.loader import (
    discover_markdown_documents,
    find_section_for_chunk,
    load_markdown,
    parse_document_header,
    parse_document_path,
)
from mavenier.preprocessing.metadata_extractor import extract_all_metadata

LOGGER = logging.getLogger(__name__)
INCLUDE_RAW_DOCLING_METADATA = True
DEFAULT_MODEL = "BAAI/bge-small-en-v1.5"
DEFAULT_MAX_TOKENS = 400


def _jsonable(value: Any) -> Any:
    """Convert Pydantic and Docling values into plain JSON values."""
    if hasattr(value, "model_dump"):
        return _jsonable(value.model_dump(mode="json"))
    if isinstance(value, dict):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_jsonable(item) for item in value]
    if hasattr(value, "value"):
        return _jsonable(value.value)
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def chunk_metadata(chunk: Any, include_raw: bool = INCLUDE_RAW_DOCLING_METADATA) -> dict[str, Any]:
    """Keep headings, captions, item types, and Docling's original metadata."""
    meta = getattr(chunk, "meta", None)
    item_types = []
    for item in getattr(meta, "doc_items", None) or []:
        label = getattr(item, "label", None)
        item_types.append(str(getattr(label, "value", label)))
    headings = [value for value in (getattr(meta, "headings", None) or []) if value.strip()]
    result = {
        "headings": headings,
        "captions": list(getattr(meta, "captions", None) or []),
        # Markdown has no reliable physical page numbers.
        "page_numbers": [],
        "document_item_types": list(dict.fromkeys(item_types)),
    }
    if include_raw:
        result["raw"] = _jsonable(meta) if meta is not None else {}
    return result


def build_contextualized_text(
    filename: str,
    section: str | None,
    section_path: list[str],
    original_text: str,
    release: str | None = None,
    series: str | None = None,
) -> str:
    """Build clean embedding text without changing the original chunk.

    Release and series are included when known so the embedding carries the
    spec's identity, which helps separate near-identical passages that recur
    across releases.
    """
    context_lines = [f"Document: {filename}"]
    if release:
        context_lines.append(f"Release: {release}")
    if series:
        context_lines.append(f"Series: {series}")
    if section:
        context_lines.append(f"Section: {section}")
    if section_path:
        context_lines.append(f"Section path: {' > '.join(section_path)}")
    return "\n".join(context_lines) + "\n\n" + original_text


def validate_chunk(record: dict[str, Any]) -> None:
    """Reject malformed records before they reach the JSONL file."""
    if not record.get("chunk_id"):
        raise ValueError("Chunk has no chunk_id")
    if not record.get("original_text", "").strip():
        raise ValueError(f"{record['chunk_id']} has empty original_text")
    if not record.get("contextualized_text", "").strip():
        raise ValueError(f"{record['chunk_id']} has empty contextualized_text")
    if record["chunk_id"] in record["original_text"]:
        raise ValueError(f"{record['chunk_id']} was inserted into original_text")
    if re.search(r"\\chunk-\d+n", record["contextualized_text"], re.IGNORECASE):
        raise ValueError(f"{record['chunk_id']} contains malformed context newlines")

    metadata_names = (
        "direction_metadata", "state_metadata", "timer_metadata",
        "asn1_metadata", "requirement_metadata",
    )
    for name in metadata_names:
        if not isinstance(record.get(name), dict) or not isinstance(record[name].get("items"), list):
            raise ValueError(f"{record['chunk_id']} has malformed {name}")


def _write_document_chunks(
    sections: list[dict[str, Any]],
    document_metadata: dict[str, Any],
    chunker: Any,
    output_file: Any,
    chunk_prefix: str,
) -> int:
    """Write every chunk of one document and return the count written.

    The chunk id is namespaced with a per-document prefix so ids stay unique
    across a whole corpus rather than only within a single file.
    """
    from docling_core.types.doc import DoclingDocument

    from mavenier.preprocessing.chunker import iter_chunks

    release = document_metadata.get("release")
    series = document_metadata.get("series")
    document_label = document_metadata.get("document_id") or document_metadata["filename"]

    chunk_number = 0
    for section in sections:
        document = DoclingDocument.model_validate(section["document"])
        markdown_text = str(section.get("markdown_text") or "")
        headings = extract_markdown_headings(markdown_text)
        source_name = str((section.get("metadata") or {}).get("source_name") or document_label)
        for chunk, _docling_context in iter_chunks(document, chunker):
            chunk_number += 1
            original_text = chunk.text
            docling = chunk_metadata(chunk)
            matched_section = find_section_for_chunk(
                chunk_text=original_text,
                sections=headings,
                docling_headings=docling["headings"],
            )
            section_title = matched_section.title if matched_section else None
            section_path = matched_section.path if matched_section else []
            docling["section"] = section_title
            docling["section_path"] = section_path

            content_kind = classify_chunk_content(
                text=original_text,
                section=section_title,
                document_item_types=docling["document_item_types"],
            )
            contextualized = build_contextualized_text(
                filename=document_label,
                section=section_title,
                section_path=section_path,
                original_text=original_text,
                release=release,
                series=series,
            )
            record = {
                "chunk_id": f"{chunk_prefix}-{chunk_number:06d}",
                "content_kind": content_kind,
                "section": section_title,
                "section_path": section_path,
                "original_text": original_text,
                "contextualized_text": contextualized,
                "document_metadata": {
                    **document_metadata,
                    "source_file": source_name,
                },
                "docling_metadata": docling,
                **extract_all_metadata(original_text, content_kind),
            }
            validate_chunk(record)
            output_file.write(json.dumps(record, ensure_ascii=False) + "\n")
    return chunk_number


def process_corpus(
    corpus_root: str | Path,
    output_path: str | Path,
    model_id: str = DEFAULT_MODEL,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    filename: str = "raw.md",
) -> int:
    """Process every spec Markdown file under a 3GPP folder tree.

    Each document's release, series, and spec identity are read from the folder
    path (and version/date from the header when present) and stored as primary
    metadata, so retrieval can pre-filter by those reliable fields.
    """
    try:
        from mavenier.preprocessing.chunker import build_chunker
    except ImportError as exc:
        raise RuntimeError(
            "Chunking packages are not installed. Install requirements.txt."
        ) from exc

    root = Path(corpus_root).expanduser().resolve()
    documents = discover_markdown_documents(root, filename=filename)
    chunker = build_chunker(model_id=model_id, max_tokens=max_tokens)
    destination = Path(output_path).expanduser().resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)

    total_chunks = 0
    documents_written = 0
    try:
        with destination.open("w", encoding="utf-8", newline="\n") as output_file:
            for document_path in documents:
                loaded = load_markdown(document_path, corpus_root=root)
                sections = loaded["sections"]
                document_metadata = loaded["metadata"]
                prefix = document_metadata.get("spec_number") or Path(
                    document_metadata["filename"]
                ).stem or "chunk"
                written = _write_document_chunks(
                    sections, document_metadata, chunker, output_file, chunk_prefix=prefix
                )
                total_chunks += written
                documents_written += 1
                LOGGER.info(
                    "Processed %s: %d chunks", document_metadata.get("document_id", document_path), written
                )
    except OSError as exc:
        raise RuntimeError(f"Could not write {destination}: {exc}") from exc

    LOGGER.info(
        "Wrote %d chunks from %d documents to %s",
        total_chunks,
        documents_written,
        destination,
    )
    return total_chunks
