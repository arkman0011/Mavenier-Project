"""Node 9: deterministic answer, sources, confidence, and refusal handling."""

from __future__ import annotations

from typing import Any

from mavenier.rag.agents.common import node_update
from mavenier.rag.graph.state import RAGState

INSUFFICIENT_ANSWER = "The retrieved documents do not contain enough reliable evidence to answer this question."
UNVERIFIED_ANSWER = "A draft answer was generated, but it could not be fully verified against the retrieved documents."


def _sources(
    claims: list[dict[str, Any]],
    chunks: list[dict[str, Any]],
) -> list[dict[str, str | None]]:
    allowed = {
        (
            str(chunk["source"]),
            str(chunk["section"]) if chunk.get("section") is not None else None,
        )
        for chunk in chunks
        if chunk.get("source")
    }
    sources = []
    seen = set()
    for claim in claims:
        if not claim.get("supported"):
            continue
        source = claim.get("source")
        section = claim.get("section")
        if not source:
            continue
        key = (str(source), str(section) if section is not None else None)
        if key in allowed and key not in seen:
            seen.add(key)
            sources.append({"source": key[0], "section": key[1]})
    return sources


def _verified_confidence(state: RAGState, sources: list[dict]) -> float:
    """Transparent score: 0.90 verified, plus source diversity up to 0.95."""
    if state.get("evidence_status") != "SUFFICIENT":
        return 0.0
    if state.get("verification_status") != "SUPPORTED":
        return 0.4
    return min(0.95, 0.90 + 0.02 * max(0, len(sources) - 1))


def finalizer_node(state: RAGState) -> dict:
    supported = state.get("verification_status") == "SUPPORTED"
    sources = (
        _sources(
            state.get("verified_claims", []),
            state.get("reranked_chunks", []),
        )
        if supported
        else []
    )
    answer = state.get("draft_answer", "") if supported else UNVERIFIED_ANSWER
    confidence = _verified_confidence(state, sources)
    return node_update(
        state,
        "finalizer",
        {"confidence": confidence, "source_count": len(sources)},
        final_answer=answer,
        confidence=confidence,
        sources=sources,
    )


def insufficient_answer_node(state: RAGState) -> dict:
    reason = state.get("evidence_reason", "").strip()
    answer = INSUFFICIENT_ANSWER
    if reason:
        answer += f" Reason: {reason}"
    return node_update(
        state,
        "insufficient_answer",
        {"confidence": 0.0, "reason": reason},
        final_answer=answer,
        confidence=0.0,
        sources=[],
    )


def safe_finalizer_node(state: RAGState) -> dict:
    """Never expose a draft that still contains unsupported claims."""
    return node_update(
        state,
        "safe_finalizer",
        {"confidence": 0.4, "unsupported_claims": state.get("unsupported_claims", [])},
        final_answer=UNVERIFIED_ANSWER,
        confidence=0.4,
        sources=[],
    )
