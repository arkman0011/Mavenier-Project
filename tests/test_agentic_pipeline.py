import mavenier.rag.pipeline as pipeline


def test_public_pipeline_initializes_limits_and_returns_safe_debug(
    monkeypatch, tmp_path
):
    received = {}

    class FakeGraph:
        def invoke(self, state, config):
            received.update(state=state, config=config)
            return {
                **state,
                "intent": "definition",
                "entities": {},
                "keywords": ["RRC"],
                "search_query": "What is RRC?",
                "filters": {},
                "evidence_status": "SUFFICIENT",
                "verification_status": "SUPPORTED",
                "unsupported_claims": [],
                "trace": [{"stage": "finalizer", "confidence": 0.9}],
                "final_answer": "Grounded answer",
                "confidence": 0.9,
                "sources": [{"source": "38.331.md", "section": "Definitions"}],
            }

    monkeypatch.setattr(pipeline, "graph", FakeGraph())
    result = pipeline.ask_agentic_rag(
        "  What is RRC?  ",
        qdrant_path=tmp_path,
        filters={"section": "Definitions"},
        debug=True,
    )

    assert received["state"]["question"] == "What is RRC?"
    assert received["state"]["max_retries"] == 2
    assert received["state"]["max_answer_retries"] == 1
    assert received["state"]["requested_filters"] == {"section": "Definitions"}
    assert received["config"] == {"recursion_limit": 25}
    assert result["answer"] == "Grounded answer"
    assert result["confidence"] == 0.9
    assert "embeddings" not in result["debug"]


def test_public_pipeline_rejects_empty_question():
    try:
        pipeline.ask_agentic_rag(" ")
    except ValueError as exc:
        assert "cannot be empty" in str(exc)
    else:
        raise AssertionError("Expected an empty question to be rejected")
