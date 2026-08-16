"""Short conditional routes that make retry policy visible in LangGraph."""

from __future__ import annotations

from mavenier.rag.graph.state import RAGState


def route_after_evidence(state: RAGState) -> str:
    if state.get("evidence_status") == "SUFFICIENT":
        return "sufficient"
    if state.get("retry_count", 0) < state.get("max_retries", 2):
        return "retry"
    return "insufficient"


def route_after_verification(state: RAGState) -> str:
    if state.get("verification_status") == "SUPPORTED":
        return "supported"
    if state.get("answer_retry_count", 0) < state.get("max_answer_retries", 1):
        return "regenerate"
    return "safe_finalize"
