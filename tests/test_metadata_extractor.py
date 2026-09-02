from mavenier.preprocessing.metadata_extractor import (
    extract_asn1_metadata,
    extract_direction_metadata,
    extract_requirement_metadata,
    extract_state_metadata,
    extract_timer_metadata,
)


def test_direction():
    item = extract_direction_metadata(
        "RRCSetupRequest is sent UE to Network using SRB1 on CCCH."
    )["items"][0]
    assert item["sender"] == "UE"
    assert item["receiver"] == "Network"
    assert item["message_name"] == "RRCSetupRequest"
    assert item["signalling_radio_bearer"] == "SRB1"


def test_state_transition():
    item = extract_state_metadata("Move from RRC_IDLE to RRC_CONNECTED.")["items"][0]
    assert item["current_state"] == "RRC_IDLE"
    assert item["target_state"] == "RRC_CONNECTED"


def test_multiple_timers_get_nearest_events():
    items = extract_timer_metadata("Start T300; T301 is stopped; expiry of T302.")["items"]
    assert [(item["timer_name"], item["timer_event"]) for item in items] == [
        ("T300", "start"), ("T301", "stop"), ("T302", "expiry")
    ]


def test_multiline_asn1():
    text = """RRCSetup ::= SEQUENCE {
    transactionIdentifier RRC-TransactionIdentifier,
    criticalExtensions CriticalExtensions OPTIONAL
}
"""
    item = extract_asn1_metadata(text)["items"][0]
    assert item["asn1_entity"] == "RRCSetup"
    assert item["field_names"] == ["transactionIdentifier", "criticalExtensions"]
    assert item["referenced_types"] == ["RRC-TransactionIdentifier", "CriticalExtensions"]


def test_requirement_keeps_condition_actor_and_action():
    item = extract_requirement_metadata(
        "If T300 expires, the UE shall transmit RRCSetupRequest."
    )["items"][0]
    assert item["requirement_actor"] == "UE"
    assert item["condition"] == "If T300 expires, the UE"
    assert item["requirement_action"] == "transmit RRCSetupRequest."
    assert item["related_timer"] == "T300"


def test_front_matter_is_not_a_technical_requirement():
    result = extract_requirement_metadata(
        "The present document may be further elaborated for the purposes of 3GPP.",
        content_kind="front_matter",
    )
    assert result == {"items": []}


def test_contact_information_has_no_hallucinated_metadata():
    text = "3GPP support office\nValbonne - France"
    extractors = (
        extract_direction_metadata,
        extract_state_metadata,
        extract_timer_metadata,
        extract_asn1_metadata,
        extract_requirement_metadata,
    )
    assert all(extractor(text) == {"items": []} for extractor in extractors)

