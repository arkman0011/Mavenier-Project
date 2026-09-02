"""Stage 2: BGE + local Qdrant retrieval with soft, self-relaxing filters.

Filters make retrieval precise, but a wrong inferred filter can return nothing.
So we try the full filter set first and, only if it comes back empty, relax to
the caller's filters and then to no filter at all. This keeps recall without
losing precision when the filters are right.
"""

from __future__ import annotations

from mavenier.rag.agents.common import node_update
from mavenier.rag.graph.state import RAGState
from mavenier.rag.retrieval.pipeline import search_text

CANDIDATE_TOP_K = 10


def _filter_attempts(state: RAGState) -> list[dict]:
    """Ordered, de-duplicated filter sets from most to least specific."""
    attempts = [state.get("filters") or {}, state.get("requested_filters") or {}, {}]
    seen: list[dict] = []
    for attempt in attempts:
        if attempt not in seen:
            seen.append(attempt)
    return seen


def retriever_node(state: RAGState) -> dict:
    chunks: list = []
    used_filters: dict = {}
    for used_filters in _filter_attempts(state):
        try:
            chunks = search_text(
                query=state["search_query"],
                qdrant_path=state["qdrant_path"],
                limit=CANDIDATE_TOP_K,
                filters=used_filters or None,
            )
        except (ValueError, RuntimeError) as exc:
            raise RuntimeError(f"Retrieval system error: {exc}") from exc
        if chunks:
            break

    relaxed = used_filters != (state.get("filters") or {})
    summary = [
        {"score": chunk.get("score"), "source": chunk.get("source"), "section": chunk.get("section")}
        for chunk in chunks
    ]
    return node_update(
        state,
        "retriever",
        {"count": len(chunks), "filters_used": used_filters, "relaxed": relaxed, "candidates": summary},
        retrieved_chunks=chunks,
        filters_used=used_filters,
        filters_relaxed=relaxed,
    )
