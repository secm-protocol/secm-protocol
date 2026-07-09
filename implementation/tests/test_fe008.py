"""RFC-0018 validation suite — FE-008 minimal validation loop v0.1."""

import uuid

import pytest

from secm import validate
from secm.core import fe008_validation as fe008


def estimation_stub(confidence: float = 0.6) -> dict:
    return {
        "id": str(uuid.uuid4()),
        "entity_ref": "graph:person:anonymous-1",
        "semantic_type": "PERSON_DIRECTIONAL_ESTIMATION",
        "confidence": confidence,
        "consent_scope": "consent:v1:rx-analysis",
    }


def test_outcome_unit_validates_strict():
    outcome = fe008.register_outcome(
        estimation_stub(),
        outcome_type="objective_outcome",
        evidence_tier="E1",
        success=True,
        note="documented result",
    )
    assert validate(outcome, strict_registry=True) == []
    assert outcome["value"]["result"]["success"] is True


def test_declared_tiers_are_capped_at_e1():
    for forbidden in ("E2", "E3", "e1", ""):
        with pytest.raises(ValueError):
            fe008.register_outcome(
                estimation_stub(),
                outcome_type="objective_outcome",
                evidence_tier=forbidden,
                success=True,
            )


def test_outcome_type_triad_enforced():
    with pytest.raises(ValueError):
        fe008.register_outcome(
            estimation_stub(),
            outcome_type="feeling",
            evidence_tier="E0",
            success=True,
        )


def test_consent_is_mandatory():
    estimation = estimation_stub()
    del estimation["consent_scope"]
    with pytest.raises(ValueError):
        fe008.register_outcome(
            estimation, outcome_type="objective_outcome", evidence_tier="E1", success=True
        )


def test_boolean_success_enforced():
    with pytest.raises(ValueError):
        fe008.register_outcome(
            estimation_stub(),
            outcome_type="objective_outcome",
            evidence_tier="E1",
            success="yes",
        )


def test_brier_score_hand_computed_vectors():
    assert fe008.brier_score([(1.0, True)]) == 0.0
    assert fe008.brier_score([(1.0, False)]) == 1.0
    assert fe008.brier_score([(0.5, True), (0.5, False)]) == 0.25
    assert round(fe008.brier_score([(0.8, True), (0.6, False)]), 4) == round(
        ((0.2**2) + (0.6**2)) / 2, 4
    )
    with pytest.raises(ValueError):
        fe008.brier_score([])


def test_report_insufficient_data_below_minimum():
    estimations = [estimation_stub() for _ in range(3)]
    outcomes = [
        fe008.register_outcome(
            e, outcome_type="objective_outcome", evidence_tier="E1", success=True
        )
        for e in estimations
    ]
    report = fe008.calibration_report(estimations, outcomes)
    assert validate(report, strict_registry=True) == []
    assert report["value"]["status"] == "insufficient-data"
    assert report["value"]["sample_size"] == 3
    assert report["value"]["recalibration"] == "not-implemented-in-v0.1"


def test_report_status_flips_exactly_at_minimum():
    estimations = [estimation_stub(0.6) for _ in range(fe008.MIN_SAMPLE)]
    outcomes = [
        fe008.register_outcome(
            e, outcome_type="observed_evidence", evidence_tier="E1", success=(i % 2 == 0)
        )
        for i, e in enumerate(estimations)
    ]
    measured = fe008.calibration_report(estimations, outcomes)
    assert measured["value"]["status"] == "measured"
    short = fe008.calibration_report(estimations[:-1], outcomes[:-1])
    assert short["value"]["status"] == "insufficient-data"


def test_unmatched_outcomes_are_ignored():
    estimation = estimation_stub()
    outcome = fe008.register_outcome(
        estimation, outcome_type="objective_outcome", evidence_tier="E1", success=True
    )
    stranger = estimation_stub()
    report = fe008.calibration_report([stranger], [outcome])
    assert report["value"]["sample_size"] == 0
    assert report["value"]["brier_score"] is None
