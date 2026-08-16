"""Create lightweight CPU embeddings with BAAI/bge-small-en-v1.5."""

from __future__ import annotations

import math
from functools import lru_cache
from typing import Any

MODEL_NAME = "BAAI/bge-small-en-v1.5"
DEVICE = "cpu"
EMBEDDING_DIMENSION = 384
MAX_SEQUENCE_LENGTH = 512
BATCH_SIZE = 4
QUERY_INSTRUCTION = "Represent this sentence for searching relevant passages: "


class TokenLengthError(ValueError):
    """Raised instead of silently truncating an oversized chunk."""


@lru_cache(maxsize=1)
def load_tokenizer() -> Any:
    """Load the official tokenizer belonging to the BGE embedding model."""
    try:
        from transformers import AutoTokenizer
    except ImportError as exc:
        raise RuntimeError(
            "Transformers is not installed. Install requirements.txt first."
        ) from exc

    try:
        return AutoTokenizer.from_pretrained(MODEL_NAME)
    except Exception as exc:
        raise RuntimeError(f"Could not load tokenizer {MODEL_NAME}: {exc}") from exc


@lru_cache(maxsize=1)
def load_embedding_model() -> Any:
    """Load BGE-small on the CPU and verify its output dimension."""
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise RuntimeError(
            "Sentence Transformers is not installed. Install requirements.txt first."
        ) from exc

    try:
        model = SentenceTransformer(MODEL_NAME, device=DEVICE)
        model.max_seq_length = MAX_SEQUENCE_LENGTH
        dimension = model.get_sentence_embedding_dimension()
    except Exception as exc:
        raise RuntimeError(f"Could not load embedding model {MODEL_NAME}: {exc}") from exc

    if dimension != EMBEDDING_DIMENSION:
        raise RuntimeError(
            f"Expected {EMBEDDING_DIMENSION} embedding dimensions, got {dimension}."
        )
    return model


def chunk_text(chunk: dict[str, Any]) -> str:
    """Return only the original chunk text; never add metadata to embeddings."""
    text = chunk.get("original_text")
    if text is None:
        # This fallback makes the module usable with the conceptual `text` schema
        # from the design prompt while preferring this project's real key.
        text = chunk.get("text")
    if not isinstance(text, str) or not text.strip():
        chunk_id = chunk.get("chunk_id", "<unknown>")
        raise ValueError(f"Chunk {chunk_id} has no non-empty text.")
    return text


def count_tokens(text: str, tokenizer: Any | None = None) -> int:
    """Count BGE tokens, including the model's required special tokens."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Cannot count tokens for empty text.")
    tokenizer = tokenizer or load_tokenizer()
    token_ids = tokenizer.encode(
        text,
        add_special_tokens=True,
        truncation=False,
    )
    return len(token_ids)


def validate_token_length(
    text: str,
    tokenizer: Any | None = None,
    label: str = "text",
) -> int:
    """Reject text above 512 tokens so important content is never truncated."""
    token_count = count_tokens(text, tokenizer)
    if token_count > MAX_SEQUENCE_LENGTH:
        raise TokenLengthError(
            f"{label} contains {token_count} BGE tokens; the safe maximum is "
            f"{MAX_SEQUENCE_LENGTH}. Re-chunk this text instead of truncating it."
        )
    return token_count


def _normalise_vector(vector: Any) -> list[float]:
    """Return a finite, 384-dimensional unit vector."""
    values = vector.tolist() if hasattr(vector, "tolist") else list(vector)
    values = [float(value) for value in values]
    if len(values) != EMBEDDING_DIMENSION:
        raise ValueError(
            f"Expected a {EMBEDDING_DIMENSION}-dimensional embedding, "
            f"got {len(values)} dimensions."
        )
    if not all(math.isfinite(value) for value in values):
        raise ValueError("Embedding contains a non-finite number.")
    norm = math.sqrt(sum(value * value for value in values))
    if norm == 0:
        raise ValueError("Embedding model returned a zero vector.")
    return [value / norm for value in values]


def embed_text(
    text: str,
    model: Any | None = None,
    tokenizer: Any | None = None,
) -> list[float]:
    """Validate and embed one passage using CPU-friendly settings."""
    tokenizer = tokenizer or load_tokenizer()
    validate_token_length(text, tokenizer)
    model = model or load_embedding_model()
    vectors = model.encode(
        [text],
        batch_size=1,
        show_progress_bar=False,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    return _normalise_vector(vectors[0])


def embed_chunks(
    chunks: list[dict[str, Any]],
    model: Any | None = None,
    tokenizer: Any | None = None,
    batch_size: int = BATCH_SIZE,
) -> list[list[float]]:
    """Embed multiple records after validating every chunk first."""
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1.")
    if not chunks:
        return []

    tokenizer = tokenizer or load_tokenizer()
    texts = []
    for chunk in chunks:
        text = chunk_text(chunk)
        validate_token_length(
            text,
            tokenizer,
            label=f"Chunk {chunk.get('chunk_id', '<unknown>')}",
        )
        texts.append(text)

    model = model or load_embedding_model()
    vectors = model.encode(
        texts,
        batch_size=batch_size,
        show_progress_bar=len(texts) > batch_size,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    return [_normalise_vector(vector) for vector in vectors]


def embed_query(
    query: str,
    model: Any | None = None,
    tokenizer: Any | None = None,
) -> list[float]:
    """Embed a search query using BGE's retrieval instruction."""
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Search query cannot be empty.")
    instructed_query = QUERY_INSTRUCTION + query.strip()
    return embed_text(instructed_query, model=model, tokenizer=tokenizer)

