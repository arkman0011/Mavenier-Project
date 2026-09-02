"""Stage 5a: draft a grounded answer from the expanded section context."""

from __future__ import annotations

from mavenier.rag.agents.common import node_update
from typing import Any

from mavenier.rag.generation.llm import GeminiRateLimitError, generate_answer
from mavenier.rag.graph.state import RAGState


MAX_EXCERPT_CHARACTERS = 700


def build_extractive_answer(chunks: list[dict[str, Any]]) -> str:
    """Return source text directly when no generative quota is available."""
    if not chunks:
        return "No relevant context was retrieved from the knowledge base."

    lines = [
        "Gemini quota is unavailable, so the most relevant retrieved evidence is shown directly:",
    ]
    for rank, chunk in enumerate(chunks[:3], start=1):
        text = " ".join(str(chunk.get("text") or "").split())
        if len(text) > MAX_EXCERPT_CHARACTERS:
            text = text[:MAX_EXCERPT_CHARACTERS].rsplit(" ", 1)[0] + "…"
        source = str(chunk.get("source") or "Unknown source")
        section = chunk.get("section")
        label = f"[{rank}] {source}"
        if section:
            label += f", section {section}"
        lines.extend(("", label, text))
    return "\n".join(lines)


def answer_generator_node(state: RAGState) -> dict:
    chunks = state.get("expanded_chunks", [])
    gemini_available = state.get("gemini_available", True)
    mode = "gemini"
    if gemini_available:
        try:
            answer = generate_answer(state["question"], chunks)
        except GeminiRateLimitError:
            gemini_available = False
            mode = "extractive_quota_fallback"
            answer = build_extractive_answer(chunks)
    else:
        mode = "extractive_quota_fallback"
        answer = build_extractive_answer(chunks)
    return node_update(
        state,
        "answer_generator",
        {"draft_created": bool(answer), "mode": mode},
        draft_answer=answer,
        answer_mode=mode,
        gemini_available=gemini_available,
    )
