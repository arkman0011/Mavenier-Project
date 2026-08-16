"""Small helpers shared by agentic query nodes."""

from __future__ import annotations

from typing import Any


def node_update(
    state: dict[str, Any],
    stage: str,
    details: dict[str, Any],
    **updates: Any,
) -> dict[str, Any]:
    """Return state updates plus a safe, user-visible stage trace entry."""
    updates["trace"] = [
        *state.get("trace", []),
        {"stage": stage, **details},
    ]
    return updates
