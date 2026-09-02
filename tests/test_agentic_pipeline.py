import mavenier.rag.pipeline as pipeline


def test_public_pipeline_passes_clean_state_and_returns_safe_debug(monkeypatch, tmp_path):
    received = {}

    class FakeGraph:
        def invoke(self, state):
            received.update(state=state)
            return {
                **state,
                "intent": "definition",
                "keywords": ["RRC"],
                "search_query": "What is RRC?",
                "filters": {},
                "filters_used": {},
                "filters_relaxed": False,
                "retrieval_confident": True,
                "top_rerank_score": 8.6,
                "verification_verdict": "supported",
                "verification_issues": [],
                "trace": [{"stage": "finalizer", "confidence": 0.9}],
                "final_answer": "Grounded answer",
                "confidence": 0.9,
                "sources": [{"source": "TS 38.331", "section": "Definitions"}],
            }

    monkeypatch.setattr(pipeline, "graph", FakeGraph())
    result = pipeline.ask_agentic_rag(
        "  What is RRC?  ",
        qdrant_path=tmp_path,
        filters={"release": "Rel-16"},
        debug=True,
    )

    assert received["state"]["question"] == "What is RRC?"
    assert received["state"]["requested_filters"] == {"release": "Rel-16"}
    assert "retry_count" not in received["state"]
    assert result["answer"] == "Grounded answer"
    assert result["confidence"] == 0.9
    assert result["debug"]["search_query"] == "What is RRC?"
    assert "embeddings" not in result["debug"]


def test_public_pipeline_rejects_empty_question():
    try:
        pipeline.ask_agentic_rag(" ")
    except ValueError as exc:
        assert "cannot be empty" in str(exc)
    else:
        raise AssertionError("Expected an empty question to be rejected")
