"""Build the explicit LangGraph State -> Nodes -> Edges workflow."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any

from langgraph.graph import END, START, StateGraph

from mavenier.rag.agents.answer_generator import (
    answer_generator_node,
    answer_regenerator_node,
)
from mavenier.rag.agents.context_builder import context_builder_node
from mavenier.rag.agents.evidence_checker import evidence_checker_node
from mavenier.rag.agents.fact_verifier import fact_verifier_node
from mavenier.rag.agents.finalizer import (
    finalizer_node,
    insufficient_answer_node,
    safe_finalizer_node,
)
from mavenier.rag.agents.query_refinement import query_refinement_node
from mavenier.rag.agents.query_understanding import query_understanding_node
from mavenier.rag.agents.reranker import reranker_node
from mavenier.rag.agents.retriever import retriever_node
from mavenier.rag.agents.search_planner import search_planner_node
from mavenier.rag.graph.routes import route_after_evidence, route_after_verification
from mavenier.rag.graph.state import RAGState

Node = Callable[[RAGState], dict[str, Any]]

DEFAULT_NODES: dict[str, Node] = {
    "query_understanding": query_understanding_node,
    "search_planner": search_planner_node,
    "retriever": retriever_node,
    "reranker": reranker_node,
    "evidence_checker": evidence_checker_node,
    "query_refinement": query_refinement_node,
    "context_builder": context_builder_node,
    "answer_generator": answer_generator_node,
    "fact_verifier": fact_verifier_node,
    "answer_regenerator": answer_regenerator_node,
    "finalizer": finalizer_node,
    "safe_finalizer": safe_finalizer_node,
    "insufficient_answer": insufficient_answer_node,
}


def build_agentic_rag_graph(nodes: Mapping[str, Node] | None = None):
    """Compile the production graph or a test graph with the same routing."""
    selected = dict(DEFAULT_NODES if nodes is None else nodes)
    missing = set(DEFAULT_NODES) - set(selected)
    if missing:
        raise ValueError(f"Missing graph nodes: {', '.join(sorted(missing))}")

    builder = StateGraph(RAGState)
    for name in DEFAULT_NODES:
        builder.add_node(name, selected[name])

    builder.add_edge(START, "query_understanding")
    builder.add_edge("query_understanding", "search_planner")
    builder.add_edge("search_planner", "retriever")
    builder.add_edge("retriever", "reranker")
    builder.add_edge("reranker", "evidence_checker")
    builder.add_conditional_edges(
        "evidence_checker",
        route_after_evidence,
        {
            "sufficient": "context_builder",
            "retry": "query_refinement",
            "insufficient": "insufficient_answer",
        },
    )
    builder.add_edge("query_refinement", "retriever")
    builder.add_edge("context_builder", "answer_generator")
    builder.add_edge("answer_generator", "fact_verifier")
    builder.add_conditional_edges(
        "fact_verifier",
        route_after_verification,
        {
            "supported": "finalizer",
            "regenerate": "answer_regenerator",
            "safe_finalize": "safe_finalizer",
        },
    )
    builder.add_edge("answer_regenerator", "fact_verifier")
    builder.add_edge("finalizer", END)
    builder.add_edge("safe_finalizer", END)
    builder.add_edge("insufficient_answer", END)
    return builder.compile()


graph = build_agentic_rag_graph()
