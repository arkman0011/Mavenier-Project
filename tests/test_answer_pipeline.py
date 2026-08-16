import mavenier.rag.generation.pipeline as answer_pipeline
from mavenier.rag.generation.llm import NO_CONTEXT_MESSAGE


def test_answer_pipeline_reuses_existing_search_with_required_counts(monkeypatch):
    calls = {}
    candidate = {
        "score": 0.8,
        "text": "Definition text",
        "source": "38.331.md",
        "section": "Definitions",
        "metadata": {"timer_metadata": {"items": [{"timer_name": "T300"}]}},
        "payload": {"chunk_id": "chunk-1"},
    }

    def fake_search_text(**kwargs):
        calls["search"] = kwargs
        return [candidate]

    def fake_rerank_results(**kwargs):
        calls["rerank"] = kwargs
        preserved = dict(kwargs["candidates"][0])
        preserved.update(rerank_score=3.0, vector_score=0.8)
        return [preserved]

    def fake_generate_answer(query, results):
        calls["generate"] = (query, results)
        return "Grounded answer"

    monkeypatch.setattr(answer_pipeline, "search_text", fake_search_text)
    monkeypatch.setattr(answer_pipeline, "rerank_results", fake_rerank_results)
    monkeypatch.setattr(answer_pipeline, "generate_answer", fake_generate_answer)

    answer = answer_pipeline.ask_rag("What is RRC?", debug=False)
    assert answer == "Grounded answer"
    assert calls["search"]["limit"] == 10
    assert calls["rerank"]["top_n"] == 3
    assert calls["generate"][1][0]["metadata"] == candidate["metadata"]


def test_no_qdrant_results_returns_without_gemini(monkeypatch):
    monkeypatch.setattr(answer_pipeline, "search_text", lambda **kwargs: [])
    assert answer_pipeline.ask_rag("Unknown topic") == NO_CONTEXT_MESSAGE


def test_debug_mode_shows_both_rankings_and_final_answer(monkeypatch, capsys):
    candidate = {
        "score": 0.8,
        "text": "Definition",
        "source": "source.md",
        "section": "Section A",
        "metadata": {},
        "payload": {"chunk_id": "one"},
    }
    reranked = [{**candidate, "vector_score": 0.8, "rerank_score": 2.0}]
    monkeypatch.setattr(answer_pipeline, "search_text", lambda **kwargs: [candidate])
    monkeypatch.setattr(answer_pipeline, "rerank_results", lambda **kwargs: reranked)
    monkeypatch.setattr(answer_pipeline, "generate_answer", lambda *args: "Answer")
    answer_pipeline.ask_rag("Question", debug=True)
    output = capsys.readouterr().out
    assert "QDRANT RESULTS" in output
    assert "RERANKED RESULTS" in output
    assert "FINAL GEMINI ANSWER" in output
    assert "0.800000" in output
    assert "2.000000" in output

