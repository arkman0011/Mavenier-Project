"""Load Markdown as structured Docling documents."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import Any

from docling.backend.md_backend import MarkdownDocumentBackend
from docling.datamodel.base_models import InputFormat
from docling.datamodel.document import InputDocument

LOGGER = logging.getLogger(__name__)

SOURCE_RE = re.compile(
    r"(?m)^\s*<!--\s*=+\s*SOURCE FILE:\s*(.+?)\s*=+\s*-->\s*$"
)
RELEASE_RE = re.compile(r"^Rel[-_]?(\d+)$", re.I)
SERIES_RE = re.compile(r"^(\d{2})[_-]?series$", re.I)
SPEC_RE = re.compile(r"^\d{4,5}$")

DOC_ID_RE = re.compile(
    r"\b3GPP\s+T[SR]\s+(\d{2})\.(\d{2,4})\b",
    re.I,
)
VERSION_RE = re.compile(r"\bV(\d+(?:\.\d+){1,2})\b")
DATE_RE = re.compile(r"\((\d{4}-\d{2})\)")


@dataclass(frozen=True)
class MarkdownHeading:
    """A heading plus its hierarchy and source-text position."""

    title: str
    path: list[str]
    start: int
    end: int
    content: str


def read_markdown(path: str | Path) -> tuple[Path, str]:
    """Validate and read a Markdown file."""

    source = Path(path).expanduser().resolve()

    if not source.is_file():
        raise FileNotFoundError(f"File does not exist: {source}")

    if source.suffix.lower() not in {".md", ".markdown"}:
        raise ValueError("Input must be a Markdown file")

    try:
        text = source.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError("Markdown must use UTF-8 encoding") from exc

    if not text.strip():
        raise ValueError(f"Markdown file is empty: {source}")

    return source, text


def split_sources(text: str, filename: str) -> list[tuple[str, str]]:
    """Split Markdown containing SOURCE FILE markers."""

    markers = list(SOURCE_RE.finditer(text))

    if not markers:
        return [(filename, text)]

    sections = [
        (
            marker.group(1).strip(),
            text[
                marker.end():
                markers[i + 1].start() if i + 1 < len(markers) else len(text)
            ].strip(),
        )
        for i, marker in enumerate(markers)
    ]

    sections = [(name, content) for name, content in sections if content]

    if not sections:
        raise ValueError("Combined Markdown contains no content")

    return sections


# Compatibility name retained for callers while the loader keeps its compact
# internal implementation.
split_combined_markdown = split_sources


def extract_markdown_headings(text: str) -> list[MarkdownHeading]:
    """Return Markdown headings with hierarchy and section boundaries."""
    matches = list(re.finditer(r"(?m)^(#{1,6})\s+(.+?)\s*$", text))
    headings: list[MarkdownHeading] = []
    stack: list[str] = []
    for index, match in enumerate(matches):
        level = len(match.group(1))
        title = match.group(2).strip()
        stack = stack[: level - 1]
        stack.append(title)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        headings.append(
            MarkdownHeading(
                title=title,
                path=list(stack),
                start=match.start(),
                end=end,
                content=text[match.start():end],
            )
        )
    return headings


def find_section_for_chunk(
    chunk_text: str,
    sections: list[MarkdownHeading],
    docling_headings: list[str] | None = None,
) -> MarkdownHeading | None:
    """Match a chunk to Docling headings first, then to its source section."""
    normalized = [value.strip().casefold() for value in (docling_headings or [])]
    for heading in reversed(sections):
        if heading.title.casefold() in normalized:
            return heading
    for heading in sections:
        if chunk_text.strip() and chunk_text.strip() in heading.content:
            return heading
    # A direct text-position lookup needs the original document, which compact
    # heading records intentionally do not retain. The nearest heading whose
    # title appears in the chunk is still a useful fallback.
    for heading in reversed(sections):
        if heading.title.casefold() in chunk_text.casefold():
            return heading
    return sections[-1] if sections else None


def path_metadata(
    source: str | Path,
    corpus_root: str | Path | None = None,
) -> dict[str, Any]:
    """Extract release, series and specification from the path."""

    source = Path(source).expanduser().resolve()
    metadata: dict[str, Any] = {}

    for part in source.parts:
        if match := RELEASE_RE.fullmatch(part):
            metadata.update(
                release=f"Rel-{match.group(1)}",
                release_number=int(match.group(1)),
            )
        elif match := SERIES_RE.fullmatch(part):
            metadata["series"] = match.group(1)
        elif SPEC_RE.fullmatch(part):
            metadata["spec_number"] = part

    series = metadata.get("series")
    spec = metadata.get("spec_number")

    if series and spec and spec.startswith(series):
        metadata["document_id"] = f"TS {series}.{spec[len(series):]}"
    elif spec:
        metadata["document_id"] = f"TS {spec}"

    if corpus_root:
        try:
            root = Path(corpus_root).expanduser().resolve()
            metadata["relative_path"] = source.relative_to(root).as_posix()
        except ValueError:
            metadata["relative_path"] = source.name

    return metadata


parse_document_path = path_metadata


def header_metadata(text: str) -> dict[str, Any]:
    """Extract document ID, version and date from the header."""

    header = "\n".join(text.splitlines()[:40])
    metadata: dict[str, Any] = {}

    if match := DOC_ID_RE.search(header):
        metadata["document_id"] = f"TS {match.group(1)}.{match.group(2)}"

    if match := VERSION_RE.search(header):
        metadata["version"] = f"V{match.group(1)}"

    if match := DATE_RE.search(header):
        metadata.update(
            date=match.group(1),
            year=int(match.group(1)[:4]),
        )

    return metadata


parse_document_header = header_metadata


def discover_markdown_documents(
    corpus_root: str | Path,
    filename: str = "raw.md",
) -> list[Path]:
    """Find source documents deterministically below the corpus root."""
    root = Path(corpus_root).expanduser().resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"Corpus folder does not exist: {root}")
    documents = sorted(path for path in root.rglob(filename) if path.is_file())
    if not documents:
        raise FileNotFoundError(f"No {filename} files found under {root}")
    return documents


def load_markdown(
    path: str | Path,
    corpus_root: str | Path | None = None,
) -> dict[str, Any]:
    """Return metadata and structured Docling sections."""

    source, text = read_markdown(path)
    sources = split_sources(text, source.name)
    common_metadata = path_metadata(source, corpus_root)

    sections = []

    for index, (name, markdown) in enumerate(sources):
        try:
            # Construct only Docling's Markdown backend. Importing the general
            # DocumentConverter also imports PDF/OCR pipelines, which defeats
            # the purpose of the lightweight format-markdown installation.
            input_document = InputDocument(
                path_or_stream=BytesIO(markdown.encode("utf-8")),
                format=InputFormat.MD,
                backend=MarkdownDocumentBackend,
                filename=name,
            )
            if not input_document.valid:
                raise RuntimeError("Docling rejected the Markdown input")
            document = input_document._backend.convert()
        except Exception as exc:
            raise RuntimeError(f"Could not parse {name}: {exc}") from exc

        sections.append(
            {
                "metadata": {
                    **common_metadata,
                    **header_metadata(markdown),
                    "source_name": name,
                    "section_index": index,
                },
                "markdown_text": markdown,
                "document": document.export_to_dict(),
            }
        )

    metadata = {
        **common_metadata,
        **header_metadata(text),
        "filename": source.name,
        "format": "markdown",
        "source_section_count": len(sections),
    }

    LOGGER.info("Loaded %d section(s) from %s", len(sections), source.name)

    return {"metadata": metadata, "sections": sections}
