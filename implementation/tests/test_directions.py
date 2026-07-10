"""RFC-0021 validation suite — directional hypotheses v0.2.

Uses the RX-000001 configuration (the real first RX) as the primary vector:
this feature exists because that reading answered nothing.
"""

from secm import validate
from secm.core import cke
from secm.engines import fe005_context as fe005
from secm.engines import fe006_behavioral as fe006
from secm.solvers import directions, personal

from test_cke import person_unit


def env_unit_full(indicator: str, value: float) -> dict:
    import datetime, uuid

    return {
        "schema_version": "0.1.0",
        "id": str(uuid.uuid4()),
        "entity_ref": "graph:place:BR",
        "semantic_type": "ECON_INDICATOR",
        "engine": {"id": "INGEST-BCB", "version": "0.1.0"},
        "transformation": {
            "name": "bcb-sgs-ingestion",
            "description": "official indicator",
            "source_tradition": "official statistical source",
            "parameters_hash": "c" * 64,
        },
        "value": {"indicator": indicator, "value": value, "region": "BR"},
        "confidence": 0.95,
        "provenance": ["source-registry:bcb"],
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }


def rx_000001_estimation() -> dict:
    """The first real RX: finances/organize-recover, BR-Nordeste, technology,
    instinct + calculated + day-to-day, with today's three indicators."""
    person = [
        person_unit("PERSON_LOCATION_CURRENT", {"region": "BR-Nordeste"}),
        person_unit(
            "PERSON_FOCUS_DOMAIN", {"domain": "finances", "direction": "organize-recover"}
        ),
        person_unit("PERSON_OCCUPATION_FIELD", {"field": "technology"}),
    ]
    env = [
        env_unit_full("interest_rate", 14.25),
        env_unit_full("inflation", 0.58),
        env_unit_full("exchange_rate", 5.1329),
    ]
    behavioral = fe006.encode(
        [
            person_unit("PERSON_BEHAVIOR_DECISION", {"option_index": 0}),
            person_unit("PERSON_BEHAVIOR_RISK", {"option_index": 1}),
            person_unit("PERSON_BEHAVIOR_HORIZON", {"option_index": 0}),
        ]
    )
    composite = [u for u in behavioral if u["semantic_type"] == "PERSON_BEHAVIOR_PROFILE"]
    return cke.converge(fe005.profile(person, env) + composite)


def test_rx_000001_now_gets_ranked_directions():
    reading = personal.solve(rx_000001_estimation())
    hypotheses = reading["value"]["direction_hypotheses"]
    assert len(hypotheses) >= 3
    assert validate(reading, strict_registry=True) == []


def test_restructure_debt_ranks_first_and_bet_ranks_last():
    hypotheses = personal.solve(rx_000001_estimation())["value"]["direction_hypotheses"]
    assert hypotheses[0]["id"] == "H2-restructure-debt"
    assert hypotheses[-1]["id"] == "H4-high-risk-recovery-bet"
    assert hypotheses[-1]["net_score"] < 0


def test_every_hypothesis_cites_evidence_and_is_labeled_unvalidated():
    hypotheses = personal.solve(rx_000001_estimation())["value"]["direction_hypotheses"]
    for hypothesis in hypotheses:
        assert hypothesis["weight_basis"] == "expert-prior-unvalidated"
        assert hypothesis["evidence_for"] or hypothesis["evidence_against"], hypothesis["id"]
        for link in hypothesis["evidence_for"] + hypothesis["evidence_against"]:
            assert link["because"]


def test_hypothesis_confidence_never_exceeds_reading_confidence():
    reading = personal.solve(rx_000001_estimation())
    ceiling = reading["confidence"]
    for hypothesis in reading["value"]["direction_hypotheses"]:
        assert hypothesis["confidence"] <= ceiling


def test_indicator_interpretations_present():
    interpretations = personal.solve(rx_000001_estimation())["value"][
        "context_interpretations"
    ]
    by_indicator = {i["indicator"]: i for i in interpretations}
    assert by_indicator["interest_rate"]["level"] == "extreme"
    assert by_indicator["exchange_rate"]["level"] == "weak-brl"


def test_structural_risks_fire_for_rx_000001():
    risks = {r["id"] for r in personal.solve(rx_000001_estimation())["value"]["risk_exposures"]}
    assert "SR1-quick-recovery-schemes" in risks  # debt distress + technology field
    assert "SR2-revolving-credit-spiral" in risks  # debt distress + extreme rate
    assert "SR3-peak-rate-borrowing" in risks


def test_unknown_domain_says_so_honestly():
    person = [
        person_unit("PERSON_LOCATION_CURRENT", {"region": "BR-Nordeste"}),
        person_unit("PERSON_FOCUS_DOMAIN", {"domain": "relationships", "direction": "personal"}),
    ]
    behavioral = fe006.encode([person_unit("PERSON_BEHAVIOR_RISK", {"option_index": 1})])
    composite = [u for u in behavioral if u["semantic_type"] == "PERSON_BEHAVIOR_PROFILE"]
    reading = personal.solve(cke.converge(fe005.profile(person) + composite))
    assert reading["value"]["direction_hypotheses"] == []
    assert any("No decision space exists yet" in s["text"] for s in reading["value"]["statements"])
    assert validate(reading, strict_registry=True) == []


def test_determinism():
    estimation = rx_000001_estimation()
    assert (
        personal.solve(estimation)["value"]["direction_hypotheses"]
        == personal.solve(estimation)["value"]["direction_hypotheses"]
    )


def test_calculated_risk_opposes_the_bet_explicitly():
    hypotheses = personal.solve(rx_000001_estimation())["value"]["direction_hypotheses"]
    bet = next(h for h in hypotheses if h["id"] == "H4-high-risk-recovery-bet")
    against_conditions = {link["condition"] for link in bet["evidence_against"]}
    assert "risk_calculated" in against_conditions
    assert "rate_extreme" in against_conditions
