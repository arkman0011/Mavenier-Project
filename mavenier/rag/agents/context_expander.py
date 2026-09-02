"""Stage 4 (small-to-big): expand the winning chunks to their full sections.

Retrieval and reranking work on small chunks for precision. Before answering,
we re-hydrate each winner to its whole parent section so the answer model sees
complete context, not a fragment. Winners from the same section collapse into
one block, so three small chunks often become one or two sections.
"""

from __future__ import annotations

from typing import Any

from mavenier.rag.agents.common import node_update
from mavenier.rag.generation.llm import build_rag_prompt
from mavenier.rag.graph.state import RAGState
from mavenier.rag.retrieval.pipeline import fetch_section_text


def _document_metadata(chunk: dict[str, Any]) -> dict[str, Any]:
    return (chunk.get("payload") or {}).get("document_metadata") or {}


def _chunk_id(chunk: dict[str, Any]) -> str | None:
    return chunk.get("chunk_id") or (chunk.get("payload") or {}).get("chunk_id")


def expand_chunks(chunks: list[dict[str, Any]], qdrant_path: str) -> list[dict[str, Any]]:
    """Return one context block per unique (document, section), full text."""
    expanded: list[dict[str, Any]] = []
    seen: set[tuple[str | None, str | None]] = set()
    for chunk in chunks:
        document = _document_metadata(chunk)
        document_id = document.get("document_id")
        section = chunk.get("section")
        key = (document_id, section)
        if key in seen:
            continue
        seen.add(key)

        text = ""
        if document_id and section:
            text = fetch_section_text(
                document_id,
                section,
                qdrant_path,
                center_chunk_id=_chunk_id(chunk),
            )
        if not text.strip():
            text = str(chunk.get("text") or "").strip()
        if not text:
            continue
        expanded.append(
            {
                "text": text,
                "source": chunk.get("source"),
                "section": section,
                "release": document.get("release"),
                "series": document.get("series"),
                "spec_number": document.get("spec_number"),
                "rerank_score": chunk.get("rerank_score"),
                "vector_score": chunk.get("vector_score"),
                "metadata": chunk.get("metadata"),
            }
        )
    return expanded


def context_expander_node(state: RAGState) -> dict:
    reranked = state.get("reranked_chunks", [])
    expanded = expand_chunks(reranked, state["qdrant_path"])
    context = build_rag_prompt(state["question"], expanded) if expanded else ""
    return node_update(
        state,
        "context_expander",
        {"section_count": len(expanded)},
        context=context,
        context_sources=[
            {"source": item.get("source"), "section": item.get("section")}
            for item in expanded
        ],
        expanded_chunks=expanded,
    )
