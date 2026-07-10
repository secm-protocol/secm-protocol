"""RFC-0020 validation suite — BCB ingestion pipeline (offline)."""

import pytest

from secm import validate
from secm.engines import fe005_context as fe005
from secm.ingestion import bcb

from test_cke import person_unit


def fake_fetch(code: int) -> list[dict]:
    return {
        432: [{"data": "08/07/2026", "valor": "14.25"}],
        433: [{"data": "01/05/2026", "valor": "0,58"}],  # comma locale tolerated
        1: [{"data": "09/07/2026", "valor": "5.1329"}],
    }[code]


def test_run_produces_three_validated_units():
    units = bcb.run(fetch=fake_fetch)
    assert len(units) == 3
    for unit in units:
        assert validate(unit, strict_registry=True) == []
        assert unit["value"]["region"] == "BR"


def test_decimal_parsing_dot_and_comma():
    units = {u["value"]["indicator"]: u["value"]["value"] for u in bcb.run(fetch=fake_fetch)}
    assert units["interest_rate"] == 14.25
    assert units["inflation"] == 0.58
    assert units["exchange_rate"] == 5.1329


def test_indicator_names_are_consumable_by_fe005():
    relevant_names = set()
    for names in fe005.RELEVANCE_MAP.values():
        relevant_names.update(names)
    for indicator in bcb.SERIES.values():
        assert indicator in relevant_names, indicator


def test_validation_gate_aborts_run():
    def poisoned(code):
        return [{"data": "08/07/2026", "valor": "not-a-number"}]

    with pytest.raises(ValueError):
        bcb.run(fetch=poisoned)


def test_national_indicator_pairs_with_subregion():
    # FE-005 hierarchical region matching (RFC-0020 amendment): BR pairs BR-*.
    interest = next(
        u for u in bcb.run(fetch=fake_fetch) if u["value"]["indicator"] == "interest_rate"
    )
    outputs = fe005.profile(
        [
            person_unit("PERSON_LOCATION_CURRENT", {"region": "BR-Sudeste"}),
            person_unit(
                "PERSON_FOCUS_DOMAIN", {"domain": "finances", "direction": "organize-recover"}
            ),
        ],
        [interest],
    )
    pairings = [u for u in outputs if "pairing" in u["value"]]
    assert len(pairings) == 1
    assert pairings[0]["value"]["pairing"]["indicator"] == "interest_rate"


def test_unrelated_region_still_never_pairs():
    interest = next(
        u for u in bcb.run(fetch=fake_fetch) if u["value"]["indicator"] == "interest_rate"
    )
    outputs = fe005.profile(
        [
            person_unit("PERSON_LOCATION_CURRENT", {"region": "PT-Norte"}),
            person_unit(
                "PERSON_FOCUS_DOMAIN", {"domain": "finances", "direction": "organize-recover"}
            ),
        ],
        [interest],
    )
    assert not any("pairing" in u["value"] for u in outputs)
