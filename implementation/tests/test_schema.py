"""RFC-0002 validation suite — written field-by-field against the RFC text.

These tests are the portable contract: any future implementation in any
language must pass equivalent vectors.
"""

import copy
import uuid

from secm import validate
from secm.registry import conforms_to_naming_rule, is_personal


def canonical_unit() -> dict:
    """A fully valid RFC-0002 unit (personal data, so consent_scope present)."""
    return {
        "schema_version": "0.1.0",
        "id": str(uuid.uuid4()),
        "entity_ref": "graph:person:anonymous-1",
        "semantic_type": "PERSON_BEHAVIOR_RISK",
        "engine": {"id": "FE-006", "version": "0.1.0"},
        "transformation": {
            "name": "risk-posture-encoding",
            "description": "maps the RX Q8 categorical answer to the risk posture scale",
            "source_tradition": "behavioral self-report, structured questionnaire",
            "parameters_hash": "a" * 64,
        },
        "value": {"risk_posture": "calculated"},
        "confidence": 0.85,
        "provenance": ["descriptor:rx-intake:v0.1:Q8"],
        "created_at": "2026-07-09T12:00:00+00:00",
        "consent_scope": "consent:v1:rx-analysis",
    }


def test_canonical_unit_is_valid():
    assert validate(canonical_unit()) == []


def test_every_missing_envelope_field_fails():
    for field in (
        "schema_version", "id", "entity_ref", "semantic_type", "engine",
        "transformation", "value", "confidence", "provenance", "created_at",
    ):
        unit = canonical_unit()
        del unit[field]
        errors = validate(unit)
        assert errors, f"removing '{field}' must fail validation"
        assert field in errors[0]


def test_unknown_schema_major_is_rejected():
    unit = canonical_unit()
    unit["schema_version"] = "1.0.0"
    errors = validate(unit)
    assert any("unknown schema major" in e for e in errors)


def test_invalid_uuid_is_rejected():
    unit = canonical_unit()
    unit["id"] = "not-a-uuid"
    assert any("UUID" in e for e in validate(unit))


def test_semantic_type_naming_rule_enforced():
    unit = canonical_unit()
    unit["semantic_type"] = "person_behavior_risk"  # lowercase: violates naming rule
    assert any("naming rule" in e for e in validate(unit))
    unit["semantic_type"] = "WRONGNS_FIELD"  # unknown namespace
    assert any("naming rule" in e for e in validate(unit))


def test_strict_registry_mode():
    unit = canonical_unit()
    unit["semantic_type"] = "PERSON_UNREGISTERED_THING"
    assert validate(unit) == []  # lenient: naming ok, registry not enforced
    assert any("not registered" in e for e in validate(unit, strict_registry=True))


def test_transformation_fields_are_mandatory():
    for field in ("name", "description", "source_tradition", "parameters_hash"):
        unit = canonical_unit()
        unit["transformation"][field] = ""
        errors = validate(unit)
        assert any(f"transformation.{field}" in e for e in errors), (
            f"empty transformation.{field} must fail — no hidden transformations"
        )


def test_parameters_hash_must_be_sha256():
    unit = canonical_unit()
    unit["transformation"]["parameters_hash"] = "xyz123"
    assert any("sha256" in e for e in validate(unit))


def test_confidence_bounds():
    for bad in (-0.1, 1.1, "high", True, None):
        unit = canonical_unit()
        unit["confidence"] = bad
        assert any("confidence" in e for e in validate(unit)), f"{bad!r} must fail"
    for ok in (0.0, 0.5, 1.0, 1):
        unit = canonical_unit()
        unit["confidence"] = ok
        assert validate(unit) == [], f"{ok!r} must pass"


def test_provenance_must_be_non_empty():
    unit = canonical_unit()
    unit["provenance"] = []
    assert any("provenance" in e for e in validate(unit))
    unit["provenance"] = ["ok", ""]
    assert any("provenance" in e for e in validate(unit))


def test_created_at_must_be_iso8601():
    unit = canonical_unit()
    unit["created_at"] = "09/07/2026 12:00"
    assert any("ISO-8601" in e for e in validate(unit))


def test_personal_unit_requires_consent_scope():
    unit = canonical_unit()
    del unit["consent_scope"]
    errors = validate(unit)
    assert any("consent_scope" in e for e in errors)


def test_non_personal_unit_needs_no_consent_scope():
    unit = canonical_unit()
    unit["semantic_type"] = "ECON_INDICATOR"
    unit["entity_ref"] = "graph:place:brazil"
    del unit["consent_scope"]
    assert validate(unit) == []


def test_multiple_errors_reported_together():
    unit = canonical_unit()
    unit["confidence"] = 2.0
    unit["provenance"] = []
    errors = validate(unit)
    assert len(errors) >= 2  # explainability: report everything, not just the first


def test_registry_helpers():
    assert conforms_to_naming_rule("PERSON_BEHAVIOR_RISK")
    assert not conforms_to_naming_rule("bad_name")
    assert is_personal("PERSON_NAME")
    assert not is_personal("ECON_INDICATOR")


def test_original_unit_not_mutated_by_validation():
    unit = canonical_unit()
    snapshot = copy.deepcopy(unit)
    validate(unit)
    assert unit == snapshot  # validation observes, never transforms
