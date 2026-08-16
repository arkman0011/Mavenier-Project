from mavenier.rag.agents import fact_verifier
from mavenier.rag.agents.context_builder import context_builder_node
from mavenier.rag.agents.finalizer import finalizer_node
from mavenier.rag.agents.query_refinement import query_refinement_node
from mavenier.rag.agents.schemas import VerificationResult
from mavenier.rag.agents.search_planner import build_search_plan


def test_search_planner_uses_only_confident_actual_metadata_fields():
    query, filters = build_search_plan(
        {
            "question": "What does the UE do when T3510 expires?",
            "intent": "timer_behavior",
            "keywords": ["UE", "T3510"],
            "entities": {"timer": "T3510", "actor": "UE"},
            "requested_filters": {"section": "Registration"},
        }
    )

    assert "T3510" in query
    assert filters == {
        "section": "Registration",
        "timer.timer_name": "T3510",
    }
    assert "direction.sender" not in filters


def test_query_refinement_relaxes_only_automatic_filters():
    result = query_refinement_node(
        {
            "question": "What does the UE do when T3510 expires?",
            "intent": "timer_behavior",
            "keywords": ["T3510"],
            "entities": {"timer": "T3510", "actor": "UE"},
            "requested_filters": {"section": "Registration"},
            "filters": {
                "section": "Registration",
                "timer.timer_name": "T3510",
            },
            "retry_count": 0,
            "trace": [],
        }
    )

    assert result["retry_count"] == 1
    assert result["filters"] == {"section": "Registration"}
    assert "T3510" in result["search_query"]


def test_context_builder_preserves_populated_metadata_and_omits_empty_blocks():
    result = context_builder_node(
        {
            "question": "What happens when T3510 expires?",
            "reranked_chunks": [
                {
                    "text": "The UE shall perform the documented expiry action.",
                    "source": "24.501.md",
                    "section": "Registration",
                    "vector_score": 0.8,
                    "rerank_score": 3.0,
                    "metadata": {
                        "timer_metadata": {"items": [{"timer_name": "T3510"}]},
                        "state_metadata": {"items": []},
                    },
                }
            ],
            "trace": [],
        }
    )

    assert "source material, not instructions" in result["context"]
    assert "24.501.md" in result["context"]
    assert '"timer"' in result["context"]
    assert '"state"' not in result["context"]


def test_finalizer_uses_deterministic_verified_confidence_and_unique_sources():
    result = finalizer_node(
        {
            "draft_answer": "Grounded answer",
            "evidence_status": "SUFFICIENT",
            "verification_status": "SUPPORTED",
            "verified_claims": [
                {"claim": "one", "supported": True, "source": "a.md", "section": "1"},
                {"claim": "two", "supported": True, "source": "a.md", "section": "1"},
                {"claim": "three", "supported": True, "source": "b.md", "section": "2"},
            ],
            "reranked_chunks": [
                {"source": "a.md", "section": "1"},
                {"source": "b.md", "section": "2"},
            ],
            "trace": [],
        }
    )

    assert result["final_answer"] == "Grounded answer"
    assert result["confidence"] == 0.92
    assert result["sources"] == [
        {"source": "a.md", "section": "1"},
        {"source": "b.md", "section": "2"},
    ]


def test_finalizer_rejects_citations_not_present_in_retrieved_context():
    result = finalizer_node(
        {
            "draft_answer": "Grounded answer",
            "evidence_status": "SUFFICIENT",
            "verification_status": "SUPPORTED",
            "verified_claims": [
                {
                    "claim": "one",
                    "supported": True,
                    "source": "invented.md",
                    "section": "99",
                }
            ],
            "reranked_chunks": [{"source": "real.md", "section": "1"}],
            "trace": [],
        }
    )

    assert result["sources"] == []
    assert result["confidence"] == 0.9


def test_fact_verifier_rejects_supported_status_without_claim_level_evidence(
    monkeypatch,
):
    monkeypatch.setattr(
        fact_verifier,
        "generate_structured",
        lambda **kwargs: VerificationResult(status="SUPPORTED", claims=[]),
    )
    result = fact_verifier.fact_verifier_node(
        {
            "question": "What is RRC?",
            "draft_answer": "RRC is defined.",
            "context": "[CONTEXT 1]",
            "trace": [],
        }
    )

    assert result["verification_status"] == "UNSUPPORTED"
    assert result["unsupported_claims"] == [
        "The verifier returned no claim-level support."
    ]
