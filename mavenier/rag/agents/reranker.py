"""Stage 3: cross-encoder rerank, plus a deterministic confidence gate.

The reranker's top score is our best cheap signal for "did we actually retrieve
anything relevant." If the best passage scores below RELEVANCE_FLOOR, we mark
retrieval as not confident so the graph abstains instead of answering from weak
matches. This value is specific to the ms-marco cross-encoder (logits, roughly
-11..+11; > 0 means "more relevant than not") and is meant to be tuned.
"""

from __future__ import annotations

from mavenier.rag.agents.common import node_update
from mavenier.rag.graph.state import RAGState
from mavenier.rag.retrieval.reranker import DEFAULT_TOP_N, rerank_results

RELEVANCE_FLOOR = 0.0


def reranker_node(state: RAGState) -> dict:
    try:
        chunks = rerank_results(
            query=state["search_query"],
            candidates=state.get("retrieved_chunks", []),
            top_n=DEFAULT_TOP_N,
        )
    except (ValueError, RuntimeError) as exc:
        raise RuntimeError(f"Reranker system error: {exc}") from exc

    top_score = float(chunks[0]["rerank_score"]) if chunks else None
    confident = bool(chunks) and top_score is not None and top_score >= RELEVANCE_FLOOR
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
        {"count": len(chunks), "top_score": top_score, "confident": confident, "candidates": summary},
        reranked_chunks=chunks,
        top_rerank_score=top_score,
        retrieval_confident=confident,
    )
