import pytest

from mavenier.rag.ingestion.pipeline import build_contextualized_text, validate_chunk


def _empty_metadata():
    return {
        "direction_metadata": {"items": []},
        "state_metadata": {"items": []},
        "timer_metadata": {"items": []},
        "asn1_metadata": {"items": []},
        "requirement_metadata": {"items": []},
    }


def test_context_has_real_newlines_and_does_not_change_original():
    original = "The UE shall start timer T300."
    context = build_contextualized_text(
        "MD Combined.md",
        "5.3 Connection control",
        ["5 RRC procedures", "5.3 Connection control"],
        original,
    )
    assert context == (
        "Document: MD Combined.md\n"
        "Section: 5.3 Connection control\n"
        "Section path: 5 RRC procedures > 5.3 Connection control\n\n"
        "The UE shall start timer T300."
    )
    assert "chunk-" not in original
    assert "\\chunk-" not in context


def test_validation_accepts_consistent_empty_metadata():
    record = {
        "chunk_id": "chunk-000001",
        "original_text": "Technical text.",
        "contextualized_text": "Document: test.md\n\nTechnical text.",
        **_empty_metadata(),
    }
    validate_chunk(record)


def test_validation_rejects_chunk_id_inside_original_text():
    record = {
        "chunk_id": "chunk-000001",
        "original_text": "Text chunk-000001 was corrupted.",
        "contextualized_text": "Document: test.md\n\nText.",
        **_empty_metadata(),
    }
    with pytest.raises(ValueError, match="inserted"):
        validate_chunk(record)

