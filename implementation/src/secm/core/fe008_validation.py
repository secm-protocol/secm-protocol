"""FE-008 Validation Engine — minimal loop v0.1 (RFC-0018 draft).

Registers real-world outcomes against directional estimations and measures
confidence calibration. v0.1 measures only: it never recalibrates weights,
because recalibration without sufficient data would be fake science.
"""

from __future__ import annotations

import hashlib
import json

from ..units import build_unit

ENGINE = {"id": "FE-008", "version": "0.1.0"}

MIN_SAMPLE = 30

# RFC-0000 §17 triad — never merged.
OUTCOME_TYPES = ("subjective_perception", "objective_outcome", "observed_evidence")

# E2/E3 are earned by statistical validation, never declared at registration.
REGISTRATION_TIERS = ("E0", "E1")

SOURCE_TRADITION = "outcome registration and calibration measurement"


def parameters_hash() -> str:
    payload = {
        "engine": ENGINE,
        "min_sample": MIN_SAMPLE,
        "outcome_types": OUTCOME_TYPES,
        "registration_tiers": REGISTRATION_TIERS,
        "score": "brier",
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()


def register_outcome(
    estimation: dict,
    *,
    outcome_type: str,
    evidence_tier: str,
    success: bool,
    note: str = "",
) -> dict:
    """Create a PROTOCOL_OUTCOME unit linked to an estimation."""
    if outcome_type not in OUTCOME_TYPES:
        raise ValueError(
            f"outcome_type must be one of {OUTCOME_TYPES} (RFC-0000 §17)"
        )
    if evidence_tier not in REGISTRATION_TIERS:
        raise ValueError(
            "evidence_tier at registration must be E0 or E1 - E2/E3 are earned "
            "by statistical validation, never declared (RFC-0018)"
        )
    if not isinstance(success, bool):
        raise ValueError("result.success must be boolean in v0.1")
    consent = estimation.get("consent_scope")
    if not consent:
        raise ValueError(
            "outcomes derived from personal estimations must carry the "
            "estimation's consent_scope (precedence rank 1)"
        )
    return build_unit(
        semantic_type="PROTOCOL_OUTCOME",
        entity_ref=estimation["entity_ref"],
        engine=ENGINE,
        value={
            "estimation_ref": estimation["id"],
            "outcome_type": outcome_type,
            "evidence_tier": evidence_tier,
            "result": {"success": success, "note": note},
        },
        confidence=1.0 if evidence_tier == "E1" else 0.5,
        provenance=[estimation["id"]],
        transformation_name="outcome-registration",
        transformation_description=(
            "records a real-world outcome against a directional estimation "
            "(RFC-0018 v0.1)"
        ),
        source_tradition=SOURCE_TRADITION,
        parameters_hash=parameters_hash(),
        consent_scope=consent,
    )


def brier_score(pairs: list[tuple[float, bool]]) -> float:
    """Mean of (confidence - outcome)^2; 0.0 is perfect, 0.25 is coin-flip level."""
    if not pairs:
        raise ValueError("brier_score requires at least one (confidence, success) pair")
    return sum((c - (1.0 if s else 0.0)) ** 2 for c, s in pairs) / len(pairs)


def calibration_report(estimations: list[dict], outcomes: list[dict]) -> dict:
    """Measure calibration over matched estimation/outcome pairs.

    Below MIN_SAMPLE the report itself says no conclusion may be drawn.
    """
    by_id = {e["id"]: e for e in estimations}
    pairs: list[tuple[float, bool]] = []
    matched_outcomes: list[dict] = []
    for outcome in outcomes:
        ref = (outcome.get("value") or {}).get("estimation_ref")
        estimation = by_id.get(ref)
        if estimation is None:
            continue
        pairs.append(
            (float(estimation["confidence"]), outcome["value"]["result"]["success"])
        )
        matched_outcomes.append(outcome)

    sample_size = len(pairs)
    status = "measured" if sample_size >= MIN_SAMPLE else "insufficient-data"
    value = {
        "sample_size": sample_size,
        "min_sample": MIN_SAMPLE,
        "status": status,
        "brier_score": round(brier_score(pairs), 4) if pairs else None,
        "mean_confidence": round(sum(c for c, _ in pairs) / sample_size, 4)
        if pairs
        else None,
        "outcome_rate": round(sum(1 for _, s in pairs if s) / sample_size, 4)
        if pairs
        else None,
        "recalibration": "not-implemented-in-v0.1",
    }
    return build_unit(
        semantic_type="PROTOCOL_CALIBRATION_REPORT",
        entity_ref="graph:protocol:calibration",
        engine=ENGINE,
        value=value,
        confidence=1.0,  # the report certainly states what it measured
        provenance=[o["id"] for o in matched_outcomes]
        or ["descriptor:fe008:empty-outcome-set"],
        transformation_name="calibration-measurement",
        transformation_description=(
            "Brier-score calibration over matched estimation/outcome pairs; "
            "explicit insufficient-data status below the minimum sample "
            "(RFC-0018 v0.1)"
        ),
        source_tradition=SOURCE_TRADITION,
        parameters_hash=parameters_hash(),
    )
