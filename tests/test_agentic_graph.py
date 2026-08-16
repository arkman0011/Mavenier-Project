from __future__ import annotations

from collections import Counter

from mavenier.rag.graph.agentic_rag_graph import build_agentic_rag_graph


def _node_set(
    *,
    evidence_statuses: list[str],
    verification_statuses: list[str] | None = None,
) -> tuple[dict, Counter]:
    calls: Counter = Counter()
    verification_statuses = verification_statuses or ["SUPPORTED"]

    def understand(state):
        calls["query_understanding"] += 1
        return {"intent": "definition", "entities": {}, "keywords": ["RRC"]}

    def plan(state):
        calls["search_planner"] += 1
        return {"search_query": state["question"], "filters": {}}

    def retrieve(state):
        calls["retriever"] += 1
        return {
            "retrieved_chunks": [
                {
                    "text": "An RRC Connection is a point-to-point connection.",
                    "source": "38.331.md",
                    "section": "Definitions",
                    "score": 0.9,
                    "metadata": {},
                    "payload": {"chunk_id": "chunk-1"},
                }
            ]
        }

    def rerank(state):
        calls["reranker"] += 1
        result = dict(state["retrieved_chunks"][0])
        result.update(vector_score=0.9, rerank_score=4.0)
        return {"reranked_chunks": [result]}

    def check_evidence(state):
        index = min(calls["evidence_checker"], len(evidence_statuses) - 1)
        status = evidence_statuses[index]
        calls["evidence_checker"] += 1
        return {
            "evidence_status": status,
            "evidence_reason": "Enough direct evidence"
            if status == "SUFFICIENT"
            else "Missing definition",
            "missing_information": [] if status == "SUFFICIENT" else ["definition"],
        }

    def refine(state):
        calls["query_refinement"] += 1
        return {
            "retry_count": state["retry_count"] + 1,
            "search_query": f"{state['question']} RRC",
            "filters": {},
        }

    def build_context(state):
        calls["context_builder"] += 1
        return {"context": "[CONTEXT 1]\nSource: 38.331.md\nSection: Definitions"}

    def generate(state):
        calls["answer_generator"] += 1
        return {"draft_answer": "RRC definition."}

    def verify(state):
        index = min(calls["fact_verifier"], len(verification_statuses) - 1)
        status = verification_statuses[index]
        calls["fact_verifier"] += 1
        return {
            "verification_status": status,
            "unsupported_claims": []
            if status == "SUPPORTED"
            else ["Unsupported sentence"],
            "verified_claims": [],
        }

    def regenerate(state):
        calls["answer_regenerator"] += 1
        return {
            "draft_answer": "RRC definition without unsupported sentence.",
            "answer_retry_count": state["answer_retry_count"] + 1,
        }

    def finalize(state):
        calls["finalizer"] += 1
        supported = state.get("verification_status") == "SUPPORTED"
        return {
            "final_answer": state["draft_answer"]
            if supported
            else "Safe verification refusal.",
            "confidence": 0.9 if supported else 0.4,
            "sources": [{"source": "38.331.md", "section": "Definitions"}]
            if supported
            else [],
        }

    def insufficient(state):
        calls["insufficient_answer"] += 1
        return {
            "final_answer": "The retrieved documents do not contain enough reliable evidence to answer this question.",
            "confidence": 0.0,
            "sources": [],
        }

    def safe_finalize(state):
        calls["safe_finalizer"] += 1
        return {
            "final_answer": "Safe verification refusal.",
            "confidence": 0.4,
            "sources": [],
        }

    return {
        "query_understanding": understand,
        "search_planner": plan,
        "retriever": retrieve,
        "reranker": rerank,
        "evidence_checker": check_evidence,
        "query_refinement": refine,
        "context_builder": build_context,
        "answer_generator": generate,
        "fact_verifier": verify,
        "answer_regenerator": regenerate,
        "finalizer": finalize,
        "safe_finalizer": safe_finalize,
        "insufficient_answer": insufficient,
    }, calls


def _initial_state() -> dict:
    return {
        "question": "What is an RRC Connection?",
        "retry_count": 0,
        "max_retries": 2,
        "answer_retry_count": 0,
        "max_answer_retries": 1,
        "debug": False,
        "trace": [],
    }


def test_sufficient_evidence_reaches_verified_final_answer():
    nodes, calls = _node_set(evidence_statuses=["SUFFICIENT"])
    result = build_agentic_rag_graph(nodes).invoke(_initial_state())

    assert result["final_answer"] == "RRC definition."
    assert result["confidence"] == 0.9
    assert calls["retriever"] == 1
    assert calls["query_refinement"] == 0
    assert calls["answer_regenerator"] == 0


def test_insufficient_evidence_stops_after_two_refinements_without_generation():
    nodes, calls = _node_set(evidence_statuses=["INSUFFICIENT"])
    result = build_agentic_rag_graph(nodes).invoke(_initial_state())

    assert result["confidence"] == 0.0
    assert "not contain enough reliable evidence" in result["final_answer"]
    assert result["retry_count"] == 2
    assert calls["retriever"] == 3
    assert calls["query_refinement"] == 2
    assert calls["answer_generator"] == 0


def test_unsupported_answer_is_regenerated_once_and_verified_again():
    nodes, calls = _node_set(
        evidence_statuses=["SUFFICIENT"],
        verification_statuses=["UNSUPPORTED", "SUPPORTED"],
    )
    result = build_agentic_rag_graph(nodes).invoke(_initial_state())

    assert result["final_answer"] == "RRC definition without unsupported sentence."
    assert result["answer_retry_count"] == 1
    assert calls["answer_regenerator"] == 1
    assert calls["fact_verifier"] == 2


def test_unsupported_answer_never_regenerates_more_than_once():
    nodes, calls = _node_set(
        evidence_statuses=["SUFFICIENT"],
        verification_statuses=["UNSUPPORTED"],
    )
    result = build_agentic_rag_graph(nodes).invoke(_initial_state())

    assert result["final_answer"] == "Safe verification refusal."
    assert result["answer_retry_count"] == 1
    assert calls["answer_regenerator"] == 1
    assert calls["fact_verifier"] == 2
