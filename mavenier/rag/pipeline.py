"""Public query-time entry point for the linear agentic RAG workflow."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from mavenier.rag.graph.agentic_rag_graph import graph
from mavenier.rag.retrieval.vector_store import DEFAULT_QDRANT_PATH


def ask_agentic_rag(
    question: str,
    qdrant_path: str | Path = DEFAULT_QDRANT_PATH,
    filters: dict[str, Any] | None = None,
    debug: bool = False,
) -> dict[str, Any]:
    """Run the linear graph and return only the useful public result fields."""
    if not isinstance(question, str) or not question.strip():
        raise ValueError("Question cannot be empty.")

    initial_state = {
        "question": question.strip(),
        "requested_filters": dict(filters or {}),
        "qdrant_path": str(Path(qdrant_path).expanduser().resolve()),
        "debug": debug,
        "trace": [],
    }
    result = graph.invoke(initial_state)
    public = {
        "answer": result["final_answer"],
        "confidence": float(result["confidence"]),
        "sources": result.get("sources", []),
    }
    if debug:
        public["debug"] = {
            "intent": result.get("intent"),
            "keywords": result.get("keywords", []),
            "search_query": result.get("search_query"),
            "filters": result.get("filters", {}),
            "filters_used": result.get("filters_used", {}),
            "filters_relaxed": result.get("filters_relaxed", False),
            "top_rerank_score": result.get("top_rerank_score"),
            "retrieval_confident": result.get("retrieval_confident"),
            "verification_verdict": result.get("verification_verdict"),
            "verification_issues": result.get("verification_issues", []),
            "gemini_available": result.get("gemini_available", True),
            "query_analysis_mode": result.get("query_analysis_mode", "gemini"),
            "answer_mode": result.get("answer_mode", "gemini"),
            "verification_mode": result.get("verification_mode", "gemini"),
            "trace": result.get("trace", []),
        }
    return public
