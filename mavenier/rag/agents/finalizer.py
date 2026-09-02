"""Stage 7: deterministic finalizer — answer with cited sections, or refuse.

Confidence reflects how the answer got here:

- retrieval not confident (abstain gate) or nothing to cite -> refuse   (0.00)
- answer_verifier says "unsupported"                        -> refuse   (0.30)
- "partially_supported" or doesn't address the question      -> answer, capped (<=0.55)
- "supported" and addresses the question                      -> answer, high (0.90-0.95)
"""

from __future__ import annotations

from typing import Any

from mavenier.rag.agents.common import node_update
from mavenier.rag.graph.state import RAGState

INSUFFICIENT_ANSWER = "The retrieved documents do not contain enough reliable evidence to answer this question."
UNSUPPORTED_ANSWER = "A draft answer was generated, but it could not be verified against the retrieved documents."
GENERATOR_ABSTENTION_MARKERS = (
    "retrieved context does not contain enough information",
    "not enough information in the retrieved context",
    "insufficient information in the retrieved context",
)


def _unique_sources(context_sources: list[dict[str, Any]]) -> list[dict[str, str | None]]:
    """The sections shown to the model, de-duplicated, in order."""
    sources: list[dict[str, str | None]] = []
    seen: set[tuple[str, str | None]] = set()
    for item in context_sources:
        source = item.get("source")
        if not source:
            continue
        section = item.get("section")
        key = (str(source), str(section) if section is not None else None)
        if key not in seen:
            seen.add(key)
            sources.append({"source": key[0], "section": key[1]})
    return sources


def _generator_abstained(draft_answer: str) -> bool:
    """Recognize the answer model's required insufficient-context response."""
    normalized = " ".join(str(draft_answer or "").casefold().split())
    return any(marker in normalized for marker in GENERATOR_ABSTENTION_MARKERS)


def finalizer_node(state: RAGState) -> dict:
    sources = _unique_sources(state.get("context_sources", []))
    draft_answer = state.get("draft_answer", "")

    # Reached from the abstain gate, expansion produced nothing to cite, or the
    # answer model explicitly determined that the context was insufficient.
    # The latter must remain a refusal even if an LLM verifier misclassifies the
    # abstention sentence itself as a supported claim.
    if (
        not state.get("retrieval_confident")
        or not sources
        or _generator_abstained(draft_answer)
    ):
        return node_update(
            state,
            "finalizer",
            {"outcome": "insufficient", "confidence": 0.0},
            final_answer=INSUFFICIENT_ANSWER,
            confidence=0.0,
            sources=[],
        )

    verdict = state.get("verification_verdict")
    addresses_question = state.get("addresses_question", True)

    if verdict == "unsupported":
        return node_update(
            state,
            "finalizer",
            {"outcome": "unsupported", "confidence": 0.3, "issues": state.get("verification_issues", [])},
            final_answer=UNSUPPORTED_ANSWER,
            confidence=0.3,
            sources=[],
        )

    if verdict == "partially_supported" or not addresses_question:
        confidence = min(0.55, 0.40 + 0.05 * len(sources))
        return node_update(
            state,
            "finalizer",
            {"outcome": "partial", "confidence": confidence, "issues": state.get("verification_issues", [])},
            final_answer=draft_answer,
            confidence=confidence,
            sources=sources,
        )

    # Fully verified: supported, and it addresses the question.
    confidence = min(0.95, 0.90 + 0.02 * max(0, len(sources) - 1))
    return node_update(
        state,
        "finalizer",
        {"outcome": "answered", "confidence": confidence, "source_count": len(sources)},
        final_answer=draft_answer,
        confidence=confidence,
        sources=sources,
    )
