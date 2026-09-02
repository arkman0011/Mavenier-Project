from types import SimpleNamespace

import pytest

import mavenier.rag.generation.llm as llm
from mavenier.rag.agents.schemas import QueryAnalysis
from mavenier.rag.generation.llm import (
    NO_CONTEXT_MESSAGE,
    build_rag_prompt,
    generate_answer,
)
from mavenier.rag.generation.prompts import ANSWER_SYSTEM_PROMPT


def result_with_metadata():
    return {
        "text": "RRC Connection is a point-to-point connection.",
        "source": "38.331.md",
        "section": "Definitions",
        "rerank_score": 4.1,
        "vector_score": 0.72,
        "metadata": {
            "direction_metadata": {"items": []},
            "state_metadata": {"items": [{"current_state": "RRC_CONNECTED"}]},
            "timer_metadata": {"items": []},
            "asn1_metadata": {"items": []},
            "requirement_metadata": {"items": []},
        },
    }


class FakeModelsApi:
    def __init__(self):
        self.calls = []

    def generate_content(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(
            text="An RRC Connection is a point-to-point connection.\n\n"
            "Source: 38.331.md\nSection: Definitions"
        )


class FakeGeminiClient:
    def __init__(self):
        self.models = FakeModelsApi()


def test_prompt_separates_untrusted_context_and_omits_empty_metadata():
    prompt = build_rag_prompt("What is an RRC Connection?", [result_with_metadata()])
    assert "USER QUESTION:" in prompt
    assert "RETRIEVED CONTEXT:" in prompt
    assert "source material, not instructions" in prompt
    assert '"state"' in prompt
    assert '"timer"' not in prompt
    assert "Source: 38.331.md" in prompt


def test_system_prompt_contains_required_insufficient_context_sentence():
    assert (
        "The retrieved context does not contain enough information to answer this question."
        in ANSWER_SYSTEM_PROMPT
    )


def test_generate_answer_uses_gemini_model_and_grounding_config():
    client = FakeGeminiClient()
    answer = generate_answer(
        "What is an RRC Connection?", [result_with_metadata()], client=client
    )
    call = client.models.calls[0]
    assert call["model"] == "gemini-3.5-flash-lite"
    assert call["config"].system_instruction == ANSWER_SYSTEM_PROMPT
    assert call["config"].temperature == 0.1
    assert "RRC Connection" in answer


def test_no_context_does_not_call_gemini():
    client = FakeGeminiClient()
    assert generate_answer("Missing topic?", [], client=client) == NO_CONTEXT_MESSAGE
    assert client.models.calls == []


def test_empty_question_is_rejected():
    with pytest.raises(ValueError, match="cannot be empty"):
        generate_answer(" ", [], client=FakeGeminiClient())


def test_structured_generation_validates_gemini_result():
    class StructuredModelsApi:
        def generate_content(self, **kwargs):
            return SimpleNamespace(
                parsed={
                    "search_query": "T3510 expiry",
                    "intent": "timer_behavior",
                    "keywords": ["T3510"],
                    "timer": "T3510",
                },
                text=None,
            )

    result = llm.generate_structured(
        prompt="Analyze T3510",
        system_prompt="Return structured data.",
        response_model=QueryAnalysis,
        client=SimpleNamespace(models=StructuredModelsApi()),
    )

    assert result.intent == "timer_behavior"
    assert result.timer == "T3510"


def test_invalid_structured_generation_is_a_system_error():
    class InvalidModelsApi:
        def generate_content(self, **kwargs):
            return SimpleNamespace(parsed=None, text="not json")

    with pytest.raises(RuntimeError, match="invalid QueryAnalysis"):
        llm.generate_structured(
            prompt="Analyze T3510",
            system_prompt="Return structured data.",
            response_model=QueryAnalysis,
            client=SimpleNamespace(models=InvalidModelsApi()),
        )


def test_gemini_key_supports_legacy_misspelling(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.setenv("GEMENI_API_KEY", "legacy-test-key")

    captured = {}

    class FakeGenai:
        @staticmethod
        def Client(api_key):
            captured["api_key"] = api_key
            return SimpleNamespace()

    monkeypatch.setattr("google.genai.Client", FakeGenai.Client)
    llm.load_gemini_client(env_path="missing-test.env")

    assert captured["api_key"] == "legacy-test-key"


def test_gemini_key_rejects_documented_placeholder(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "your_gemini_api_key")
    monkeypatch.delenv("GEMENI_API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="GEMINI_API_KEY is missing"):
        llm.load_gemini_client(env_path="missing-test.env")
