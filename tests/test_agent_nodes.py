from mavenier.rag.agents import query_analysis
from mavenier.rag.agents import answer_generator
from mavenier.rag.agents.answer_generator import answer_generator_node
from mavenier.rag.agents.answer_verifier import answer_verifier_node
from mavenier.rag.agents.context_expander import context_expander_node
from mavenier.rag.agents.finalizer import finalizer_node
from mavenier.rag.agents.query_analysis import build_filters
from mavenier.rag.agents.retriever import retriever_node
from mavenier.rag.agents.schemas import QueryAnalysis
from mavenier.rag.generation.llm import GeminiRateLimitError


def test_build_filters_maps_only_explicit_fields_and_respects_caller():
    analysis = QueryAnalysis(
        search_query="NR RRC reconfiguration in release 16",
        intent="procedure_explanation",
        release="Rel-16",
        series="38",
        timer=None,
    )
    filters = build_filters(analysis, requested={"section": "5.3"})
    assert filters == {"release": "Rel-16", "series": "38", "section": "5.3"}


def test_build_filters_validates_timer_and_gates_asn1_on_intent():
    good = build_filters(
        QueryAnalysis(search_query="q", intent="timer_behavior", timer="t300"), None
    )
    assert good == {"timer.timer_name": "T300"}

    # asn1_entity only becomes a filter for asn1_lookup intent
    ignored = build_filters(
        QueryAnalysis(search_query="q", intent="definition", asn1_entity="RRCReconfiguration"), None
    )
    assert ignored == {}


def test_query_analysis_node_writes_query_and_filters(monkeypatch):
    monkeypatch.setattr(
        query_analysis,
        "generate_structured",
        lambda **kwargs: QueryAnalysis(
            search_query="T3510 expiry behaviour",
            intent="timer_behavior",
            keywords=["T3510"],
            timer="T3510",
        ),
    )
    result = query_analysis.query_analysis_node(
        {"question": "What happens when T3510 expires?", "requested_filters": {}}
    )
    assert result["search_query"] == "T3510 expiry behaviour"
    assert result["filters"] == {"timer.timer_name": "T3510"}
    assert result["intent"] == "timer_behavior"


def test_query_analysis_uses_local_rules_after_gemini_quota(monkeypatch):
    def quota_failure(**kwargs):
        raise GeminiRateLimitError("quota")

    monkeypatch.setattr(query_analysis, "generate_structured", quota_failure)
    result = query_analysis.query_analysis_node(
        {
            "question": "What happens when T300 expires in TS 23.002?",
            "requested_filters": {},
            "trace": [],
        }
    )

    assert result["gemini_available"] is False
    assert result["query_analysis_mode"] == "local_quota_fallback"
    assert result["intent"] == "timer_behavior"
    assert result["filters"] == {
        "series": "23",
        "spec_number": "23002",
        "timer.timer_name": "T300",
    }


def test_retriever_relaxes_filters_when_first_attempt_is_empty(monkeypatch):
    attempts = []

    def fake_search_text(query, qdrant_path, limit, filters):
        attempts.append(filters)
        # Only the unfiltered attempt returns anything.
        return [] if filters else [{"text": "hit", "source": "TS 23.501", "section": "5"}]

    monkeypatch.setattr("mavenier.rag.agents.retriever.search_text", fake_search_text)
    result = retriever_node(
        {
            "search_query": "q",
            "qdrant_path": "/tmp/q",
            "filters": {"release": "Rel-16"},
            "requested_filters": {},
            "trace": [],
        }
    )
    assert result["filters_relaxed"] is True
    assert len(result["retrieved_chunks"]) == 1
    # tried the specific filter, then relaxed to no filter (None)
    assert attempts == [{"release": "Rel-16"}, None]


def test_context_expander_dedupes_sections_and_expands(monkeypatch):
    monkeypatch.setattr(
        "mavenier.rag.agents.context_expander.fetch_section_text",
        lambda document_id, section, qdrant_path, **kwargs: f"FULL SECTION {document_id}/{section}",
    )
    two_chunks_same_section = [
        {
            "text": "fragment a",
            "source": "TS 23.501",
            "section": "5.3",
            "payload": {"document_metadata": {"document_id": "TS 23.501"}},
        },
        {
            "text": "fragment b",
            "source": "TS 23.501",
            "section": "5.3",
            "payload": {"document_metadata": {"document_id": "TS 23.501"}},
        },
    ]
    result = context_expander_node(
        {"question": "q", "qdrant_path": "/tmp/q", "reranked_chunks": two_chunks_same_section, "trace": []}
    )
    # two fragments from the same section collapse into one expanded block
    assert len(result["expanded_chunks"]) == 1
    assert result["trace"][-1]["section_count"] == 1
    assert "FULL SECTION TS 23.501/5.3" in result["context"]
    assert result["context_sources"] == [{"source": "TS 23.501", "section": "5.3"}]


def test_answer_generator_returns_excerpts_without_another_gemini_call(monkeypatch):
    monkeypatch.setattr(
        answer_generator,
        "generate_answer",
        lambda *args, **kwargs: (_ for _ in ()).throw(
            AssertionError("Gemini must not be called after quota is known")
        ),
    )
    result = answer_generator_node(
        {
            "question": "What is RRC?",
            "gemini_available": False,
            "expanded_chunks": [
                {
                    "source": "TS 36.116",
                    "section": "3.1 Definitions",
                    "text": "RRC is described by this retrieved evidence.",
                }
            ],
            "trace": [],
        }
    )

    assert result["answer_mode"] == "extractive_quota_fallback"
    assert "TS 36.116" in result["draft_answer"]
    assert "RRC is described" in result["draft_answer"]


def test_answer_verifier_caps_extractive_fallback_without_gemini(monkeypatch):
    monkeypatch.setattr(
        "mavenier.rag.agents.answer_verifier.generate_structured",
        lambda **kwargs: (_ for _ in ()).throw(
            AssertionError("Verifier must not call Gemini for extractive fallback")
        ),
    )
    result = answer_verifier_node(
        {
            "question": "What is RRC?",
            "answer_mode": "extractive_quota_fallback",
            "draft_answer": "Retrieved excerpt",
            "expanded_chunks": [],
            "trace": [],
        }
    )

    assert result["verification_verdict"] == "partially_supported"
    assert result["addresses_question"] is False
    assert result["verification_mode"] == "deterministic_quota_fallback"


def test_finalizer_refuses_when_retrieval_not_confident():
    # abstain gate reached the finalizer without answering
    result = finalizer_node({"retrieval_confident": False, "trace": []})
    assert result["confidence"] == 0.0
    assert "not contain enough reliable evidence" in result["final_answer"]
    assert result["sources"] == []


def test_finalizer_refuses_when_nothing_was_shown_to_the_model():
    # confident retrieval but expansion produced no citable sections
    result = finalizer_node(
        {"retrieval_confident": True, "draft_answer": "text", "context_sources": [], "trace": []}
    )
    assert result["confidence"] == 0.0
    assert result["sources"] == []


def test_finalizer_keeps_generator_abstention_at_zero_confidence():
    result = finalizer_node(
        {
            "retrieval_confident": True,
            "verification_verdict": "supported",
            "addresses_question": True,
            "draft_answer": (
                "The retrieved context does not contain enough information "
                "to answer this question."
            ),
            "context_sources": [{"source": "TS 22.261", "section": "6.22"}],
            "trace": [],
        }
    )

    assert result["confidence"] == 0.0
    assert result["sources"] == []
    assert "not contain enough reliable evidence" in result["final_answer"]


def test_finalizer_answers_and_cites_the_shown_sections_when_verified():
    result = finalizer_node(
        {
            "retrieval_confident": True,
            "verification_verdict": "supported",
            "addresses_question": True,
            "draft_answer": "Grounded answer",
            "context_sources": [
                {"source": "TS 38.331", "section": "4.2"},
                {"source": "TS 38.331", "section": "4.2"},  # duplicate collapses
                {"source": "TS 23.501", "section": "5.3"},
            ],
            "trace": [],
        }
    )
    assert result["final_answer"] == "Grounded answer"
    assert result["sources"] == [
        {"source": "TS 38.331", "section": "4.2"},
        {"source": "TS 23.501", "section": "5.3"},
    ]
    # 0.90 + 0.02 * (2 unique sources - 1)
    assert result["confidence"] == 0.92


def test_finalizer_refuses_safely_when_verdict_is_unsupported():
    result = finalizer_node(
        {
            "retrieval_confident": True,
            "verification_verdict": "unsupported",
            "draft_answer": "risky text",
            "context_sources": [{"source": "TS 38.331", "section": "4.2"}],
            "trace": [],
        }
    )
    assert result["confidence"] == 0.3
    assert result["sources"] == []
    assert result["final_answer"] != "risky text"


def test_finalizer_caps_confidence_when_partially_supported():
    result = finalizer_node(
        {
            "retrieval_confident": True,
            "verification_verdict": "partially_supported",
            "draft_answer": "Mostly grounded answer",
            "context_sources": [{"source": "TS 38.331", "section": "4.2"}],
            "trace": [],
        }
    )
    assert result["final_answer"] == "Mostly grounded answer"
    assert result["confidence"] <= 0.55


def test_answer_verifier_node_passes_question_answer_and_chunk_metadata(monkeypatch):
    captured = {}

    def fake_generate_structured(prompt, system_prompt, response_model, client=None):
        captured["prompt"] = prompt
        return response_model(verdict="supported", addresses_question=True, issues=[])

    monkeypatch.setattr(
        "mavenier.rag.agents.answer_verifier.generate_structured", fake_generate_structured
    )
    result = answer_verifier_node(
        {
            "question": "What happens when T300 expires?",
            "draft_answer": "The UE re-attempts the procedure.",
            "expanded_chunks": [
                {
                    "text": "If T300 expires, the UE shall...",
                    "source": "TS 38.331",
                    "section": "5.3.3",
                    "release": "Rel-16",
                    "series": "38",
                    "metadata": {"timer_metadata": {"items": [{"timer_name": "T300"}]}},
                }
            ],
            "trace": [],
        }
    )
    assert result["verification_verdict"] == "supported"
    assert "T300 expires" in captured["prompt"]
    assert "timer_metadata" in captured["prompt"]
    assert "Rel-16" in captured["prompt"]
