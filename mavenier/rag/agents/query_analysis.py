"""Stage 1: turn the question into a search query plus metadata filters.

This single agent replaces the old query_understanding + search_planner pair.
It is the "metadata brain": it decides which reliable filters (release, series,
spec, timer, asn1) can safely narrow retrieval, and leaves the rest to
semantic search.
"""

from __future__ import annotations

import json
import re

from mavenier.rag.agents.common import node_update
from mavenier.rag.agents.prompts import QUERY_ANALYSIS_PROMPT
from mavenier.rag.agents.schemas import QueryAnalysis
from mavenier.rag.generation.llm import GeminiRateLimitError, generate_structured
from mavenier.rag.graph.state import RAGState


def build_filters(analysis: QueryAnalysis, requested: dict | None) -> dict:
    """Map the analysis fields onto the vector store's filter alias keys.

    Caller-supplied ``requested`` filters always win; the model only adds a
    filter when it is confident enough to have filled the field.
    """
    filters: dict[str, str] = {}
    if analysis.release:
        filters["release"] = analysis.release.strip()
    if analysis.series:
        filters["series"] = analysis.series.strip()
    if analysis.spec_number:
        filters["spec_number"] = analysis.spec_number.strip()
    if analysis.timer and re.fullmatch(r"T\d{3,4}", analysis.timer.strip(), re.IGNORECASE):
        filters["timer.timer_name"] = analysis.timer.strip().upper()
    if analysis.intent == "asn1_lookup" and analysis.asn1_entity:
        filters["asn1.message_name"] = analysis.asn1_entity.strip()

    # Anything the API caller asked for takes precedence over the inference.
    filters.update(requested or {})
    return filters


def analyze_query_locally(question: str) -> QueryAnalysis:
    """Extract conservative query hints when Gemini quota is unavailable."""
    timer_match = re.search(r"\bT\d{3,4}\b", question, re.IGNORECASE)
    release_match = re.search(r"\bRel(?:ease)?[- ]?(\d{1,2})\b", question, re.IGNORECASE)
    spec_match = re.search(
        r"\b(?:3GPP\s+)?TS\s*(\d{2})[. -]?(\d{2,3})\b",
        question,
        re.IGNORECASE,
    )
    state_match = re.search(r"\bRRC_(?:IDLE|INACTIVE|CONNECTED)\b", question, re.IGNORECASE)
    lowered = question.casefold()
    if timer_match:
        intent = "timer_behavior"
    elif state_match:
        intent = "state_transition"
    elif lowered.startswith(("what is ", "what are ", "define ")):
        intent = "definition"
    elif any(word in lowered for word in ("compare", "difference between", "versus", " vs ")):
        intent = "comparison"
    else:
        intent = "general_technical_question"

    keywords = []
    explicit_terms = re.findall(r"\b[A-Z][A-Z0-9_-]{1,}\b", question)
    if timer_match:
        explicit_terms.append(timer_match.group(0).upper())
    if state_match:
        explicit_terms.append(state_match.group(0).upper())
    for value in explicit_terms:
        if value.casefold() not in {item.casefold() for item in keywords}:
            keywords.append(value)

    return QueryAnalysis(
        search_query=question,
        intent=intent,
        keywords=keywords,
        release=f"Rel-{release_match.group(1)}" if release_match else None,
        series=spec_match.group(1) if spec_match else None,
        spec_number="".join(spec_match.groups()) if spec_match else None,
        timer=timer_match.group(0).upper() if timer_match else None,
    )

def query_analysis_node(state: RAGState) -> dict:
    question = state["question"].strip()
    gemini_available = state.get("gemini_available", True)
    mode = "gemini"
    if gemini_available:
        try:
            analysis = generate_structured(
                prompt="Analyze this question:\n" + json.dumps(question, ensure_ascii=False),
                system_prompt=QUERY_ANALYSIS_PROMPT,
                response_model=QueryAnalysis,
            )
        except GeminiRateLimitError:
            gemini_available = False
            mode = "local_quota_fallback"
            analysis = analyze_query_locally(question)
    else:
        mode = "local_quota_fallback"
        analysis = analyze_query_locally(question)

    search_query = analysis.search_query.strip() or question
    filters = build_filters(analysis, state.get("requested_filters"))
    return node_update(
        state,
        "query_analysis",
        {
            "intent": analysis.intent,
            "search_query": search_query,
            "filters": filters,
            "keywords": analysis.keywords,
            "mode": mode,
        },
        intent=analysis.intent,
        search_query=search_query,
        filters=filters,
        keywords=analysis.keywords,
        gemini_available=gemini_available,
        query_analysis_mode=mode,
    )
