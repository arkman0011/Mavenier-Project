"""Retry node: broaden only with terms already present in the question analysis."""

from __future__ import annotations

from mavenier.rag.agents.common import node_update
from mavenier.rag.graph.state import RAGState

INTENT_HINTS = {
    "definition": "definition",
    "procedure_explanation": "procedure actions conditions",
    "timer_behavior": "timer expiry action procedure",
    "state_transition": "state transition condition action",
    "message_lookup": "message behavior procedure",
    "asn1_lookup": "ASN.1 definition fields",
    "requirement_lookup": "normative requirement condition action",
    "specification_lookup": "specification section",
    "comparison": "technical comparison",
}


def _unique_terms(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result = []
    for value in values:
        cleaned = value.strip()
        if cleaned and cleaned.casefold() not in seen:
            seen.add(cleaned.casefold())
            result.append(cleaned)
    return result


def query_refinement_node(state: RAGState) -> dict:
    retry_count = state.get("retry_count", 0) + 1
    terms = [
        state["question"],
        *state.get("keywords", []),
        *state.get("entities", {}).values(),
    ]
    if retry_count > 1:
        terms.append(INTENT_HINTS.get(state.get("intent", ""), "technical procedure"))
    search_query = " ".join(_unique_terms(terms))

    # The first retry relaxes metadata because older indexed records may not
    # contain the expected field even when their passage text is relevant.
    filters = dict(state.get("requested_filters") or {})
    return node_update(
        state,
        "query_refinement",
        {"retry_count": retry_count, "query": search_query, "filters": filters},
        retry_count=retry_count,
        search_query=search_query,
        filters=filters,
    )
