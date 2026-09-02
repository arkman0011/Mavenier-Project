"""Build the query workflow as a LangGraph state machine.

Almost linear: the only branch is the deterministic abstain gate after
reranking. If retrieval is not confident, we skip the answer + verification LLM
calls entirely and go straight to a refusal. Judgment is done by the three LLM
nodes (query_analysis, answer_generator, answer_verifier); everything else is
deterministic Python.

    query_analysis -> retriever -> reranker --confident--> context_expander
                   -> answer_generator -> answer_verifier -> finalizer
                                       \\--not confident--> finalizer (refuse)
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any

from langgraph.graph import END, START, StateGraph

from mavenier.rag.agents.answer_generator import answer_generator_node
from mavenier.rag.agents.answer_verifier import answer_verifier_node
from mavenier.rag.agents.context_expander import context_expander_node
from mavenier.rag.agents.finalizer import finalizer_node
from mavenier.rag.agents.query_analysis import query_analysis_node
from mavenier.rag.agents.reranker import reranker_node
from mavenier.rag.agents.retriever import retriever_node
from mavenier.rag.graph.state import RAGState

Node = Callable[[RAGState], dict[str, Any]]

# The order here IS the graph; edges below chain these (with one branch).
PIPELINE: tuple[str, ...] = (
    "query_analysis",
    "retriever",
    "reranker",
    "context_expander",
    "answer_generator",
    "answer_verifier",
    "finalizer",
)

DEFAULT_NODES: dict[str, Node] = {
    "query_analysis": query_analysis_node,
    "retriever": retriever_node,
    "reranker": reranker_node,
    "context_expander": context_expander_node,
    "answer_generator": answer_generator_node,
    "answer_verifier": answer_verifier_node,
    "finalizer": finalizer_node,
}


def route_after_rerank(state: RAGState) -> str:
    """The one branch: answer only when retrieval is confident, else abstain."""
    return "answer" if state.get("retrieval_confident") else "abstain"


def build_agentic_rag_graph(nodes: Mapping[str, Node] | None = None):
    """Compile the production graph or a test graph with the same wiring."""
    selected = dict(DEFAULT_NODES if nodes is None else nodes)
    missing = set(DEFAULT_NODES) - set(selected)
    if missing:
        raise ValueError(f"Missing graph nodes: {', '.join(sorted(missing))}")

    builder = StateGraph(RAGState)
    for name in PIPELINE:
        builder.add_node(name, selected[name])

    builder.add_edge(START, "query_analysis")
    builder.add_edge("query_analysis", "retriever")
    builder.add_edge("retriever", "reranker")
    builder.add_conditional_edges(
        "reranker",
        route_after_rerank,
        {"answer": "context_expander", "abstain": "finalizer"},
    )
    builder.add_edge("context_expander", "answer_generator")
    builder.add_edge("answer_generator", "answer_verifier")
    builder.add_edge("answer_verifier", "finalizer")
    builder.add_edge("finalizer", END)
    return builder.compile()


graph = build_agentic_rag_graph()
