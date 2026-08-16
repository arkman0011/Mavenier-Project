"""Five deterministic metadata extractors for 3GPP RRC text."""

from __future__ import annotations

import re
from typing import Any

from mavenier.rag.ingestion.content_classifier import should_extract_requirements

STATE_RE = re.compile(r"\bRRC_(?:IDLE|INACTIVE|CONNECTED)\b", re.IGNORECASE)
TIMER_RE = re.compile(r"\bT\d{3,4}\b", re.IGNORECASE)
NORMATIVE_RE = re.compile(r"\b(shall not|should not|need not|shall|should|may)\b", re.IGNORECASE)
MESSAGE_RE = re.compile(
    r"\b(?:RRC[A-Z][A-Za-z0-9-]*|[A-Z][A-Za-z0-9-]*"
    r"(?:Request|Response|Complete|Command|Indication|Failure|Reject|Setup|Release))\b"
)


def _unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))


def _nearby(text: str, start: int, end: int, distance: int = 120) -> str:
    return text[max(0, start - distance):min(len(text), end + distance)]


def extract_direction_metadata(text: str) -> dict[str, list[dict[str, Any]]]:
    """Find only explicitly written UE/network directions."""
    pattern = re.compile(
        r"\b(UE\s+(?:to|→)\s+(?:the\s+)?network|"
        r"(?:the\s+)?network\s+(?:to|→)\s+UE)\b",
        re.IGNORECASE,
    )
    items = []
    for match in pattern.finditer(text):
        ue_to_network = match.group(1).lower().startswith("ue")
        context = _nearby(text, match.start(), match.end())
        message = MESSAGE_RE.search(context)
        srb = re.search(r"\bSRB\d\b", context, re.IGNORECASE)
        rlc = re.search(r"\b(?:AM|UM|TM)\s+RLC\b", context, re.IGNORECASE)
        channel = re.search(r"\b(?:CCCH|DCCH|BCCH|PCCH)\b", context, re.IGNORECASE)
        items.append({
            "content_kind": "rrc_message",
            "message_name": message.group(0) if message else None,
            "direction": "UE to Network" if ue_to_network else "Network to UE",
            "sender": "UE" if ue_to_network else "Network",
            "receiver": "Network" if ue_to_network else "UE",
            "signalling_radio_bearer": srb.group(0).upper() if srb else None,
            "rlc_sap": rlc.group(0).upper() if rlc else None,
            "logical_channel": channel.group(0).upper() if channel else None,
        })
    return {"items": items}


def extract_state_metadata(text: str) -> dict[str, list[dict[str, Any]]]:
    """Find state transitions first, then remaining standalone state mentions."""
    transition = re.compile(
        r"\b(?:from\s+)?(RRC_(?:IDLE|INACTIVE|CONNECTED))\s+"
        r"(?:state\s+)?to\s+(RRC_(?:IDLE|INACTIVE|CONNECTED))\b",
        re.IGNORECASE,
    )
    items = []
    consumed: set[str] = set()
    for match in transition.finditer(text):
        current, target = match.group(1).upper(), match.group(2).upper()
        consumed.update((current, target))
        items.append({
            "content_kind": "rrc_procedure", "procedure_name": None,
            "current_state": current, "target_state": target,
            "actor": None, "trigger_message": None,
        })
    for state in _unique([value.upper() for value in STATE_RE.findall(text)]):
        if state not in consumed:
            items.append({
                "content_kind": "rrc_procedure", "procedure_name": None,
                "current_state": state, "target_state": None,
                "actor": None, "trigger_message": None,
            })
    return {"items": items}


def extract_timer_metadata(text: str) -> dict[str, list[dict[str, Any]]]:
    """Associate each timer with the closest explicit start/stop/expiry event."""
    event_re = re.compile(
        r"\b(start(?:ed|ing)?|stop(?:ped|ping)?|expir(?:y|e[sd]?|ing))\b",
        re.IGNORECASE,
    )
    items = []
    for timer_match in TIMER_RE.finditer(text):
        context_start = max(0, timer_match.start() - 80)
        context = text[context_start:min(len(text), timer_match.end() + 120)]
        timer_center = timer_match.start() - context_start + len(timer_match.group(0)) / 2
        events = list(event_re.finditer(context))
        nearest = min(
            events,
            key=lambda event: abs((event.start() + event.end()) / 2 - timer_center),
            default=None,
        )
        event_name = None
        if nearest:
            word = nearest.group(1).lower()
            event_name = "start" if word.startswith("start") else "stop" if word.startswith("stop") else "expiry"
        message = MESSAGE_RE.search(context)
        items.append({
            "content_kind": "timer_procedure",
            "timer_name": timer_match.group(0).upper(),
            "timer_event": event_name,
            "timer_actor": None,
            "related_procedure": None,
            "related_message": message.group(0) if message else None,
            "expiry_action": None,
        })
    keyed = {(item["timer_name"], item["timer_event"], item["related_message"]): item for item in items}
    return {"items": list(keyed.values())}


def extract_asn1_metadata(text: str) -> dict[str, list[dict[str, Any]]]:
    """Extract multiline SEQUENCE, CHOICE, and ENUMERATED definitions."""
    definition_re = re.compile(
        r"(?m)^\s*([A-Za-z][\w-]*)\s*::=\s*(SEQUENCE|CHOICE|ENUMERATED)\b"
    )
    starts = list(definition_re.finditer(text))
    items = []
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        body = text[match.end():end]
        field_names: list[str] = []
        referenced_types: list[str] = []
        if match.group(2).upper() in {"SEQUENCE", "CHOICE"}:
            field_re = re.compile(
                r"(?m)^\s*([a-z][\w-]*)\s+([A-Za-z][\w-]*)"
                r"(?:\s+OPTIONAL)?\s*,?\s*$"
            )
            for field in field_re.finditer(body):
                field_names.append(field.group(1))
                referenced_types.append(field.group(2))
        items.append({
            "content_kind": "asn1_definition",
            "asn1_entity": match.group(1),
            "asn1_type": match.group(2).upper(),
            "parent_message": None,
            "field_names": _unique(field_names),
            "referenced_types": _unique(referenced_types),
        })
    return {"items": items}


def _actor_before_normative(text: str) -> str | None:
    """Return a small set of explicit 3GPP actors; otherwise do not guess."""
    actors = re.findall(
        r"\b(?:the\s+)?(UE|network|gNB|eNB|AMF|RRC|UICC|USIM|ME)\b",
        text,
        re.IGNORECASE,
    )
    return actors[-1].upper() if actors else None


def extract_requirement_metadata(
    text: str,
    content_kind: str = "general_text",
) -> dict[str, list[dict[str, Any]]]:
    """Keep multiline conditions and normative actions in the same sentence."""
    if not should_extract_requirements(content_kind, text):
        return {"items": []}

    normalized = re.sub(r"\s+", " ", text).strip()
    sentences = re.split(r"(?<=[.;])\s+(?=[A-Z])", normalized)
    items = []
    for sentence in sentences:
        matches = list(NORMATIVE_RE.finditer(sentence))
        for index, match in enumerate(matches):
            # For a second normative term, its condition starts after the previous
            # action separator rather than repeating the entire first clause.
            left_start = matches[index - 1].end() if index else 0
            condition = sentence[left_start:match.start()].strip(" ,;:") or None
            action_end = matches[index + 1].start() if index + 1 < len(matches) else len(sentence)
            action = sentence[match.end():action_end].strip(" ,;:") or None
            term = match.group(1).lower()
            strength = "mandatory" if term.startswith("shall") else "recommended" if term.startswith("should") else "permitted"
            timer = TIMER_RE.search(sentence)
            message = MESSAGE_RE.search(sentence)
            items.append({
                "content_kind": "requirement",
                "requirement_actor": _actor_before_normative(sentence[:match.start()]),
                "condition": condition,
                "requirement_action": action,
                "normative_term": term,
                "requirement_strength": strength,
                "related_timer": timer.group(0).upper() if timer else None,
                "related_message": message.group(0) if message else None,
            })
    return {"items": items}


def extract_all_metadata(text: str, content_kind: str = "general_text") -> dict[str, Any]:
    """Run all five independent rule-based extractors."""
    return {
        "direction_metadata": extract_direction_metadata(text),
        "state_metadata": extract_state_metadata(text),
        "timer_metadata": extract_timer_metadata(text),
        "asn1_metadata": extract_asn1_metadata(text),
        "requirement_metadata": extract_requirement_metadata(text, content_kind),
    }

