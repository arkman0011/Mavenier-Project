"""Rerank a small Qdrant candidate set with a lightweight cross-encoder."""

from __future__ import annotations

import copy
from functools import lru_cache
from typing import Any

RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L6-v2"
RERANKER_DEVICE = "cpu"
RERANKER_BATCH_SIZE = 2
DEFAULT_TOP_N = 3


@lru_cache(maxsize=1)
def load_reranker() -> Any:
    """Load the cross-encoder once and reuse it for later questions."""
    try:
        from sentence_transformers import CrossEncoder
    except ImportError as exc:
        raise RuntimeError(
            "Sentence Transformers is not installed. Install requirements.txt first."
        ) from exc

    try:
        return CrossEncoder(RERANKER_MODEL, device=RERANKER_DEVICE)
    except Exception as exc:
        raise RuntimeError(
            f"Could not load reranker {RERANKER_MODEL}: {exc}"
        ) from exc


def _candidate_text(candidate: dict[str, Any], rank: int) -> str:
    """Read the text returned by the existing Qdrant search function."""
    text = candidate.get("text")
    if not isinstance(text, str) or not text.strip():
        raise ValueError(f"Qdrant candidate {rank} has no non-empty text field.")
    return text


def rerank_results(
    query: str,
    candidates: list[dict[str, Any]],
    top_n: int = DEFAULT_TOP_N,
    model: Any | None = None,
    batch_size: int = RERANKER_BATCH_SIZE,
) -> list[dict[str, Any]]:
    """Score query/passage pairs and preserve each complete candidate."""
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Reranker query cannot be empty.")
    if top_n < 1:
        raise ValueError("top_n must be at least 1.")
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1.")
    if not candidates:
        return []

    pairs = [
        (query.strip(), _candidate_text(candidate, rank))
        for rank, candidate in enumerate(candidates, start=1)
    ]
    model = model or load_reranker()
    try:
        raw_scores = model.predict(
            pairs,
            batch_size=batch_size,
            show_progress_bar=False,
        )
    except Exception as exc:
        raise RuntimeError(f"Reranker inference failed: {exc}") from exc

    scores = raw_scores.tolist() if hasattr(raw_scores, "tolist") else list(raw_scores)
    if len(scores) != len(candidates):
        raise RuntimeError(
            "Reranker returned a different number of scores than candidates."
        )

    reranked = []
    for candidate, score in zip(candidates, scores):
        preserved = copy.deepcopy(candidate)
        payload = preserved.get("payload") or {}
        preserved.setdefault("chunk_id", payload.get("chunk_id"))
        preserved["vector_score"] = float(
            preserved.get("vector_score", preserved.get("score", 0.0))
        )
        preserved["rerank_score"] = float(score)
        reranked.append(preserved)

    reranked.sort(key=lambda item: item["rerank_score"], reverse=True)
    return reranked[: min(top_n, len(reranked))]

