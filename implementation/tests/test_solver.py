"""RFC-0019 validation suite — Personal Solver v0.1.

Uses the real pipeline (intake -> engines -> CKE) to build estimations.
"""

from secm import validate
from secm.core import cke
from secm.solvers import personal

from test_cke import slice_outputs


def make_estimation(*, with_environment: bool = True) -> dict:
    return cke.converge(slice_outputs(with_environment=with_environment))


def test_reading_validates_strict_and_inherits_confidence():
    estimation = make_estimation()
    reading = personal.solve(estimation)
    assert validate(reading, strict_registry=True) == []
    assert reading["semantic_type"] == "PERSON_DIRECTIONAL_READING"
    assert reading["confidence"] == estimation["confidence"]
    assert reading["value"]["confidence"]["score"] == estimation["confidence"]


def test_disclaimer_always_present():
    for with_env in (True, False):
        reading = personal.solve(make_estimation(with_environment=with_env))
        assert "never determines destiny" in reading["value"]["disclaimer"]


def test_every_statement_cites_resolvable_evidence():
    estimation = make_estimation()
    valid_refs = {s["provenance_ref"] for s in estimation["value"]["signals"]}
    valid_refs.add(estimation["id"])
    reading = personal.solve(estimation)
    assert reading["value"]["statements"], "a reading must say something"
    for statement in reading["value"]["statements"]:
        assert statement["based_on"], statement["text"]
        assert set(statement["based_on"]) <= valid_refs


def test_alignment_rule_r1_fires_for_measured_long_pattern():
    # slice_outputs uses risk 'calculated' + horizon '1-3-years' -> R1
    reading = personal.solve(make_estimation())
    rule_ids = [s.get("rule_id") for s in reading["value"]["statements"] if "rule_id" in s]
    assert "R1-long-horizon-measured-risk" in rule_ids


def test_environment_absence_is_stated():
    reading = personal.solve(make_estimation(with_environment=False))
    texts = " ".join(s["text"] for s in reading["value"]["statements"])
    assert "No regional environment data was available" in texts


def test_unvalidated_prior_reason_always_present():
    reading = personal.solve(make_estimation())
    assert any(
        "unvalidated uniform prior" in reason
        for reason in reading["value"]["confidence"]["reasons"]
    )


def test_confidence_band_wording():
    assert personal._band(0.2) == "low"
    assert personal._band(0.5) == "moderate-low"
    assert personal._band(0.7) == "moderate"
    assert personal._band(0.9) == "relatively high (still a hypothesis)"


def test_determinism_of_reading_payload():
    estimation = make_estimation()
    assert personal.solve(estimation)["value"] == personal.solve(estimation)["value"]
