"""Store and search enriched 3GPP chunks in a local Qdrant database."""

from __future__ import annotations

import copy
import uuid
from pathlib import Path
from typing import Any

from mavenier.rag.retrieval.embeddings import EMBEDDING_DIMENSION, chunk_text

COLLECTION_NAME = "telecom_rag"
DEFAULT_QDRANT_PATH = Path(__file__).resolve().parents[3] / "qdrant_data"
POINT_NAMESPACE = uuid.UUID("b55aa0da-c367-48fb-96ec-05a6b283c4b4")

# These paths match the project's ACTUAL metadata schema. Friendly aliases on
# the left let callers use the shorter conceptual names from the design prompt.
FILTER_FIELD_ALIASES = {
    "direction.direction": "direction_metadata.items[].direction",
    "direction.sender": "direction_metadata.items[].sender",
    "direction.receiver": "direction_metadata.items[].receiver",
    "state.source_state": "state_metadata.items[].current_state",
    "state.target_state": "state_metadata.items[].target_state",
    "timer.timer_name": "timer_metadata.items[].timer_name",
    "asn1.message_name": "asn1_metadata.items[].asn1_entity",
    "requirement.requirement_type": "requirement_metadata.items[].normative_term",
    "section": "section",
}

PAYLOAD_INDEX_FIELDS = tuple(dict.fromkeys(FILTER_FIELD_ALIASES.values()))
METADATA_FIELDS = (
    "direction_metadata",
    "state_metadata",
    "timer_metadata",
    "asn1_metadata",
    "requirement_metadata",
)


def _qdrant_imports() -> tuple[Any, Any]:
    """Import Qdrant lazily so preprocessing can still run independently."""
    try:
        from qdrant_client import QdrantClient, models
    except ImportError as exc:
        raise RuntimeError(
            "Qdrant Client is not installed. Install requirements.txt first."
        ) from exc
    return QdrantClient, models


def get_qdrant_client(path: str | Path = DEFAULT_QDRANT_PATH) -> Any:
    """Open a persistent local Qdrant database—no server or API key needed."""
    QdrantClient, _ = _qdrant_imports()
    storage_path = Path(path).expanduser().resolve()
    try:
        return QdrantClient(path=str(storage_path))
    except Exception as exc:
        raise RuntimeError(f"Could not open Qdrant storage at {storage_path}: {exc}") from exc


def _distance_name(value: Any) -> str:
    raw = getattr(value, "value", value)
    return str(raw).lower().split(".")[-1]


def create_collection_if_needed(
    client: Any,
    collection_name: str = COLLECTION_NAME,
) -> bool:
    """Create a 384/COSINE collection, or safely validate the existing one."""
    _, models = _qdrant_imports()
    try:
        exists = client.collection_exists(collection_name)
        if not exists:
            client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=EMBEDDING_DIMENSION,
                    distance=models.Distance.COSINE,
                ),
            )
            return True

        info = client.get_collection(collection_name)
        vectors = info.config.params.vectors
        if isinstance(vectors, dict):
            raise RuntimeError(
                f"Collection {collection_name!r} uses named vectors; this project "
                "expects one unnamed vector."
            )
        size = getattr(vectors, "size", None)
        distance = _distance_name(getattr(vectors, "distance", None))
        if size != EMBEDDING_DIMENSION or distance != "cosine":
            raise RuntimeError(
                f"Collection {collection_name!r} is incompatible: expected "
                f"size={EMBEDDING_DIMENSION}, distance=COSINE; got "
                f"size={size}, distance={distance}. Existing data was not changed."
            )
        return False
    except RuntimeError:
        raise
    except Exception as exc:
        raise RuntimeError(f"Could not create/check Qdrant collection: {exc}") from exc


def create_payload_indexes(
    client: Any,
    collection_name: str = COLLECTION_NAME,
) -> None:
    """Create keyword indexes only for fields intended for filtering."""
    _, models = _qdrant_imports()
    try:
        info = client.get_collection(collection_name)
        existing = set((getattr(info, "payload_schema", None) or {}).keys())
        for field_name in PAYLOAD_INDEX_FIELDS:
            if field_name not in existing:
                client.create_payload_index(
                    collection_name=collection_name,
                    field_name=field_name,
                    field_schema=models.PayloadSchemaType.KEYWORD,
                    wait=True,
                )
    except Exception as exc:
        raise RuntimeError(f"Could not create Qdrant payload indexes: {exc}") from exc


def stable_point_id(chunk: dict[str, Any]) -> str:
    """Generate the same UUID whenever the same source chunk is ingested."""
    chunk_id = chunk.get("chunk_id")
    if not isinstance(chunk_id, str) or not chunk_id.strip():
        raise ValueError("Every chunk needs a non-empty chunk_id.")
    document = chunk.get("document_metadata") or {}
    identity = "|".join(
        (
            str(document.get("filename") or "unknown-document"),
            str(document.get("source_file") or "unknown-source"),
            chunk_id,
        )
    )
    return str(uuid.uuid5(POINT_NAMESPACE, identity))


def build_payload(chunk: dict[str, Any]) -> dict[str, Any]:
    """Copy the complete record without changing any metadata block."""
    payload = copy.deepcopy(chunk)
    payload.setdefault("text", chunk_text(chunk))
    document = payload.get("document_metadata") or {}
    payload.setdefault(
        "source",
        document.get("source_file") or document.get("filename"),
    )
    return payload


def _validate_vector(vector: Any, label: str) -> list[float]:
    values = vector.tolist() if hasattr(vector, "tolist") else list(vector)
    values = [float(value) for value in values]
    if len(values) != EMBEDDING_DIMENSION:
        raise ValueError(
            f"{label} has {len(values)} dimensions; expected {EMBEDDING_DIMENSION}."
        )
    return values


def store_chunks(
    client: Any,
    chunks: list[dict[str, Any]],
    embeddings: list[list[float]],
    collection_name: str = COLLECTION_NAME,
    upload_batch_size: int = 64,
) -> int:
    """Upsert chunks, so re-ingestion replaces rather than duplicates them."""
    if len(chunks) != len(embeddings):
        raise ValueError("The number of chunks and embeddings must match.")
    if upload_batch_size < 1:
        raise ValueError("upload_batch_size must be at least 1.")
    if not chunks:
        return 0

    _, models = _qdrant_imports()
    points = []
    for chunk, vector in zip(chunks, embeddings):
        chunk_id = str(chunk.get("chunk_id") or "<unknown>")
        points.append(
            models.PointStruct(
                id=stable_point_id(chunk),
                vector=_validate_vector(vector, chunk_id),
                payload=build_payload(chunk),
            )
        )

    try:
        for start in range(0, len(points), upload_batch_size):
            client.upsert(
                collection_name=collection_name,
                points=points[start:start + upload_batch_size],
                wait=True,
            )
    except Exception as exc:
        raise RuntimeError(f"Could not store chunks in Qdrant: {exc}") from exc
    return len(points)


def build_filter(filters: dict[str, Any] | None) -> Any | None:
    """Convert reusable exact-match filters into a Qdrant filter."""
    if not filters:
        return None
    _, models = _qdrant_imports()
    conditions = []
    for requested_field, value in filters.items():
        field_name = FILTER_FIELD_ALIASES.get(requested_field, requested_field)
        if value is None:
            continue
        if isinstance(value, (list, tuple, set)):
            match = models.MatchAny(any=list(value))
        else:
            match = models.MatchValue(value=value)
        conditions.append(models.FieldCondition(key=field_name, match=match))
    return models.Filter(must=conditions) if conditions else None


def search_similar(
    client: Any,
    query_vector: list[float],
    limit: int = 5,
    filters: dict[str, Any] | None = None,
    collection_name: str = COLLECTION_NAME,
) -> list[dict[str, Any]]:
    """Return semantic matches with their original text and metadata."""
    if limit < 1:
        raise ValueError("limit must be at least 1.")
    vector = _validate_vector(query_vector, "Query vector")
    try:
        response = client.query_points(
            collection_name=collection_name,
            query=vector,
            query_filter=build_filter(filters),
            with_payload=True,
            with_vectors=False,
            limit=limit,
        )
    except Exception as exc:
        raise RuntimeError(f"Qdrant similarity search failed: {exc}") from exc

    results = []
    for point in response.points:
        payload = dict(point.payload or {})
        document = payload.get("document_metadata") or {}
        metadata = {
            name: copy.deepcopy(payload.get(name, {"items": []}))
            for name in METADATA_FIELDS
        }
        results.append({
            "score": float(point.score),
            "text": payload.get("original_text") or payload.get("text"),
            "source": payload.get("source") or document.get("source_file") or document.get("filename"),
            "section": payload.get("section"),
            "metadata": metadata,
            "payload": payload,
        })
    return results

