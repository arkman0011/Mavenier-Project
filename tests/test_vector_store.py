import copy

import pytest

from mavenier.rag.retrieval.vector_store import build_payload, stable_point_id


def sample_chunk():
    return {
        "chunk_id": "chunk-000001",
        "original_text": "The UE shall start T300.",
        "section": "RRC establishment",
        "document_metadata": {
            "filename": "MD Combined.md",
            "source_file": "raw.md",
        },
        "direction_metadata": {"items": []},
        "state_metadata": {"items": []},
        "timer_metadata": {"items": [{"timer_name": "T300"}]},
        "asn1_metadata": {"items": []},
        "requirement_metadata": {"items": [{"normative_term": "shall"}]},
    }


def test_payload_preserves_all_five_metadata_blocks_unchanged():
    chunk = sample_chunk()
    before = copy.deepcopy(chunk)
    payload = build_payload(chunk)
    for name in (
        "direction_metadata", "state_metadata", "timer_metadata",
        "asn1_metadata", "requirement_metadata",
    ):
        assert payload[name] == before[name]
    assert chunk == before
    assert payload["text"] == chunk["original_text"]


def test_stable_point_id_is_repeatable_and_source_sensitive():
    first = sample_chunk()
    second = copy.deepcopy(first)
    assert stable_point_id(first) == stable_point_id(first)
    second["document_metadata"]["source_file"] = "another.md"
    assert stable_point_id(first) != stable_point_id(second)


def test_stable_point_id_requires_chunk_id():
    with pytest.raises(ValueError, match="chunk_id"):
        stable_point_id({})

