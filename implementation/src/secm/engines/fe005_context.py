"""FE-005 Context System — RFC-0015 v0.1.

Builds the person-side context profile and pairs it with environment-side
units (RFC-0014 ingestion) when they exist. When the environment side is
empty, the engine says so explicitly — it never invents context.
"""

from __future__ import annotations

import datetime
import hashlib
import json

from ..units import build_unit

ENGINE = {"id": "FE-005", "version": "0.2.0"}  # 0.2.0: hierarchical region matching (RFC-0020)

# Structured self-declared facts baseline (RFC-0015 parameter).
PROFILE_CONFIDENCE = 0.8

# Relevance map v0.1 (RFC-0015): focus domain -> ECON indicator names.
# A versioned, benchmarkable parameter — never hardcoded belief.
RELEVANCE_MAP: dict[str, tuple[str, ...]] = {
    "career": ("unemployment_rate", "gdp_growth"),
    "business": ("gdp_growth", "interest_rate", "inflation"),
    "finances": ("inflation", "interest_rate", "exchange_rate"),
    "education": ("unemployment_rate",),
    "relationships": (),
    "relocation": ("gdp_growth", "unemployment_rate", "inflation"),
    "personal": (),
}

SOURCE_TRADITION = "contextual profiling, structured intake + declared public sources"

# RFC-0014 staleness rule, v0.1 factors.
_FRESHNESS_STEPS = ((180, 1.0), (540, 0.8))
_FRESHNESS_FLOOR = 0.5


def parameters_hash() -> str:
    payload = {
        "engine": ENGINE,
        "profile_confidence": PROFILE_CONFIDENCE,
        "relevance_map": {k: list(v) for k, v in RELEVANCE_MAP.items()},
        "freshness": {"steps": _FRESHNESS_STEPS, "floor": _FRESHNESS_FLOOR},
        "region_matching": "hierarchical-v1",
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()


def region_matches(env_region: str | None, person_region: str) -> bool:
    """Hierarchical region matching (RFC-0020): exact match, or a country-level
    indicator (e.g. 'BR') matches any of its sub-regions ('BR-Sudeste')."""
    if not env_region:
        return False
    return env_region == person_region or person_region.startswith(env_region + "-")


def freshness_factor(created_at: str, *, now: datetime.datetime | None = None) -> float:
    """Stale context widens uncertainty honestly (RFC-0014 §5)."""
    created = datetime.datetime.fromisoformat(created_at)
    now = now or datetime.datetime.now(datetime.timezone.utc)
    age_days = (now - created).days
    for max_days, factor in _FRESHNESS_STEPS:
        if age_days <= max_days:
            return factor
    return _FRESHNESS_FLOOR


def profile(person_units: list[dict], environment_units: list[dict] = ()) -> list[dict]:
    """Build the PERSON_CONTEXT profile, pairings, and the honest empty marker."""
    by_type: dict[str, dict] = {}
    for unit in person_units:
        by_type.setdefault(unit.get("semantic_type", ""), unit)

    location = by_type.get("PERSON_LOCATION_CURRENT")
    focus = by_type.get("PERSON_FOCUS_DOMAIN")
    if location is None or focus is None:
        raise ValueError(
            "FE-005 requires PERSON_LOCATION_CURRENT and PERSON_FOCUS_DOMAIN "
            "(guaranteed by RX Band 1, RFC-0011)"
        )

    region = (location.get("value") or {}).get("region")
    domain = (focus.get("value") or {}).get("domain")
    if not region or not domain:
        raise ValueError("region (bucketed) and focus domain are mandatory values")

    phash = parameters_hash()
    consumed = [location, focus]
    profile_value: dict = {
        "region": region,
        "focus_domain": domain,
        "direction": (focus.get("value") or {}).get("direction"),
    }

    occupation = by_type.get("PERSON_OCCUPATION_FIELD")
    if occupation is not None:
        profile_value["field"] = (occupation.get("value") or {}).get("field")
        consumed.append(occupation)
    birth_band = by_type.get("PERSON_BIRTH_DATE")  # Tier 0: only the band exists here
    if birth_band is not None:
        profile_value["age_band"] = (birth_band.get("value") or {}).get("age_band")
        consumed.append(birth_band)
    constraints = by_type.get("PERSON_CONSTRAINTS")
    if constraints is not None:
        profile_value["constraints"] = (constraints.get("value") or {}).get("constraints")
        consumed.append(constraints)

    consent = next(
        (u.get("consent_scope") for u in consumed if u.get("consent_scope")), None
    )
    profile_unit = build_unit(
        semantic_type="PERSON_CONTEXT",
        entity_ref=location["entity_ref"],
        engine=ENGINE,
        value={"profile": {k: v for k, v in profile_value.items() if v is not None}},
        confidence=PROFILE_CONFIDENCE,
        provenance=[u["id"] for u in consumed],
        transformation_name="context-profile-composition",
        transformation_description=(
            "normalizes bucketed person-side intake into one context profile "
            "(RFC-0015)"
        ),
        source_tradition=SOURCE_TRADITION,
        parameters_hash=phash,
        consent_scope=consent,
    )

    outputs = [profile_unit]
    relevant = RELEVANCE_MAP.get(domain, ())
    for env in environment_units:
        if env.get("semantic_type") != "ECON_INDICATOR":
            continue
        env_value = env.get("value") or {}
        if not region_matches(env_value.get("region"), region):
            continue
        if env_value.get("indicator") not in relevant:
            continue
        confidence = (
            min(PROFILE_CONFIDENCE, float(env.get("confidence", 0.0)))
            * freshness_factor(env["created_at"])
        )
        outputs.append(
            build_unit(
                semantic_type="PERSON_CONTEXT",
                entity_ref=location["entity_ref"],
                engine=ENGINE,
                value={
                    "pairing": {
                        "indicator": env_value.get("indicator"),
                        "indicator_value": env_value.get("value"),
                        "region": region,
                        "focus_domain": domain,
                    }
                },
                confidence=confidence,
                provenance=[profile_unit["id"], env["id"]],
                transformation_name="context-environment-pairing",
                transformation_description=(
                    "pairs the person context profile with a relevant regional "
                    "environment indicator (RFC-0015 relevance map v0.1)"
                ),
                source_tradition=SOURCE_TRADITION,
                parameters_hash=phash,
                consent_scope=consent,
            )
        )

    if len(outputs) == 1:
        outputs.append(
            build_unit(
                semantic_type="PERSON_CONTEXT",
                entity_ref=location["entity_ref"],
                engine=ENGINE,
                value={"environment_coverage": "none", "region": region},
                confidence=1.0,  # absence honestly stated is a certain fact
                provenance=[profile_unit["id"]],
                transformation_name="environment-coverage-marker",
                transformation_description=(
                    "states explicitly that no environment context exists for "
                    "this region, so downstream confidence drops for auditable "
                    "reasons (RFC-0015)"
                ),
                source_tradition=SOURCE_TRADITION,
                parameters_hash=phash,
                consent_scope=consent,
            )
        )
    return outputs
