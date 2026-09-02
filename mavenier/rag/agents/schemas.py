"""Structured Gemini outputs for the two judgment nodes."""

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


class QueryAnalysis(BaseModel):
    """One structured read of the user's question.

    Produces the semantic search query AND any metadata filters that are
    *explicitly* present in the question. Filters left as None are simply not
    applied, so a vague question searches the whole corpus rather than being
    wrongly narrowed.
    """

    search_query: str
    intent: Intent = "general_technical_question"
    keywords: list[str] = Field(default_factory=list)

    # Metadata filters — only fill these when the question states them outright.
    release: str | None = None          # e.g. "Rel-16"
    series: str | None = None           # e.g. "38"
    spec_number: str | None = None      # e.g. "38331"
    timer: str | None = None            # e.g. "T300"
    asn1_entity: str | None = None      # e.g. "RRCReconfiguration"


class AnswerVerification(BaseModel):
    """Whether the draft answer is supported by the chunks (text + metadata).

    The verifier sees the user question, the answer, and every used chunk's
    text plus its structured metadata, so it can corroborate specific facts
    (timers, states, messages, release/series) rather than guess from prose.
    """

    verdict: Literal["supported", "partially_supported", "unsupported"]
    addresses_question: bool = True
    issues: list[str] = Field(default_factory=list)
