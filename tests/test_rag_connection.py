from types import SimpleNamespace

import mavenier.rag.retrieval.vector_store as vector_store
import mavenier.rag.retrieval.pipeline as retrieval_pipeline
from mavenier.rag.retrieval.embeddings import EMBEDDING_DIMENSION, embed_chunks
from mavenier.rag.retrieval.vector_store import search_similar, store_chunks


class FakeTokenizer:
    def encode(self, text, add_special_tokens=True, truncation=False):
        return list(range(len(text.split()) + 2))


class FakeEmbeddingModel:
    def encode(self, texts, **kwargs):
        return [[1.0] + [0.0] * (EMBEDDING_DIMENSION - 1) for _ in texts]


class FakePointStruct:
    def __init__(self, id, vector, payload):
        self.id = id
        self.vector = vector
        self.payload = payload


class FakeMatchValue:
    def __init__(self, value):
        self.value = value


class FakeMatchAny:
    def __init__(self, any):
        self.any = any


class FakeFieldCondition:
    def __init__(self, key, match):
        self.key = key
        self.match = match


class FakeFilter:
    def __init__(self, must):
        self.must = must


class FakeModels:
    PointStruct = FakePointStruct
    MatchValue = FakeMatchValue
    MatchAny = FakeMatchAny
    FieldCondition = FakeFieldCondition
    Filter = FakeFilter


class FakeQdrantClient:
    def __init__(self):
        self.points = []

    def upsert(self, collection_name, points, wait):
        self.points.extend(points)

    def query_points(self, **kwargs):
        point = self.points[0]
        scored = SimpleNamespace(score=0.99, payload=point.payload)
        return SimpleNamespace(points=[scored])


def test_chunk_to_vector_to_storage_to_retrieval_preserves_metadata(monkeypatch):
    monkeypatch.setattr(
        vector_store,
        "_qdrant_imports",
        lambda: (FakeQdrantClient, FakeModels),
    )
    chunk = {
        "chunk_id": "chunk-000001",
        "original_text": "The UE shall start T300.",
        "section": "RRC connection establishment",
        "document_metadata": {"filename": "38.331.md", "source_file": "38.331.md"},
        "direction_metadata": {"items": []},
        "state_metadata": {"items": [{"current_state": "RRC_IDLE"}]},
        "timer_metadata": {"items": [{"timer_name": "T300"}]},
        "asn1_metadata": {"items": []},
        "requirement_metadata": {"items": [{"normative_term": "shall"}]},
    }
    original_metadata = {
        name: chunk[name]
        for name in (
            "direction_metadata", "state_metadata", "timer_metadata",
            "asn1_metadata", "requirement_metadata",
        )
    }

    vectors = embed_chunks(
        [chunk], model=FakeEmbeddingModel(), tokenizer=FakeTokenizer()
    )
    assert len(vectors[0]) == 384

    client = FakeQdrantClient()
    assert store_chunks(client, [chunk], vectors) == 1
    results = search_similar(client, vectors[0], limit=1)

    assert results[0]["text"] == chunk["original_text"]
    assert results[0]["metadata"] == original_metadata
    assert results[0]["payload"]["timer_metadata"] == chunk["timer_metadata"]


def test_search_pipeline_closes_local_qdrant_client(monkeypatch):
    class ClosableClient:
        closed = False

        def collection_exists(self, name):
            return True

        def close(self):
            self.closed = True

    client = ClosableClient()
    monkeypatch.setattr(retrieval_pipeline, "load_tokenizer", lambda: object())
    monkeypatch.setattr(retrieval_pipeline, "load_embedding_model", lambda: object())
    monkeypatch.setattr(
        retrieval_pipeline,
        "embed_query",
        lambda query, model, tokenizer: [1.0] + [0.0] * 383,
    )
    monkeypatch.setattr(retrieval_pipeline, "get_qdrant_client", lambda path: client)
    monkeypatch.setattr(
        retrieval_pipeline,
        "search_similar",
        lambda **kwargs: [{"text": "result"}],
    )

    assert retrieval_pipeline.search_text("RRC") == [{"text": "result"}]
    assert client.closed is True
