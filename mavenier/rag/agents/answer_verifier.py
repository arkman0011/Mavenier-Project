"""Stage 6 (LLM): verify the draft answer against the used chunks + metadata.

Unlike a plain text verifier, this one receives each chunk's structured
metadata (timers, states, messages, ASN.1, requirements) plus its spec
identity, so it can corroborate specific facts rather than guess from prose.
"""

from __future__ import annotations

import json
from typing import Any

from mavenier.rag.agents.common import node_update
from mavenier.rag.agents.prompts import ANSWER_VERIFIER_PROMPT
from mavenier.rag.agents.schemas import AnswerVerification
from mavenier.rag.generation.llm import GeminiRateLimitError, generate_structured
from mavenier.rag.graph.state import RAGState

METADATA_BLOCKS = (
    "direction_metadata",
    "state_metadata",
    "timer_metadata",
    "asn1_metadata",
    "requirement_metadata",
)


def _evidence(chunks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Compact per-chunk record: identity, populated metadata, and text."""
    evidence = []
    for chunk in chunks:
        blocks = chunk.get("metadata") or {}
        populated = {
            name: blocks[name]
            for name in METADATA_BLOCKS
            if isinstance(blocks.get(name), dict) and blocks[name].get("items")
        }
        evidence.append(
            {
                "source": chunk.get("source"),
                "section": chunk.get("section"),
                "release": chunk.get("release"),
                "series": chunk.get("series"),
                "spec_number": chunk.get("spec_number"),
                "metadata": populated,
                "text": chunk.get("text"),
            }
        )
    return evidence


def answer_verifier_node(state: RAGState) -> dict:
    fallback_issue = "Gemini quota unavailable; independent LLM verification was skipped."
    if state.get("answer_mode") == "extractive_quota_fallback":
        return node_update(
            state,
            "answer_verifier",
            {
                "verdict": "partially_supported",
                "addresses_question": False,
                "issues": [fallback_issue],
                "mode": "deterministic_quota_fallback",
            },
            verification_verdict="partially_supported",
            addresses_question=False,
            verification_issues=[fallback_issue],
            verification_mode="deterministic_quota_fallback",
        )

    payload = {
        "user_question": state["question"],
        "draft_answer": state.get("draft_answer", ""),
        "evidence": _evidence(state.get("expanded_chunks", [])),
    }
    try:
        result = generate_structured(
            prompt="Verify this answer:\n" + json.dumps(payload, ensure_ascii=False),
            system_prompt=ANSWER_VERIFIER_PROMPT,
            response_model=AnswerVerification,
        )
        mode = "gemini"
    except GeminiRateLimitError:
        return node_update(
            state,
            "answer_verifier",
            {
                "verdict": "partially_supported",
                "addresses_question": True,
                "issues": [fallback_issue],
                "mode": "deterministic_quota_fallback",
            },
            verification_verdict="partially_supported",
            addresses_question=True,
            verification_issues=[fallback_issue],
            verification_mode="deterministic_quota_fallback",
            gemini_available=False,
        )
    return node_update(
        state,
        "answer_verifier",
        {
            "verdict": result.verdict,
            "addresses_question": result.addresses_question,
            "issues": result.issues,
            "mode": mode,
        },
        verification_verdict=result.verdict,
        addresses_question=result.addresses_question,
        verification_issues=result.issues,
        verification_mode=mode,
    )
