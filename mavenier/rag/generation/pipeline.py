"""Query-time orchestration: existing retrieval -> reranker -> Gemini."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from mavenier.rag.generation.llm import generate_answer
from mavenier.rag.retrieval.pipeline import search_text
from mavenier.rag.retrieval.reranker import DEFAULT_TOP_N, rerank_results
from mavenier.rag.retrieval.vector_store import DEFAULT_QDRANT_PATH

CANDIDATE_TOP_K = 10
FINAL_TOP_N = DEFAULT_TOP_N


def _display_source(result: dict[str, Any]) -> str:
    return str(result.get("source") or "Not provided")


def _display_section(result: dict[str, Any]) -> str:
    return str(result.get("section") or "Not provided")


def print_qdrant_debug(candidates: list[dict[str, Any]]) -> None:
    """Show retrieval ordering without printing embeddings or full passages."""
    print("\nQDRANT RESULTS")
    if not candidates:
        print("No candidates returned.")
        return
    for rank, candidate in enumerate(candidates, start=1):
        print(
            f"{rank}. vector_score={float(candidate.get('score', 0.0)):.6f} | "
            f"source={_display_source(candidate)} | "
            f"section={_display_section(candidate)}"
        )


def print_reranker_debug(results: list[dict[str, Any]]) -> None:
    """Show the new ordering while retaining the original vector scores."""
    print("\nRERANKED RESULTS")
    if not results:
        print("No candidates available for reranking.")
        return
    for rank, result in enumerate(results, start=1):
        print(
            f"{rank}. rerank_score={float(result['rerank_score']):.6f} | "
            f"vector_score={float(result['vector_score']):.6f} | "
            f"source={_display_source(result)} | "
            f"section={_display_section(result)}"
        )


def ask_rag(
    query: str,
    qdrant_path: str | Path = DEFAULT_QDRANT_PATH,
    filters: dict[str, Any] | None = None,
    debug: bool = False,
) -> str:
    """Answer one question using the existing collection and new final stages."""
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Question cannot be empty.")

    candidates = search_text(
        query=query.strip(),
        qdrant_path=qdrant_path,
        limit=CANDIDATE_TOP_K,
        filters=filters,
    )
    if debug:
        print_qdrant_debug(candidates)

    best_chunks = rerank_results(
        query=query.strip(),
        candidates=candidates,
        top_n=FINAL_TOP_N,
    )
    if debug:
        print_reranker_debug(best_chunks)

    answer = generate_answer(query.strip(), best_chunks)
    if debug:
        print("\nFINAL GEMINI ANSWER")
        print(answer)
    return answer

