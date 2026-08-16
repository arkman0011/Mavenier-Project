"""Coordinate Markdown loading, Docling chunking, extraction, and JSONL output."""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any

from mavenier.rag.ingestion.content_classifier import classify_chunk_content
from mavenier.rag.ingestion.loader import find_section_for_chunk, load_markdown
from mavenier.rag.ingestion.metadata_extractor import extract_all_metadata

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
) -> str:
    """Build clean embedding text without changing the original chunk."""
    context_lines = [f"Document: {filename}"]
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

    valid_terms = {"shall", "shall not", "should", "should not", "may", "need not"}
    for requirement in record["requirement_metadata"]["items"]:
        if requirement.get("normative_term") not in valid_terms:
            raise ValueError(f"{record['chunk_id']} has an invalid normative term")
        if not requirement.get("requirement_action"):
            raise ValueError(f"{record['chunk_id']} has a requirement without an action")


def process_markdown(
    input_path: str | Path,
    output_path: str | Path,
    model_id: str = DEFAULT_MODEL,
    max_tokens: int = DEFAULT_MAX_TOKENS,
) -> int:
    """Process one Markdown file and return the number of chunks written."""
    # Docling is imported only for a real run. Formatting and validation tests stay
    # lightweight and give clearer errors when dependencies have not been installed.
    try:
        from mavenier.rag.ingestion.chunker import build_chunker, iter_chunks
    except ImportError as exc:
        raise RuntimeError(
            "Chunking packages are not installed. Install requirements.txt."
        ) from exc

    sections, document_metadata = load_markdown(input_path)
    chunker = build_chunker(model_id=model_id, max_tokens=max_tokens)
    destination = Path(output_path).expanduser().resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)

    chunk_number = 0
    try:
        with destination.open("w", encoding="utf-8", newline="\n") as output_file:
            for section in sections:
                for chunk, _docling_context in iter_chunks(section.document, chunker):
                    chunk_number += 1
                    original_text = chunk.text
                    docling = chunk_metadata(chunk)
                    matched_section = find_section_for_chunk(
                        chunk_text=original_text,
                        sections=section.headings,
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
                        filename=document_metadata["filename"],
                        section=section_title,
                        section_path=section_path,
                        original_text=original_text,
                    )
                    record = {
                        "chunk_id": f"chunk-{chunk_number:06d}",
                        "content_kind": content_kind,
                        "section": section_title,
                        "section_path": section_path,
                        "original_text": original_text,
                        "contextualized_text": contextualized,
                        "document_metadata": {
                            **document_metadata,
                            "source_file": section.source_name,
                        },
                        "docling_metadata": docling,
                        **extract_all_metadata(original_text, content_kind),
                    }
                    validate_chunk(record)
                    output_file.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError as exc:
        raise RuntimeError(f"Could not write {destination}: {exc}") from exc

    LOGGER.info("Wrote %d chunks to %s", chunk_number, destination)
    return chunk_number

