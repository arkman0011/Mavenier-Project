"""Load one Markdown file, including a file made from several source files."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

LOGGER = logging.getLogger(__name__)

# Example boundary in the supplied file:
# <!-- ===== SOURCE FILE: raw__1_.md ===== -->
SOURCE_MARKER = re.compile(
    r"(?m)^\s*<!--\s*=+\s*SOURCE FILE:\s*(.+?)\s*=+\s*-->\s*$"
)


@dataclass
class MarkdownSection:
    """One Markdown heading and the text that belongs directly below it."""

    level: int
    title: str
    path: list[str]
    content: str


@dataclass
class LoadedSection:
    """One source section and its converted Docling document."""

    source_name: str
    markdown_text: str
    headings: list[MarkdownSection]
    document: Any


HEADING_PATTERN = re.compile(r"(?m)^(#{1,6})[ \t]+(.+?)\s*$")


def _clean_heading(title: str) -> str:
    """Remove common Markdown decoration while preserving the heading wording."""
    title = re.sub(r"\s+#+\s*$", "", title).strip()
    return title.strip("*_` ")


def extract_markdown_headings(text: str) -> list[MarkdownSection]:
    """Extract each heading and its parent hierarchy with a small regex parser."""
    matches = list(HEADING_PATTERN.finditer(text))
    hierarchy: list[str] = []
    sections: list[MarkdownSection] = []

    for index, match in enumerate(matches):
        level = len(match.group(1))
        title = _clean_heading(match.group(2))
        if not title:
            continue

        # A level-3 heading replaces the previous level-3 branch but retains
        # levels 1 and 2 as its parents.
        hierarchy = hierarchy[: level - 1]
        hierarchy.append(title)
        content_end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append(
            MarkdownSection(
                level=level,
                title=title,
                path=hierarchy.copy(),
                content=text[match.end():content_end].strip(),
            )
        )
    return sections


def _normalise_for_matching(text: str) -> str:
    """Normalize whitespace/Markdown punctuation only for section matching."""
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def find_section_for_chunk(
    chunk_text: str,
    sections: list[MarkdownSection],
    docling_headings: list[str] | None = None,
) -> MarkdownSection | None:
    """Find the nearest section using Docling headings, then source-text evidence."""
    valid_docling_headings = [
        _clean_heading(value) for value in (docling_headings or []) if value.strip()
    ]
    if valid_docling_headings:
        current_title = valid_docling_headings[-1]
        for section in reversed(sections):
            if section.title == current_title:
                return section

    normalized_chunk = _normalise_for_matching(chunk_text)
    if not normalized_chunk:
        return None

    # Exact text evidence is preferred. A short probe tolerates a chunk that is
    # smaller than its complete source section.
    probe = " ".join(normalized_chunk.split()[:20])
    for section in sections:
        source_text = _normalise_for_matching(f"{section.title} {section.content}")
        if probe and probe in source_text:
            return section

    # Final conservative fallback: choose a section only when several meaningful
    # words overlap. Returning None is better than attaching a wrong heading.
    chunk_words = set(normalized_chunk.split())
    best_section = None
    best_score = 0
    for section in sections:
        section_words = set(_normalise_for_matching(section.content).split())
        score = len(chunk_words & section_words)
        if score > best_score:
            best_section, best_score = section, score
    return best_section if best_score >= 4 else None


def split_combined_markdown(text: str, fallback_name: str) -> list[tuple[str, str]]:
    """Split a combined file at SOURCE FILE comments.

    A normal Markdown file without these comments is returned as one section.
    """
    markers = list(SOURCE_MARKER.finditer(text))
    if not markers:
        return [(fallback_name, text)]

    sections: list[tuple[str, str]] = []
    for index, marker in enumerate(markers):
        content_start = marker.end()
        content_end = markers[index + 1].start() if index + 1 < len(markers) else len(text)
        content = text[content_start:content_end].strip()
        if content:
            sections.append((marker.group(1).strip(), content))
    return sections


def load_markdown(path: str | Path) -> tuple[list[LoadedSection], dict[str, Any]]:
    """Read UTF-8 Markdown and convert every source section with Docling."""
    # Import here so the lightweight source splitter can be tested independently.
    # If packages are missing, the error clearly points to requirements.txt.
    try:
        from docling.datamodel.base_models import InputFormat
        from docling.document_converter import DocumentConverter
    except ImportError as exc:
        raise RuntimeError(
            "Docling is not installed. Install the packages in requirements.txt."
        ) from exc

    source = Path(path).expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(f"Markdown file does not exist: {source}")
    if source.suffix.lower() not in {".md", ".markdown"}:
        raise ValueError("Input must be a .md or .markdown file")

    try:
        text = source.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{source.name} is not valid UTF-8 Markdown") from exc
    if not text.strip():
        raise ValueError(f"Markdown file is empty: {source}")

    raw_sections = split_combined_markdown(text, source.name)
    LOGGER.info("Found %d source section(s) in %s", len(raw_sections), source.name)

    # Markdown uses Docling's SimplePipeline. No OCR, page rendering, or layout AI
    # model is needed.
    converter = DocumentConverter(allowed_formats=[InputFormat.MD])
    loaded: list[LoadedSection] = []
    for source_name, section_text in raw_sections:
        try:
            result = converter.convert_string(
                content=section_text,
                format=InputFormat.MD,
                name=source_name,
            )
        except Exception as exc:
            raise RuntimeError(f"Docling could not read section {source_name}: {exc}") from exc
        loaded.append(
            LoadedSection(
                source_name=source_name,
                markdown_text=section_text,
                headings=extract_markdown_headings(section_text),
                document=result.document,
            )
        )

    metadata = {
        "filename": source.name,
        "source_path": str(source),
        "format": "markdown",
        "source_section_count": len(loaded),
    }
    return loaded, metadata

