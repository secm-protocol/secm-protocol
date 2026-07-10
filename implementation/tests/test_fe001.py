"""RFC-0022 validation suite — FE-001 Nominal Encoding System v0.1.

Primary vector: "Osvaldo Vaz da Costa Filho" — the same name hand-computed
under classical Pythagorean numerology at the very start of this project's
history (total=7, vowels=1, consonants=6). Reusing it here demonstrates the
constitutional promise directly: same arithmetic, neutral names, honest
confidence — decomposition, not adopted belief (RFC-0000 §3-4).
"""

import pytest

from secm import validate
from secm.engines import fe001_nominal as fe001

BANNED_TERMS = (
    "life path", "soul number", "soul urge", "expression number",
    "kabbalah", "gematria", "astrology", "master number",
)


def test_reference_name_matches_hand_computed_numerology():
    unit = fe001.encode(
        "Osvaldo Vaz da Costa Filho",
        entity_ref="graph:person:vision-keeper",
        consent_scope="consent:v1:rx-analysis:vision-keeper",
    )
    assert unit["value"]["total_reduction"] == 7
    assert unit["value"]["vowel_reduction"] == 1
    assert unit["value"]["consonant_reduction"] == 6


def test_unit_validates_strict():
    unit = fe001.encode(
        "Osvaldo Vaz da Costa Filho",
        entity_ref="graph:person:x",
        consent_scope="consent:v1:test",
    )
    assert validate(unit, strict_registry=True) == []


def test_confidence_is_low_and_labeled_by_description():
    unit = fe001.encode(
        "Ana Lima", entity_ref="graph:person:x", consent_scope="consent:v1:test"
    )
    assert unit["confidence"] == fe001.BASELINE_CONFIDENCE
    assert unit["confidence"] < 0.5  # deliberately weaker than self-report (0.55)


def test_no_banned_terminology_in_output():
    """The module docstring may *name* the banned terms to document the
    constitutional rule (RFC-0000 §4) — that is documentation, not exposure.
    The unit itself (what the protocol actually produces/exposes) must never
    contain them."""
    unit = fe001.encode(
        "Ana Lima", entity_ref="graph:person:x", consent_scope="consent:v1:test"
    )
    blob = str(unit).lower()
    for term in BANNED_TERMS:
        assert term not in blob, term


def test_determinism():
    a = fe001.encode("Ana Lima", entity_ref="graph:person:x", consent_scope="c")
    b = fe001.encode("Ana Lima", entity_ref="graph:person:x", consent_scope="c")
    assert a["value"] == b["value"]


def test_case_and_whitespace_insensitive():
    a = fe001.encode("ana lima", entity_ref="graph:person:x", consent_scope="c")
    b = fe001.encode("  ANA   LIMA  ", entity_ref="graph:person:x", consent_scope="c")
    assert a["value"] == b["value"]


def test_empty_name_raises():
    with pytest.raises(ValueError):
        fe001.encode("123 !!!", entity_ref="graph:person:x", consent_scope="c")


def test_output_irreversible_to_raw_name():
    unit = fe001.encode(
        "Osvaldo Vaz da Costa Filho",
        entity_ref="graph:person:x",
        consent_scope="consent:v1:test",
    )
    serialized = str(unit).lower()
    assert "osvaldo" not in serialized
    assert "costa" not in serialized


def test_reduction_halts_at_repdigit_multiples_of_11():
    from secm.reduction import reduce_number

    assert reduce_number(11) == 11
    assert reduce_number(22) == 22
    assert reduce_number(33) == 33
    assert reduce_number(29) == 11  # 2+9=11 -> halts at 11
    assert reduce_number(88) == 7  # 8+8=16 -> 1+6=7
