"""Real local-Qdrant smoke test; skipped until qdrant-client is installed."""

import pytest

qdrant_client = pytest.importorskip("qdrant_client")

from mavenier.rag.retrieval.vector_store import (  # noqa: E402
    create_collection_if_needed,
    get_qdrant_client,
    search_similar,
    store_chunks,
)


def test_real_local_qdrant_round_trip(tmp_path):
    client = get_qdrant_client(tmp_path / "qdrant")
    assert create_collection_if_needed(client) is True
    chunk = {
        "chunk_id": "smoke-1",
        "original_text": "The UE starts timer T300.",
        "section": "Timers",
        "document_metadata": {"filename": "test.md", "source_file": "test.md"},
        "direction_metadata": {"items": []},
        "state_metadata": {"items": []},
        "timer_metadata": {"items": [{"timer_name": "T300"}]},
        "asn1_metadata": {"items": []},
        "requirement_metadata": {"items": []},
    }
    vector = [1.0] + [0.0] * 383
    store_chunks(client, [chunk], [vector])
    results = search_similar(client, vector, limit=1)
    assert results[0]["text"] == chunk["original_text"]
    assert results[0]["metadata"]["timer_metadata"] == chunk["timer_metadata"]

