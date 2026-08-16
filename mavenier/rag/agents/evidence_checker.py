"""Node 5: decide whether reranked passages cover the whole question."""

from __future__ import annotations

from mavenier.rag.agents.common import node_update
from mavenier.rag.agents.prompts import EVIDENCE_CHECKER_PROMPT
from mavenier.rag.agents.schemas import EvidenceCheckResult
from mavenier.rag.generation.llm import build_rag_prompt, generate_structured
from mavenier.rag.graph.state import RAGState


def evidence_checker_node(state: RAGState) -> dict:
    chunks = state.get("reranked_chunks", [])
    if not chunks:
        result = EvidenceCheckResult(
            status="INSUFFICIENT",
            reason="No retrieved passages were available.",
            missing_information=["relevant document evidence"],
        )
    else:
        result = generate_structured(
            prompt=build_rag_prompt(state["question"], chunks),
            system_prompt=EVIDENCE_CHECKER_PROMPT,
            response_model=EvidenceCheckResult,
        )
    return node_update(
        state,
        "evidence_checker",
        {
            "status": result.status,
            "reason": result.reason,
            "missing_information": result.missing_information,
        },
        evidence_status=result.status,
        evidence_reason=result.reason,
        missing_information=result.missing_information,
    )
