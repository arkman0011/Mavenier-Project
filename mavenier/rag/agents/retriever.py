"""Node 3: reuse BGE and local Qdrant retrieval."""

from __future__ import annotations

from mavenier.rag.agents.common import node_update
from mavenier.rag.graph.state import RAGState
from mavenier.rag.retrieval.pipeline import search_text

CANDIDATE_TOP_K = 10


def retriever_node(state: RAGState) -> dict:
    try:
        chunks = search_text(
            query=state["search_query"],
            qdrant_path=state["qdrant_path"],
            limit=CANDIDATE_TOP_K,
            filters=state.get("filters"),
        )
    except (ValueError, RuntimeError) as exc:
        raise RuntimeError(f"Retrieval system error: {exc}") from exc
    summary = [
        {
            "score": chunk.get("score"),
            "source": chunk.get("source"),
            "section": chunk.get("section"),
        }
        for chunk in chunks
    ]
    return node_update(
        state,
        "retriever",
        {"count": len(chunks), "candidates": summary},
        retrieved_chunks=chunks,
    )
