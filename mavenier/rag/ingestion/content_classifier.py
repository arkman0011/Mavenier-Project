"""Small rule-based classifier that separates boilerplate from technical text."""

from __future__ import annotations

import re

# These are ordinary tuples so a beginner can add terms later.
TECHNICAL_SIGNALS = (
    "ue", "network", "gnb", "enb", "rrc", "lower layers", "upper layers",
    "e-utran", "nr", "entity", "message", "procedure", "timer", "bearer",
    "channel", "protocol", "radio", "cell", "nas", "amf", "uicc", "usim",
)

BOILERPLATE_KINDS = {
    "front_matter", "table_of_contents", "copyright", "foreword",
}


def contains_technical_signal(text: str) -> bool:
    """Return True when text explicitly contains configurable 3GPP terminology."""
    lowered = text.lower()
    return any(re.search(rf"\b{re.escape(term)}\b", lowered) for term in TECHNICAL_SIGNALS)


def classify_chunk_content(
    text: str,
    section: str | None,
    document_item_types: list[str] | None = None,
) -> str:
    """Classify a chunk with transparent, CPU-friendly rules."""
    lowered_text = text.lower()
    lowered_section = (section or "").lower()
    item_types = {value.lower() for value in (document_item_types or [])}

    if "copyright" in lowered_section or "copyright notification" in lowered_text:
        return "copyright"
    if "contents" in lowered_section or "table of contents" in lowered_text:
        return "table_of_contents"
    if "foreword" in lowered_section:
        return "foreword"
    if "references" in lowered_section:
        return "references"
    if (
        "the present document" in lowered_text
        or "3gpp support office" in lowered_text
        or "postal address" in lowered_text
        or "shall not be implemented" in lowered_text
    ):
        return "front_matter"
    if re.search(r"(?m)^\s*[A-Za-z][\w-]*\s*::=", text):
        return "asn1_definition"
    if "table" in item_types or re.search(r"(?m)^\s*\|.+\|\s*$", text):
        return "table"
    if contains_technical_signal(f"{section or ''} {text}"):
        return "technical_procedure"
    return "general_text"


def should_extract_requirements(content_kind: str, text: str) -> bool:
    """Require both a non-boilerplate class and explicit technical evidence."""
    return content_kind not in BOILERPLATE_KINDS and contains_technical_signal(text)

