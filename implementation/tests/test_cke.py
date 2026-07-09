"""RFC-0017 validation suite — CKE minimal convergence v0.1.

Exercises the real pipeline: RX intake units -> FE-005 + FE-006 -> CKE.
"""

import datetime
import uuid

import pytest

from secm import validate
from secm.core import cke
from secm.engines import fe005_context as fe005
from secm.engines import fe006_behavioral as fe006


def person_unit(semantic_type: str, value: dict) -> dict:
    return {
        "schema_version": "0.1.0",
        "id": str(uuid.uuid4()),
        "entity_ref": "graph:person:anonymous-1",
        "semantic_type": semantic_type,
        "engine": {"id": "rx-intake", "version": "0.1.0"},
        "transformation": {
            "name": "rx-intake-capture",
            "description": "captures an RX answer",
            "source_tradition": "structured questionnaire",
            "parameters_hash": "b" * 64,
        },
        "value": value,
        "confidence": 1.0,
        "provenance": ["descriptor:rx-intake:v0.1"],
        "created_at": "2026-07-09T12:00:00+00:00",
        "consent_scope": "consent:v1:rx-analysis",
    }


def env_unit(indicator: str = "inflation") -> dict:
    return {
        "schema_version": "0.1.0",
        "id": str(uuid.uuid4()),
        "entity_ref": "graph:place:BR-Sudeste",
        "semantic_type": "ECON_INDICATOR",
        "engine": {"id": "ingestion", "version": "0.1.0"},
        "transformation": {
            "name": "indicator-ingestion",
            "description": "ingests an official regional indicator",
            "source_tradition": "official statistical source",
            "parameters_hash": "c" * 64,
        },
        "value": {"indicator": indicator, "value": 4.5, "region": "BR-Sudeste"},
        "confidence": 0.9,
        "provenance": ["source-registry:bcb:run-001"],
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }


def slice_outputs(*, with_environment: bool, behavioral_answers: int = 3) -> list[dict]:
    """Run the real engines and return their combined outputs."""
    fe005_inputs = [
        person_unit("PERSON_LOCATION_CURRENT", {"region": "BR-Sudeste"}),
        person_unit(
            "PERSON_FOCUS_DOMAIN", {"domain": "finances", "direction": "organize-recover"}
        ),
    ]
    env = [env_unit()] if with_environment else []
    context_units = fe005.profile(fe005_inputs, env)

    behavioral_intake = [
        person_unit("PERSON_BEHAVIOR_DECISION", {"option_index": 1}),
        person_unit("PERSON_BEHAVIOR_RISK", {"option_index": 1}),
        person_unit("PERSON_BEHAVIOR_HORIZON", {"option_index": 2}),
    ][:behavioral_answers]
    behavioral_units = fe006.encode(behavioral_intake)
    composite = [u for u in behavioral_units if u["semantic_type"] == "PERSON_BEHAVIOR_PROFILE"]
    return context_units + composite


def test_estimation_validates_strict_and_carries_question():
    estimation = cke.converge(slice_outputs(with_environment=True))
    assert validate(estimation, strict_registry=True) == []
    assert estimation["semantic_type"] == "PERSON_DIRECTIONAL_ESTIMATION"
    assert estimation["value"]["question"] == {
        "focus_domain": "finances",
        "direction": "organize-recover",
    }


def test_confidence_formula_full_coverage_with_environment():
    # signals: profile 0.8, pairing min(0.8,0.9)*1.0=0.8, behavioral composite 0.55
    estimation = cke.converge(slice_outputs(with_environment=True))
    expected = round(min((0.8 + 0.8 + 0.55) / 3, 0.8, cke.CONFIDENCE_CEILING), 4)
    assert estimation["confidence"] == expected


def test_environment_gap_penalty_applies():
    estimation = cke.converge(slice_outputs(with_environment=False))
    # signals: profile 0.8 + composite 0.55 (marker excluded); coverage 2/2
    expected = round(((0.8 + 0.55) / 2) * cke.ENVIRONMENT_GAP_FACTOR, 4)
    assert estimation["confidence"] == expected
    assert (
        estimation["value"]["convergence"]["annotations"]["environment_coverage"]
        == "none"
    )


def test_marker_is_annotation_not_signal():
    estimation = cke.converge(slice_outputs(with_environment=False))
    assert not any(
        "environment_coverage" in s["observation"] for s in estimation["value"]["signals"]
    )


def test_coverage_factor_penalizes_missing_engine():
    fe005_only = [
        u
        for u in slice_outputs(with_environment=True)
        if u["engine"]["id"] == "FE-005"
    ]
    estimation = cke.converge(fe005_only)
    assert estimation["value"]["convergence"]["coverage"]["factor"] == 0.5
    # base mean (0.8+0.8)/2=0.8, coverage 0.5 -> 0.4, under both caps
    assert estimation["confidence"] == round(0.8 * 0.5, 4)


def test_confidence_never_exceeds_strongest_component():
    estimation = cke.converge(slice_outputs(with_environment=True))
    strongest = max(s["unit_confidence"] for s in estimation["value"]["signals"])
    assert estimation["confidence"] <= strongest
    assert estimation["confidence"] <= cke.CONFIDENCE_CEILING


def test_weights_are_labeled_unvalidated():
    estimation = cke.converge(slice_outputs(with_environment=True))
    for signal in estimation["value"]["signals"]:
        assert signal["engine_weight"]["basis"] == "uniform-prior-unvalidated"
    for weight in estimation["value"]["convergence"]["engine_weights"].values():
        assert weight["basis"] == "uniform-prior-unvalidated"


def test_every_signal_provenance_resolves_to_consumed_unit():
    units = slice_outputs(with_environment=True)
    estimation = cke.converge(units)
    unit_ids = {u["id"] for u in units}
    for signal in estimation["value"]["signals"]:
        assert signal["provenance_ref"] in unit_ids
    assert set(estimation["provenance"]) == unit_ids


def test_foreign_engine_units_are_ignored():
    units = slice_outputs(with_environment=True)
    intruder = person_unit("PERSON_CONTEXT", {"profile": {"region": "X", "focus_domain": "career"}})
    intruder["engine"] = {"id": "UNKNOWN-ENGINE", "version": "9.9.9"}
    estimation = cke.converge(units + [intruder])
    assert intruder["id"] not in estimation["provenance"]


def test_missing_profile_raises():
    behavioral_only = [
        u for u in slice_outputs(with_environment=True) if u["engine"]["id"] == "FE-006"
    ]
    with pytest.raises(ValueError):
        cke.converge(behavioral_only)


def test_consent_propagates_to_estimation():
    estimation = cke.converge(slice_outputs(with_environment=True))
    assert estimation["consent_scope"] == "consent:v1:rx-analysis"


def test_determinism_of_value_payload():
    units = slice_outputs(with_environment=False)
    first = cke.converge(units)["value"]
    second = cke.converge(units)["value"]
    assert first == second
