"""RFC-0015 validation suite — FE-005 Context System v0.1."""

import datetime
import uuid

import pytest

from secm import validate
from secm.engines import fe005_context as fe005


def person_unit(semantic_type: str, value: dict) -> dict:
    return {
        "schema_version": "0.1.0",
        "id": str(uuid.uuid4()),
        "entity_ref": "graph:person:anonymous-1",
        "semantic_type": semantic_type,
        "engine": {"id": "rx-intake", "version": "0.1.0"},
        "transformation": {
            "name": "rx-intake-capture",
            "description": "captures a bucketed RX answer",
            "source_tradition": "structured questionnaire",
            "parameters_hash": "b" * 64,
        },
        "value": value,
        "confidence": 1.0,
        "provenance": ["descriptor:rx-intake:v0.1"],
        "created_at": "2026-07-09T12:00:00+00:00",
        "consent_scope": "consent:v1:rx-analysis",
    }


def env_unit(indicator: str, region: str = "BR-Sudeste", *, created_at: str | None = None) -> dict:
    return {
        "schema_version": "0.1.0",
        "id": str(uuid.uuid4()),
        "entity_ref": f"graph:place:{region}",
        "semantic_type": "ECON_INDICATOR",
        "engine": {"id": "ingestion", "version": "0.1.0"},
        "transformation": {
            "name": "indicator-ingestion",
            "description": "ingests an official regional indicator",
            "source_tradition": "official statistical source",
            "parameters_hash": "c" * 64,
        },
        "value": {"indicator": indicator, "value": 4.5, "region": region},
        "confidence": 0.9,
        "provenance": ["source-registry:bcb:run-001"],
        "created_at": created_at
        or datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }


def band1() -> list[dict]:
    return [
        person_unit("PERSON_LOCATION_CURRENT", {"region": "BR-Sudeste"}),
        person_unit("PERSON_FOCUS_DOMAIN", {"domain": "finances", "direction": "organize-recover"}),
    ]


def test_band1_yields_profile_plus_honest_empty_marker():
    out = fe005.profile(band1())
    assert len(out) == 2
    profile, marker = out
    assert profile["value"]["profile"]["region"] == "BR-Sudeste"
    assert profile["confidence"] == fe005.PROFILE_CONFIDENCE
    assert marker["value"]["environment_coverage"] == "none"
    assert marker["confidence"] == 1.0


def test_all_outputs_validate_strict():
    outputs = fe005.profile(band1(), [env_unit("inflation")])
    for unit in outputs:
        assert validate(unit, strict_registry=True) == []


def test_relevant_fresh_indicator_produces_pairing():
    out = fe005.profile(band1(), [env_unit("inflation")])
    pairings = [u for u in out if "pairing" in u["value"]]
    assert len(pairings) == 1
    pairing = pairings[0]
    assert pairing["value"]["pairing"]["indicator"] == "inflation"
    assert pairing["confidence"] == round(min(0.8, 0.9) * 1.0, 4)
    assert not any("environment_coverage" in u["value"] for u in out)


def test_irrelevant_indicator_is_ignored_marker_returns():
    # unemployment_rate is not in the finances relevance set
    out = fe005.profile(band1(), [env_unit("unemployment_rate")])
    assert not any("pairing" in u["value"] for u in out)
    assert any(u["value"].get("environment_coverage") == "none" for u in out)


def test_wrong_region_is_ignored():
    out = fe005.profile(band1(), [env_unit("inflation", region="BR-Norte")])
    assert not any("pairing" in u["value"] for u in out)


def test_stale_environment_lowers_confidence():
    stale = env_unit("inflation", created_at="2024-01-01T00:00:00+00:00")
    out = fe005.profile(band1(), [stale])
    pairing = next(u for u in out if "pairing" in u["value"])
    assert pairing["confidence"] == round(0.8 * 0.5, 4)


def test_optional_inputs_enrich_profile():
    units = band1() + [
        person_unit("PERSON_OCCUPATION_FIELD", {"field": "technology"}),
        person_unit("PERSON_BIRTH_DATE", {"age_band": "35-44"}),  # Tier 0: band only
    ]
    profile = fe005.profile(units)[0]["value"]["profile"]
    assert profile["field"] == "technology"
    assert profile["age_band"] == "35-44"


def test_missing_band1_inputs_raise():
    with pytest.raises(ValueError):
        fe005.profile([person_unit("PERSON_FOCUS_DOMAIN", {"domain": "finances"})])
    with pytest.raises(ValueError):
        fe005.profile([person_unit("PERSON_LOCATION_CURRENT", {"region": "BR-Sudeste"})])


def test_privacy_no_precise_location_or_age_in_outputs():
    units = band1() + [person_unit("PERSON_BIRTH_DATE", {"age_band": "35-44"})]
    for unit in fe005.profile(units, [env_unit("inflation")]):
        serialized = str(unit["value"])
        assert "birth" not in serialized.lower()
        for forbidden_key in ("city", "exact", "date"):
            assert forbidden_key not in unit["value"].get("profile", {})


def test_freshness_factor_steps():
    now = datetime.datetime(2026, 7, 9, tzinfo=datetime.timezone.utc)
    assert fe005.freshness_factor("2026-06-01T00:00:00+00:00", now=now) == 1.0
    assert fe005.freshness_factor("2025-06-01T00:00:00+00:00", now=now) == 0.8
    assert fe005.freshness_factor("2024-01-01T00:00:00+00:00", now=now) == 0.5


def test_determinism_of_value_payloads():
    inputs = band1()
    env = [env_unit("inflation", created_at="2026-07-01T00:00:00+00:00")]
    first = [u["value"] for u in fe005.profile(inputs, env)]
    second = [u["value"] for u in fe005.profile(inputs, env)]
    assert first == second
