"""Node 8: verify each draft claim against the same retrieved evidence."""

from __future__ import annotations

from mavenier.rag.agents.common import node_update
from mavenier.rag.agents.prompts import FACT_VERIFIER_PROMPT
from mavenier.rag.agents.schemas import VerificationResult
from mavenier.rag.generation.llm import generate_structured
from mavenier.rag.graph.state import RAGState


def fact_verifier_node(state: RAGState) -> dict:
    prompt = "\n\n".join(
        (
            "QUESTION:\n" + state["question"],
            "DRAFT ANSWER:\n" + state["draft_answer"],
            "EVIDENCE:\n" + state["context"],
        )
    )
    result = generate_structured(
        prompt=prompt,
        system_prompt=FACT_VERIFIER_PROMPT,
        response_model=VerificationResult,
    )
    unsupported = list(result.unsupported_claims)
    unsupported.extend(
        claim.claim
        for claim in result.claims
        if not claim.supported and claim.claim not in unsupported
    )
    if not result.claims:
        unsupported.append("The verifier returned no claim-level support.")
    status = "UNSUPPORTED" if unsupported else result.status
    return node_update(
        state,
        "fact_verifier",
        {"status": status, "unsupported_claims": unsupported},
        verification_status=status,
        verified_claims=[claim.model_dump() for claim in result.claims],
        unsupported_claims=unsupported,
    )
