"""Connect existing JSONL chunks to BGE embeddings and local Qdrant."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from mavenier.rag.retrieval.embeddings import embed_chunks, embed_query, load_embedding_model, load_tokenizer
from mavenier.rag.retrieval.vector_store import (
    COLLECTION_NAME,
    DEFAULT_QDRANT_PATH,
    create_collection_if_needed,
    create_payload_indexes,
    get_qdrant_client,
    search_similar,
    store_chunks,
)


def load_chunks_from_jsonl(jsonl_path: str | Path) -> list[dict[str, Any]]:
    """Read preprocessing records and report the exact malformed line."""
    source = Path(jsonl_path).expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(
            f"Chunk file not found: {source}. Run `python -m scripts.run_pipeline` first."
        )

    chunks = []
    try:
        with source.open("r", encoding="utf-8") as input_file:
            for line_number, line in enumerate(input_file, start=1):
                if not line.strip():
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(
                        f"Invalid JSON on line {line_number} of {source}: {exc}"
                    ) from exc
                if not isinstance(record, dict):
                    raise ValueError(
                        f"Line {line_number} of {source} is not a JSON object."
                    )
                chunks.append(record)
    except OSError as exc:
        raise RuntimeError(f"Could not read {source}: {exc}") from exc

    if not chunks:
        raise ValueError(f"No chunks were found in {source}.")
    return chunks


def ingest_jsonl(
    jsonl_path: str | Path,
    qdrant_path: str | Path = DEFAULT_QDRANT_PATH,
    collection_name: str = COLLECTION_NAME,
) -> dict[str, Any]:
    """Embed all JSONL chunks and safely upsert them into local Qdrant."""
    chunks = load_chunks_from_jsonl(jsonl_path)
    tokenizer = load_tokenizer()
    model = load_embedding_model()
    vectors = embed_chunks(chunks, model=model, tokenizer=tokenizer)

    client = get_qdrant_client(qdrant_path)
    created = create_collection_if_needed(client, collection_name)
    create_payload_indexes(client, collection_name)
    stored = store_chunks(client, chunks, vectors, collection_name)
    return {
        "collection": collection_name,
        "collection_created": created,
        "chunks_stored": stored,
        "qdrant_path": str(Path(qdrant_path).expanduser().resolve()),
    }


def search_text(
    query: str,
    qdrant_path: str | Path = DEFAULT_QDRANT_PATH,
    limit: int = 5,
    filters: dict[str, Any] | None = None,
    collection_name: str = COLLECTION_NAME,
) -> list[dict[str, Any]]:
    """Embed a query with BGE and retrieve matching stored chunks."""
    tokenizer = load_tokenizer()
    model = load_embedding_model()
    query_vector = embed_query(query, model=model, tokenizer=tokenizer)
    client = get_qdrant_client(qdrant_path)
    if not client.collection_exists(collection_name):
        raise RuntimeError(
            f"Collection {collection_name!r} does not exist. Run ingestion first."
        )
    return search_similar(
        client=client,
        query_vector=query_vector,
        limit=limit,
        filters=filters,
        collection_name=collection_name,
    )

