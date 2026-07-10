"""Banco Central do Brasil SGS ingestion — first live RFC-0014 pipeline
(RFC-0020 draft).

Fetches declared official series, normalizes them into canonical
ECON_INDICATOR units, and refuses to store anything that fails strict
validation. Registry entry: ingestion/SOURCE-REGISTRY.md (bcb-sgs-*).
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import urllib.request

from ..schema import validate
from ..units import build_unit

ENGINE = {"id": "INGEST-BCB", "version": "0.1.0"}

# Official source; still a parameter, not a claim of truth.
CONFIDENCE = 0.95

REGION = "BR"  # national level; FE-005 hierarchical matching pairs BR with BR-*

# Declared series (ingestion/SOURCE-REGISTRY.md). Registry changes are Class 2.
SERIES: dict[int, str] = {
    432: "interest_rate",   # Meta Selic, % a.a.
    433: "inflation",       # IPCA, monthly variation %
    1: "exchange_rate",     # USD/BRL
}

# The single-item endpoint proved flaky in live verification (2026-07-09):
# request a small window and take the most recent observation.
FETCH_WINDOW = 5
API = (
    "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados/"
    "ultimos/{window}?formato=json"
)

SOURCE_TRADITION = "official statistical source (Banco Central do Brasil, SGS)"


def parameters_hash() -> str:
    payload = {
        "engine": ENGINE,
        "series": {str(k): v for k, v in SERIES.items()},
        "region": REGION,
        "confidence": CONFIDENCE,
        "fetch_window": FETCH_WINDOW,
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()


def fetch_latest(code: int) -> list[dict]:
    request = urllib.request.Request(
        API.format(code=code, window=FETCH_WINDOW),
        headers={"User-Agent": "secm-protocol-ingestion/0.1"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    if not isinstance(payload, list) or not payload:
        raise RuntimeError(f"SGS {code}: unexpected payload shape: {payload!r}")
    return payload


def to_unit(code: int, observation: dict) -> dict:
    indicator = SERIES[code]
    # SGS returns decimals with dot ("5.1329") but be tolerant of comma locales.
    value = float(str(observation["valor"]).replace(",", "."))
    return build_unit(
        semantic_type="ECON_INDICATOR",
        entity_ref=f"graph:place:{REGION}",
        engine=ENGINE,
        value={
            "indicator": indicator,
            "value": value,
            "region": REGION,
            "series": code,
            "reference_date": observation["data"],
        },
        confidence=CONFIDENCE,
        provenance=[f"source-registry:bcb-sgs-{code}"],
        transformation_name="bcb-sgs-ingestion",
        transformation_description=(
            "fetches the most recent observation of a declared BCB SGS series "
            "and normalizes it into a canonical unit (RFC-0020 v0.1)"
        ),
        source_tradition=SOURCE_TRADITION,
        parameters_hash=parameters_hash(),
    )


def run(fetch=fetch_latest) -> list[dict]:
    """Ingest all declared series. An invalid unit aborts the whole run:
    nothing unvalidated is ever stored (RFC-0020 validation gate)."""
    units = []
    for code in SERIES:
        observations = fetch(code)
        unit = to_unit(code, observations[-1])
        errors = validate(unit, strict_registry=True)
        if errors:
            raise RuntimeError(f"SGS {code}: unit failed validation: {errors}")
        units.append(unit)
    return units


def main() -> None:
    units = run()
    repo_root = pathlib.Path(__file__).resolve().parents[4]
    out_dir = repo_root / "data" / "environment"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "bcb-latest.json"
    out_file.write_text(json.dumps(units, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"ingested {len(units)} validated units -> {out_file}")


if __name__ == "__main__":
    main()
