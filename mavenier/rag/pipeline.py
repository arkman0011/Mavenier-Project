"""Public query-time entry point for the LangGraph agentic RAG workflow."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from mavenier.rag.graph.agentic_rag_graph import graph
from mavenier.rag.retrieval.vector_store import DEFAULT_QDRANT_PATH

MAX_RETRIEVAL_RETRIES = 2
MAX_ANSWER_RETRIES = 1


def ask_agentic_rag(
    question: str,
    qdrant_path: str | Path = DEFAULT_QDRANT_PATH,
    filters: dict[str, Any] | None = None,
    debug: bool = False,
) -> dict[str, Any]:
    """Run the bounded graph and return only useful public result fields."""
    if not isinstance(question, str) or not question.strip():
        raise ValueError("Question cannot be empty.")

    initial_state = {
        "question": question.strip(),
        "requested_filters": dict(filters or {}),
        "qdrant_path": str(Path(qdrant_path).expanduser().resolve()),
        "retry_count": 0,
        "max_retries": MAX_RETRIEVAL_RETRIES,
        "answer_retry_count": 0,
        "max_answer_retries": MAX_ANSWER_RETRIES,
        "debug": debug,
        "trace": [],
    }
    result = graph.invoke(initial_state, config={"recursion_limit": 25})
    public = {
        "answer": result["final_answer"],
        "confidence": float(result["confidence"]),
        "sources": result.get("sources", []),
    }
    if debug:
        public["debug"] = {
            "intent": result.get("intent"),
            "entities": result.get("entities", {}),
            "keywords": result.get("keywords", []),
            "search_query": result.get("search_query"),
            "filters": result.get("filters", {}),
            "evidence_status": result.get("evidence_status"),
            "retry_count": result.get("retry_count", 0),
            "verification_status": result.get("verification_status"),
            "unsupported_claims": result.get("unsupported_claims", []),
            "trace": result.get("trace", []),
        }
    return public
