from types import SimpleNamespace

import pytest

import mavenier.rag.generation.llm as llm
from mavenier.rag.agents.schemas import QueryUnderstandingResult
from mavenier.rag.generation.llm import (
    NO_CONTEXT_MESSAGE,
    SYSTEM_PROMPT,
    build_rag_prompt,
    generate_answer,
)


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
        in SYSTEM_PROMPT
    )


def test_generate_answer_uses_gemini_model_and_grounding_config(monkeypatch):
    client = FakeGeminiClient()
    fake_config = {"system_instruction": SYSTEM_PROMPT, "temperature": 0.1}
    monkeypatch.setattr(llm, "_generation_config", lambda: fake_config)
    answer = generate_answer(
        "What is an RRC Connection?", [result_with_metadata()], client=client
    )
    call = client.models.calls[0]
    assert call["model"] == "gemini-3.5-flash"
    assert call["config"] == fake_config
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
                    "intent": "timer_behavior",
                    "entities": {"timer": "T3510"},
                    "keywords": ["T3510"],
                },
                text=None,
            )

    result = llm.generate_structured(
        prompt="Analyze T3510",
        system_prompt="Return structured data.",
        response_model=QueryUnderstandingResult,
        client=SimpleNamespace(models=StructuredModelsApi()),
    )

    assert result.intent == "timer_behavior"
    assert result.entities == {"timer": "T3510"}


def test_invalid_structured_generation_is_a_system_error():
    class InvalidModelsApi:
        def generate_content(self, **kwargs):
            return SimpleNamespace(parsed=None, text="not json")

    with pytest.raises(RuntimeError, match="invalid QueryUnderstandingResult"):
        llm.generate_structured(
            prompt="Analyze T3510",
            system_prompt="Return structured data.",
            response_model=QueryUnderstandingResult,
            client=SimpleNamespace(models=InvalidModelsApi()),
        )
