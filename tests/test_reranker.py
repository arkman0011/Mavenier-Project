import copy

import pytest

from mavenier.rag.retrieval.reranker import rerank_results


class FakeReranker:
    def predict(self, pairs, batch_size, show_progress_bar):
        assert batch_size == 2
        assert show_progress_bar is False
        assert pairs[1] == ("What is RRC?", "Exact RRC definition")
        return [0.1, 4.2, -0.5]


def candidates():
    return [
        {
            "score": 0.91,
            "text": "Broad radio information",
            "source": "a.md",
            "section": "A",
            "metadata": {"timer_metadata": {"items": []}},
            "payload": {"chunk_id": "chunk-a", "direction_metadata": {"items": []}},
        },
        {
            "score": 0.82,
            "text": "Exact RRC definition",
            "source": "b.md",
            "section": "B",
            "metadata": {"state_metadata": {"items": [{"current_state": "RRC_IDLE"}]}},
            "payload": {"chunk_id": "chunk-b", "state_metadata": {"items": []}},
        },
        {
            "score": 0.75,
            "text": "Unrelated history",
            "source": "c.md",
            "section": "C",
            "metadata": {},
            "payload": {"chunk_id": "chunk-c"},
        },
    ]


def test_reranker_reorders_and_preserves_complete_results():
    original = candidates()
    before = copy.deepcopy(original)
    results = rerank_results(
        "What is RRC?", original, top_n=2, model=FakeReranker()
    )
    assert [item["chunk_id"] for item in results] == ["chunk-b", "chunk-a"]
    assert results[0]["rerank_score"] == 4.2
    assert results[0]["vector_score"] == 0.82
    assert results[0]["metadata"] == before[1]["metadata"]
    assert results[0]["payload"] == before[1]["payload"]
    assert original == before


def test_reranker_returns_early_for_no_candidates():
    assert rerank_results("Question", [], model=FakeReranker()) == []


def test_reranker_reports_malformed_candidate():
    with pytest.raises(ValueError, match="no non-empty text"):
        rerank_results("Question", [{"score": 0.5}], model=FakeReranker())

