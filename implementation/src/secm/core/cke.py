"""CKE — Convergence Knowledge Engine, minimal v0.1 (RFC-0017).

The heart of SECM (RFC-0000 §13): never trusts a single engine, searches
for convergence. Two constitutional honesty rules govern this code:

1. Weights are earned, and nothing is earned yet — every estimation carries
   the "uniform-prior-unvalidated" label until FE-008 calibration exists.
2. Convergence cannot manufacture certainty — estimation confidence never
   exceeds its strongest component, and is protocol-capped below 1.0.
"""

from __future__ import annotations

import hashlib
import json

from ..units import build_unit

ENGINE = {"id": "CKE", "version": "0.1.0"}

EXPECTED_ENGINES = ("FE-005", "FE-006")
UNIFORM_PRIOR_WEIGHT = 1.0
WEIGHT_BASIS = "uniform-prior-unvalidated"
ENVIRONMENT_GAP_FACTOR = 0.85
CONFIDENCE_CEILING = 0.95

SOURCE_TRADITION = "cross-engine evidence convergence"


def parameters_hash() -> str:
    payload = {
        "engine": ENGINE,
        "expected_engines": EXPECTED_ENGINES,
        "uniform_prior_weight": UNIFORM_PRIOR_WEIGHT,
        "weight_basis": WEIGHT_BASIS,
        "environment_gap_factor": ENVIRONMENT_GAP_FACTOR,
        "confidence_ceiling": CONFIDENCE_CEILING,
        "method": "weighted-evidence-bundle",
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()


def converge(units: list[dict]) -> dict:
    """Converge slice-engine outputs into one directional estimation unit.

    Requires the FE-005 PERSON_CONTEXT profile unit — it carries the question.
    Units from engines outside EXPECTED_ENGINES are ignored (Zero Trust).
    """
    consumed: list[dict] = []
    signal_units: list[dict] = []
    annotations: dict = {}
    profile_unit: dict | None = None

    for unit in units:
        engine_id = (unit.get("engine") or {}).get("id")
        if engine_id not in EXPECTED_ENGINES:
            continue
        consumed.append(unit)
        value = unit.get("value") or {}
        if "environment_coverage" in value:
            # Absence honestly stated is meta-information, never a signal:
            # its 1.0 confidence would raise the mean - exactly backwards.
            annotations["environment_coverage"] = value["environment_coverage"]
            continue
        if engine_id == "FE-005" and "profile" in value and profile_unit is None:
            profile_unit = unit
        signal_units.append(unit)

    if profile_unit is None:
        raise ValueError(
            "CKE requires the FE-005 PERSON_CONTEXT profile unit - no estimation "
            "without a question (RFC-0017)"
        )

    profile = profile_unit["value"]["profile"]
    question = {
        "focus_domain": profile.get("focus_domain"),
        "direction": profile.get("direction"),
    }

    signals = []
    weighted_sum = 0.0
    weight_total = 0.0
    strongest_component = 0.0
    for unit in signal_units:
        weight = UNIFORM_PRIOR_WEIGHT
        unit_confidence = float(unit["confidence"])
        weighted_sum += weight * unit_confidence
        weight_total += weight
        strongest_component = max(strongest_component, unit_confidence)
        signals.append(
            {
                "source_engine": unit["engine"]["id"],
                "semantic_type": unit["semantic_type"],
                "observation": unit["value"],
                "unit_confidence": unit_confidence,
                "engine_weight": {"value": weight, "basis": WEIGHT_BASIS},
                "provenance_ref": unit["id"],
            }
        )

    contributing = sorted({u["engine"]["id"] for u in consumed})
    coverage_factor = len(contributing) / len(EXPECTED_ENGINES)

    confidence = (weighted_sum / weight_total) * coverage_factor
    if annotations.get("environment_coverage") == "none":
        confidence *= ENVIRONMENT_GAP_FACTOR
    confidence = min(confidence, strongest_component, CONFIDENCE_CEILING)

    consent = next(
        (u.get("consent_scope") for u in signal_units if u.get("consent_scope")), None
    )
    return build_unit(
        semantic_type="PERSON_DIRECTIONAL_ESTIMATION",
        entity_ref=profile_unit["entity_ref"],
        engine=ENGINE,
        value={
            "question": question,
            "signals": signals,
            "convergence": {
                "method": "weighted-evidence-bundle",
                "engine_weights": {
                    engine_id: {"value": UNIFORM_PRIOR_WEIGHT, "basis": WEIGHT_BASIS}
                    for engine_id in contributing
                },
                "coverage": {
                    "contributing": contributing,
                    "expected": list(EXPECTED_ENGINES),
                    "factor": round(coverage_factor, 4),
                },
                "annotations": annotations,
            },
        },
        confidence=confidence,
        provenance=[u["id"] for u in consumed],
        transformation_name="minimal-convergence",
        transformation_description=(
            "bundles slice-engine evidence into one explainable directional "
            "estimation; weighted mean with coverage and environment-gap "
            "factors, capped at the strongest component and the protocol "
            "ceiling (RFC-0017 v0.1)"
        ),
        source_tradition=SOURCE_TRADITION,
        parameters_hash=parameters_hash(),
        consent_scope=consent,
    )
