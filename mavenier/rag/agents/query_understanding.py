"""Node 1: convert a telecom question into explicit structured terms."""

from __future__ import annotations

import json

from mavenier.rag.agents.common import node_update
from mavenier.rag.agents.prompts import QUERY_UNDERSTANDING_PROMPT
from mavenier.rag.agents.schemas import QueryUnderstandingResult
from mavenier.rag.generation.llm import generate_structured
from mavenier.rag.graph.state import RAGState


def query_understanding_node(state: RAGState) -> dict:
    question = state["question"].strip()
    result = generate_structured(
        prompt="Analyze this question:\n" + json.dumps(question, ensure_ascii=False),
        system_prompt=QUERY_UNDERSTANDING_PROMPT,
        response_model=QueryUnderstandingResult,
    )
    entities = {
    entity.key: entity.value
    for entity in result.entities
}
    return node_update(
        state,
        "query_understanding",
        {
            "intent": result.intent,
            "entities": entities,
            "keywords": result.keywords,
        },
        intent=result.intent,
        entities=result.entities,
        keywords=result.keywords,
    )
