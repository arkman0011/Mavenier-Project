"""Docling HybridChunker using the small Rust-based tokenizers package."""

from __future__ import annotations

from typing import Any, Iterator

from docling.chunking import HybridChunker
from docling_core.transforms.chunker.tokenizer.base import BaseTokenizer
from pydantic import ConfigDict
from tokenizers import Tokenizer

DEFAULT_MODEL = "BAAI/bge-small-en-v1.5"
DEFAULT_MAX_TOKENS = 400


class LightweightTokenizer(BaseTokenizer):
    """Small adapter between Hugging Face Tokenizers and Docling."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    tokenizer: Any
    max_tokens: int = DEFAULT_MAX_TOKENS

    def count_tokens(self, text: str) -> int:
        """Count tokens without importing Transformers or Torch."""
        return len(self.tokenizer.encode(text, add_special_tokens=False).ids)

    def get_max_tokens(self) -> int:
        return self.max_tokens

    def get_tokenizer(self) -> Any:
        return self.tokenizer


def build_chunker(
    model_id: str = DEFAULT_MODEL,
    max_tokens: int = DEFAULT_MAX_TOKENS,
) -> HybridChunker:
    """Build a heading-aware, token-aware HybridChunker."""
    if max_tokens < 50:
        raise ValueError("max_tokens must be at least 50")

    raw_tokenizer = Tokenizer.from_pretrained(model_id)
    tokenizer = LightweightTokenizer(tokenizer=raw_tokenizer, max_tokens=max_tokens)
    return HybridChunker(tokenizer=tokenizer, merge_peers=True)


def iter_chunks(document: Any, chunker: HybridChunker) -> Iterator[tuple[Any, str]]:
    """Yield each chunk and the heading-enriched text used later for embeddings."""
    for chunk in chunker.chunk(dl_doc=document):
        yield chunk, chunker.contextualize(chunk=chunk)

