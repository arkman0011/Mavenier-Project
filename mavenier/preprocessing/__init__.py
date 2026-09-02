"""Offline preprocessing: turn the 3GPP spec folders into one enriched JSONL.

This package is deliberately separate from ``mavenier.rag``. It runs once, by
hand, to build ``outputs/enriched_chunks.jsonl`` from ``input/3gpp/marked``.
The RAG application only ever reads that JSONL; it never runs this code.
"""
