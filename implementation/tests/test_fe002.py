"""RFC-0023 validation suite — FE-002 Temporal Encoding System v0.1.

Primary vector: 1986-04-20 — the same birth date hand-computed under
classical numerology at the very start of this project's history
(reduction=3). Ground truth for birth_weekday verified against Python's
own calendar (Sunday).
"""

from secm import validate
from secm.engines import fe002_temporal as fe002


def test_reference_date_matches_hand_computed_numerology():
    unit = fe002.encode(
        "1986-04-20",
        entity_ref="graph:person:vision-keeper",
        consent_scope="consent:v1:rx-analysis:vision-keeper",
    )
    assert unit["value"]["date_reduction"] == 3
    assert unit["value"]["birth_weekday"] == "Sunday"


def test_unit_validates_strict():
    unit = fe002.encode(
        "1990-01-01", entity_ref="graph:person:x", consent_scope="consent:v1:test"
    )
    assert validate(unit, strict_registry=True) == []


def test_confidence_is_low_for_both_fields():
    unit = fe002.encode(
        "1990-01-01", entity_ref="graph:person:x", consent_scope="consent:v1:test"
    )
    assert unit["confidence"] == fe002.BASELINE_CONFIDENCE
    assert unit["confidence"] < 0.5


def test_determinism():
    a = fe002.encode("1990-01-01", entity_ref="graph:person:x", consent_scope="c")
    b = fe002.encode("1990-01-01", entity_ref="graph:person:x", consent_scope="c")
    assert a["value"] == b["value"]


def test_output_irreversible_to_raw_date():
    unit = fe002.encode(
        "1986-04-20", entity_ref="graph:person:x", consent_scope="consent:v1:test"
    )
    serialized = str(unit)
    assert "1986" not in serialized
    assert "04-20" not in serialized


def test_no_banned_terminology_in_output():
    unit = fe002.encode(
        "1990-01-01", entity_ref="graph:person:x", consent_scope="consent:v1:test"
    )
    blob = str(unit).lower()
    for term in ("life path", "master number", "astrology"):
        assert term not in blob
