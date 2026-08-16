"""Node 2: build a conservative semantic query and optional metadata filters."""

from __future__ import annotations

import re
from typing import Any

from mavenier.rag.agents.common import node_update
from mavenier.rag.graph.state import RAGState


def _append_unique(parts: list[str], value: Any) -> None:
    if not isinstance(value, str) or not value.strip():
        return
    cleaned = value.strip()
    if cleaned.casefold() not in {part.casefold() for part in parts}:
        parts.append(cleaned)


def build_search_plan(state: RAGState) -> tuple[str, dict[str, Any]]:
    """Map only high-confidence entities to fields in the actual Qdrant schema."""
    parts = [state["question"].strip()]
    for keyword in state.get("keywords", []):
        _append_unique(parts, keyword)
    for value in state.get("entities", {}).values():
        _append_unique(parts, value)

    filters = dict(state.get("requested_filters") or {})
    entities = state.get("entities", {})
    timer = entities.get("timer")
    if isinstance(timer, str) and re.fullmatch(
        r"T\d{3,4}", timer.strip(), re.IGNORECASE
    ):
        filters.setdefault("timer.timer_name", timer.strip().upper())

    asn1_entity = entities.get("asn1_entity")
    if (
        state.get("intent") == "asn1_lookup"
        and isinstance(asn1_entity, str)
        and asn1_entity.strip()
    ):
        filters.setdefault("asn1.message_name", asn1_entity.strip())
    return " ".join(parts), filters


def search_planner_node(state: RAGState) -> dict:
    search_query, filters = build_search_plan(state)
    return node_update(
        state,
        "search_planner",
        {"query": search_query, "filters": filters},
        search_query=search_query,
        filters=filters,
    )
