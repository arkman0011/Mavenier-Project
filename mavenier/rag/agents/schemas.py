"""Structured Gemini outputs for semantic decision nodes."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

Intent = Literal[
    "definition",
    "procedure_explanation",
    "timer_behavior",
    "state_transition",
    "message_lookup",
    "asn1_lookup",
    "requirement_lookup",
    "specification_lookup",
    "comparison",
    "general_technical_question",
]


class QueryUnderstandingResult(BaseModel):
    """Only information explicitly stated in the question."""

    intent: Intent = "general_technical_question"
    entities: dict[str, str] = Field(default_factory=dict)
    keywords: list[str] = Field(default_factory=list)


class EvidenceCheckResult(BaseModel):
    """Whether every meaningful question part is covered by evidence."""

    status: Literal["SUFFICIENT", "INSUFFICIENT"]
    reason: str
    missing_information: list[str] = Field(default_factory=list)


class VerifiedClaim(BaseModel):
    """One factual answer claim and its evidence result."""

    claim: str
    supported: bool
    source: str | None = None
    section: str | None = None


class VerificationResult(BaseModel):
    """Claim-level verification against the supplied context only."""

    status: Literal["SUPPORTED", "UNSUPPORTED"]
    claims: list[VerifiedClaim] = Field(default_factory=list)
    unsupported_claims: list[str] = Field(default_factory=list)
