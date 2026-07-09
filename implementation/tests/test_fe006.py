"""RFC-0016 validation suite — FE-006 Behavioral System v0.1."""

import uuid

import pytest

from secm import validate
from secm.engines import fe006_behavioral as fe006


def intake_unit(semantic_type: str, option_index: int) -> dict:
    return {
        "schema_version": "0.1.0",
        "id": str(uuid.uuid4()),
        "entity_ref": "graph:person:anonymous-1",
        "semantic_type": semantic_type,
        "engine": {"id": "rx-intake", "version": "0.1.0"},
        "transformation": {
            "name": "rx-intake-capture",
            "description": "captures a categorical RX answer",
            "source_tradition": "structured questionnaire",
            "parameters_hash": "b" * 64,
        },
        "value": {"option_index": option_index},
        "confidence": 1.0,
        "provenance": ["descriptor:rx-intake:v0.1"],
        "created_at": "2026-07-09T12:00:00+00:00",
        "consent_scope": "consent:v1:rx-analysis",
    }


def full_intake() -> list[dict]:
    return [
        intake_unit("PERSON_BEHAVIOR_DECISION", 0),
        intake_unit("PERSON_BEHAVIOR_RISK", 1),
        intake_unit("PERSON_BEHAVIOR_HORIZON", 3),
    ]


def test_full_intake_yields_three_axes_plus_composite():
    out = fe006.encode(full_intake())
    assert len(out) == 4
    assert out[-1]["semantic_type"] == "PERSON_BEHAVIOR_PROFILE"


def test_all_outputs_validate_strict():
    for unit in fe006.encode(full_intake()):
        assert validate(unit, strict_registry=True) == [], unit["semantic_type"]


def test_mapping_positions_and_labels():
    out = fe006.encode(full_intake())
    by_axis = {u["value"]["axis"]: u["value"] for u in out[:-1]}
    assert by_axis["decision_latency"] == {
        "axis": "decision_latency", "position": 0.0, "label": "instinct",
    }
    assert by_axis["risk_appetite"]["label"] == "calculated"
    assert by_axis["planning_horizon"] == {
        "axis": "planning_horizon", "position": 1.0, "label": "5-plus-years",
    }


def test_composite_confidence_scales_with_coverage():
    full = fe006.encode(full_intake())
    assert full[-1]["confidence"] == fe006.BASELINE_CONFIDENCE
    partial = fe006.encode(full_intake()[:2])
    assert len(partial) == 3
    assert partial[-1]["confidence"] == round(fe006.BASELINE_CONFIDENCE * 2 / 3, 4)
    assert partial[-1]["value"]["coverage"] == round(2 / 3, 4)


def test_no_answers_yields_nothing():
    assert fe006.encode([]) == []
    assert fe006.encode([intake_unit("PERSON_FOCUS_DOMAIN", 1)]) == []


def test_bad_option_index_raises():
    for bad in (-1, 4, "2", None, True):
        unit = intake_unit("PERSON_BEHAVIOR_RISK", 0)
        unit["value"]["option_index"] = bad
        with pytest.raises(ValueError):
            fe006.encode([unit])


def test_determinism_of_value_payloads():
    inputs = full_intake()
    first = [u["value"] for u in fe006.encode(inputs)]
    second = [u["value"] for u in fe006.encode(inputs)]
    assert first == second


def test_provenance_and_consent_propagation():
    inputs = full_intake()
    out = fe006.encode(inputs)
    input_ids = {u["id"] for u in inputs}
    for axis_unit in out[:-1]:
        assert set(axis_unit["provenance"]) <= input_ids
        assert axis_unit["consent_scope"] == "consent:v1:rx-analysis"
    composite = out[-1]
    assert set(composite["provenance"]) == {u["id"] for u in out[:-1]}


def test_confidence_never_exceeds_baseline():
    for unit in fe006.encode(full_intake()):
        assert unit["confidence"] <= fe006.BASELINE_CONFIDENCE


def test_parameters_hash_is_stable_sha256():
    assert fe006.parameters_hash() == fe006.parameters_hash()
    assert len(fe006.parameters_hash()) == 64
