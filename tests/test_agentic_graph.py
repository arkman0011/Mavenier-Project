from __future__ import annotations

from collections import Counter

from mavenier.rag.graph.agentic_rag_graph import PIPELINE, build_agentic_rag_graph


def _node_set(*, reranked: list | None = None, verdict: str = "supported"):
    """Fake every node so we test the wiring, not the models."""
    calls: Counter = Counter()
    reranked = [
        {"text": "An RRC Connection is a point-to-point connection.", "source": "TS 38.331", "section": "Definitions"}
    ] if reranked is None else reranked

    def query_analysis(state):
        calls["query_analysis"] += 1
        return {"intent": "definition", "keywords": ["RRC"], "search_query": state["question"], "filters": {}}

    def retriever(state):
        calls["retriever"] += 1
        return {"retrieved_chunks": reranked, "filters_used": {}, "filters_relaxed": False}

    def reranker(state):
        calls["reranker"] += 1
        return {"reranked_chunks": reranked, "retrieval_confident": bool(reranked)}

    def context_expander(state):
        calls["context_expander"] += 1
        return {
            "context": "[CONTEXT 1]",
            "context_sources": [{"source": "TS 38.331", "section": "Definitions"}],
            "expanded_chunks": reranked,
        }

    def answer_generator(state):
        calls["answer_generator"] += 1
        return {"draft_answer": "RRC definition."}

    def answer_verifier(state):
        calls["answer_verifier"] += 1
        return {"verification_verdict": verdict, "addresses_question": True, "verification_issues": []}

    def finalizer(state):
        calls["finalizer"] += 1
        if not state.get("retrieval_confident"):
            return {"final_answer": "insufficient", "confidence": 0.0, "sources": []}
        if state.get("verification_verdict") == "unsupported":
            return {"final_answer": "unsupported", "confidence": 0.3, "sources": []}
        return {
            "final_answer": state["draft_answer"],
            "confidence": 0.9,
            "sources": state.get("context_sources", []),
        }

    nodes = {
        "query_analysis": query_analysis,
        "retriever": retriever,
        "reranker": reranker,
        "context_expander": context_expander,
        "answer_generator": answer_generator,
        "answer_verifier": answer_verifier,
        "finalizer": finalizer,
    }
    return nodes, calls


def _initial_state() -> dict:
    return {"question": "What is an RRC Connection?", "qdrant_path": "/tmp/q", "debug": False, "trace": []}


def test_pipeline_runs_every_stage_once_in_order():
    nodes, calls = _node_set()
    result = build_agentic_rag_graph(nodes).invoke(_initial_state())

    assert result["final_answer"] == "RRC definition."
    assert result["confidence"] == 0.9
    for stage in PIPELINE:
        assert calls[stage] == 1


def test_low_confidence_retrieval_abstains_without_calling_any_llm():
    nodes, calls = _node_set()

    def weak_reranker(state):
        calls["reranker"] += 1
        return {"reranked_chunks": [{"text": "loosely related"}], "retrieval_confident": False}

    nodes["reranker"] = weak_reranker
    result = build_agentic_rag_graph(nodes).invoke(_initial_state())

    assert result["confidence"] == 0.0
    # the abstain gate skipped expansion, answering, AND verification
    assert calls["context_expander"] == 0
    assert calls["answer_generator"] == 0
    assert calls["answer_verifier"] == 0


def test_unsupported_verdict_reaches_finalizer_as_a_refusal():
    nodes, calls = _node_set(verdict="unsupported")
    result = build_agentic_rag_graph(nodes).invoke(_initial_state())

    assert result["confidence"] == 0.3
    assert calls["answer_verifier"] == 1
