import math

import pytest

from mavenier.rag.retrieval.embeddings import (
    EMBEDDING_DIMENSION,
    QUERY_INSTRUCTION,
    TokenLengthError,
    chunk_text,
    embed_chunks,
    embed_query,
    validate_token_length,
)


class FakeTokenizer:
    def encode(self, text, add_special_tokens=True, truncation=False):
        assert truncation is False
        extra = 2 if add_special_tokens else 0
        return list(range(len(text.split()) + extra))


class FakeModel:
    def __init__(self):
        self.received = []

    def encode(self, texts, **kwargs):
        self.received.extend(texts)
        assert kwargs["normalize_embeddings"] is True
        return [[1.0] + [0.0] * (EMBEDDING_DIMENSION - 1) for _ in texts]


def test_chunk_text_prefers_original_and_does_not_embed_metadata():
    chunk = {
        "chunk_id": "chunk-1",
        "original_text": "The UE starts T300.",
        "contextualized_text": "Section metadata plus text",
        "timer_metadata": {"items": [{"timer_name": "T300"}]},
    }
    model = FakeModel()
    vectors = embed_chunks([chunk], model=model, tokenizer=FakeTokenizer())
    assert model.received == ["The UE starts T300."]
    assert len(vectors[0]) == 384
    assert math.isclose(sum(value * value for value in vectors[0]), 1.0)


def test_oversized_text_is_rejected_instead_of_truncated():
    text = "word " * 511  # 511 words + 2 special tokens = 513
    with pytest.raises(TokenLengthError, match="Re-chunk"):
        validate_token_length(text, FakeTokenizer())


def test_query_instruction_is_used_only_for_query():
    model = FakeModel()
    embed_query("When does the timer expire?", model=model, tokenizer=FakeTokenizer())
    assert model.received == [QUERY_INSTRUCTION + "When does the timer expire?"]


def test_missing_chunk_text_has_clear_error():
    with pytest.raises(ValueError, match="no non-empty text"):
        chunk_text({"chunk_id": "chunk-empty", "original_text": " "})

