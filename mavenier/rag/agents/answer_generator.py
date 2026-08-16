"""Node 7 and regeneration node: grounded Gemini answer production."""

from __future__ import annotations

import json

from mavenier.rag.agents.common import node_update
from mavenier.rag.agents.prompts import ANSWER_REGENERATION_PROMPT
from mavenier.rag.generation.llm import generate_answer, generate_with_system_prompt
from mavenier.rag.graph.state import RAGState


def answer_generator_node(state: RAGState) -> dict:
    answer = generate_answer(state["question"], state.get("reranked_chunks", []))
    return node_update(
        state,
        "answer_generator",
        {"draft_created": bool(answer)},
        draft_answer=answer,
    )


def answer_regenerator_node(state: RAGState) -> dict:
    retry_count = state.get("answer_retry_count", 0) + 1
    prompt = "\n\n".join(
        (
            "QUESTION:\n" + state["question"],
            "CURRENT DRAFT:\n" + state.get("draft_answer", ""),
            "UNSUPPORTED CLAIMS:\n"
            + json.dumps(state.get("unsupported_claims", []), ensure_ascii=False),
            "RETRIEVED CONTEXT:\n" + state["context"],
        )
    )
    answer = generate_with_system_prompt(prompt, ANSWER_REGENERATION_PROMPT)
    return node_update(
        state,
        "answer_regenerator",
        {"answer_retry_count": retry_count},
        draft_answer=answer,
        answer_retry_count=retry_count,
    )
