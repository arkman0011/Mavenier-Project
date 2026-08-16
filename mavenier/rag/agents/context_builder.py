"""Node 6: deterministically format numbered, injection-safe context."""

from __future__ import annotations

from mavenier.rag.agents.common import node_update
from mavenier.rag.generation.llm import build_rag_prompt
from mavenier.rag.graph.state import RAGState


def context_builder_node(state: RAGState) -> dict:
    chunks = [
        chunk
        for chunk in state.get("reranked_chunks", [])
        if isinstance(chunk.get("text"), str) and chunk["text"].strip()
    ]
    context = build_rag_prompt(state["question"], chunks)
    return node_update(
        state,
        "context_builder",
        {"context_count": len(chunks)},
        context=context,
        reranked_chunks=chunks,
    )
