from types import SimpleNamespace

import pytest

fastapi = pytest.importorskip("fastapi")

from fastapi import HTTPException  # noqa: E402

import mavenier.api.app as api  # noqa: E402


def test_health_check_does_not_load_models():
    assert api.health_check() == {"status": "ok"}


def test_root_describes_available_routes():
    assert api.service_information() == {
        "name": "3GPP Telecom RAG API",
        "status": "ok",
        "documentation": "/docs",
        "health": "/health",
    }


def test_startup_skips_ingestion_when_collection_has_points(monkeypatch):
    class FakeClient:
        closed = False

        def collection_exists(self, name):
            return name == "telecom_rag"

        def get_collection(self, name):
            return SimpleNamespace(points_count=12)

        def close(self):
            self.closed = True

    client = FakeClient()
    monkeypatch.setattr(api, "get_qdrant_client", lambda path: client)
    monkeypatch.setattr(
        api,
        "ingest_jsonl",
        lambda *args: pytest.fail("Existing collection must not be re-ingested"),
    )

    api.prepare_knowledge_base()
    assert client.closed is True


def test_startup_ingests_existing_chunk_file_when_collection_is_missing(
    monkeypatch, tmp_path
):
    class FakeClient:
        def collection_exists(self, name):
            return False

        def close(self):
            pass

    chunk_file = tmp_path / "enriched_chunks.jsonl"
    chunk_file.write_text('{"chunk_id":"chunk-1"}\n', encoding="utf-8")
    received = {}

    monkeypatch.setattr(api, "CHUNK_FILE", chunk_file)
    monkeypatch.setattr(api, "QDRANT_FOLDER", tmp_path / "qdrant_data")
    monkeypatch.setattr(api, "get_qdrant_client", lambda path: FakeClient())

    def fake_ingest(jsonl_path, qdrant_path, collection_name):
        received.update(
            jsonl_path=jsonl_path,
            qdrant_path=qdrant_path,
            collection_name=collection_name,
        )
        return {"chunks_stored": 1}

    monkeypatch.setattr(api, "ingest_jsonl", fake_ingest)
    api.prepare_knowledge_base()

    assert received == {
        "jsonl_path": chunk_file,
        "qdrant_path": tmp_path / "qdrant_data",
        "collection_name": "telecom_rag",
    }


def test_startup_asks_to_build_dataset_when_missing(monkeypatch, tmp_path):
    class FakeClient:
        def collection_exists(self, name):
            return False

        def close(self):
            pass

    monkeypatch.setattr(api, "CHUNK_FILE", tmp_path / "missing.jsonl")
    monkeypatch.setattr(api, "get_qdrant_client", lambda path: FakeClient())

    with pytest.raises(FileNotFoundError, match="build_dataset"):
        api.prepare_knowledge_base()


def test_ask_endpoint_calls_agentic_pipeline(monkeypatch):
    received = {}

    def fake_ask_agentic_rag(question, filters, debug):
        received.update(question=question, filters=filters, debug=debug)
        return {
            "answer": "Grounded answer",
            "confidence": 0.92,
            "sources": [{"source": "38.331.md", "section": "Definitions"}],
        }

    monkeypatch.setattr(api, "ask_agentic_rag", fake_ask_agentic_rag)
    response = api.ask_question(
        api.AskRequest(
            question="What is RRC?",
            filters={"section": "Definitions"},
            debug=False,
        )
    )
    assert response.answer == "Grounded answer"
    assert response.confidence == 0.92
    assert response.sources == [{"source": "38.331.md", "section": "Definitions"}]
    assert received == {
        "question": "What is RRC?",
        "filters": {"section": "Definitions"},
        "debug": False,
    }


def test_invalid_query_error_becomes_http_400(monkeypatch):
    def fail(**kwargs):
        raise ValueError("Question cannot be empty.")

    monkeypatch.setattr(api, "ask_agentic_rag", fail)
    with pytest.raises(HTTPException) as caught:
        api.ask_question(api.AskRequest(question=" "))
    assert caught.value.status_code == 400


def test_rate_limit_error_becomes_http_429(monkeypatch):
    def fail(**kwargs):
        raise RuntimeError("Gemini rate limit or quota was reached.")

    monkeypatch.setattr(api, "ask_agentic_rag", fail)
    with pytest.raises(HTTPException) as caught:
        api.ask_question(api.AskRequest(question="What is RRC?"))
    assert caught.value.status_code == 429
