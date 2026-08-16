"""Node 4: reuse the existing cross-encoder reranker."""

from __future__ import annotations

from mavenier.rag.agents.common import node_update
from mavenier.rag.graph.state import RAGState
from mavenier.rag.retrieval.reranker import DEFAULT_TOP_N, rerank_results


def reranker_node(state: RAGState) -> dict:
    try:
        chunks = rerank_results(
            query=state["search_query"],
            candidates=state.get("retrieved_chunks", []),
            top_n=DEFAULT_TOP_N,
        )
    except (ValueError, RuntimeError) as exc:
        raise RuntimeError(f"Reranker system error: {exc}") from exc
    summary = [
        {
            "rerank_score": chunk.get("rerank_score"),
            "vector_score": chunk.get("vector_score"),
            "source": chunk.get("source"),
            "section": chunk.get("section"),
        }
        for chunk in chunks
    ]
    return node_update(
        state,
        "reranker",
        {"count": len(chunks), "candidates": summary},
        reranked_chunks=chunks,
    )
