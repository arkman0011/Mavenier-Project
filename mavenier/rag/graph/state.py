"""Shared state passed between the query workflow's nodes."""

from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict


class RAGState(TypedDict, total=False):
    # Input
    question: str
    qdrant_path: str
    requested_filters: dict[str, Any]
    debug: bool
    gemini_available: bool

    # query_analysis
    intent: str
    keywords: list[str]
    search_query: str
    filters: dict[str, Any]
    query_analysis_mode: str

    # retriever
    retrieved_chunks: list[dict[str, Any]]
    filters_used: dict[str, Any]
    filters_relaxed: bool

    # reranker
    reranked_chunks: list[dict[str, Any]]
    top_rerank_score: float | None
    retrieval_confident: bool

    # context_expander (small-to-big)
    context: str
    context_sources: list[dict[str, Any]]
    expanded_chunks: list[dict[str, Any]]

    # answer_generator
    draft_answer: str
    answer_mode: str

    # answer_verifier
    verification_verdict: str
    addresses_question: bool
    verification_issues: list[str]
    verification_mode: str

    # finalizer
    final_answer: str
    confidence: float
    sources: list[dict[str, str | None]]

    # trace for debugging
    trace: list[dict[str, Any]]
