"""Beginner-friendly shared state for the complete query workflow."""

from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict


class RAGState(TypedDict, total=False):
    question: str
    intent: str
    entities: dict[str, str]
    keywords: list[str]
    requested_filters: dict[str, Any]
    filters: dict[str, Any]
    search_query: str
    qdrant_path: str
    retrieved_chunks: list[dict[str, Any]]
    reranked_chunks: list[dict[str, Any]]
    evidence_status: str
    evidence_reason: str
    missing_information: list[str]
    retry_count: int
    max_retries: int
    context: str
    draft_answer: str
    verification_status: str
    verified_claims: list[dict[str, Any]]
    unsupported_claims: list[str]
    answer_retry_count: int
    max_answer_retries: int
    final_answer: str
    confidence: float
    sources: list[dict[str, str | None]]
    debug: bool
    trace: list[dict[str, Any]]
