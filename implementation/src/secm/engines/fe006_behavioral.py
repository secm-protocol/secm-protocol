"""FE-006 Behavioral System — RFC-0016 v0.1.

Deterministic ordinal axis mapping of the RX behavioral answers (Q7-Q9).
Self-report is E0 evidence: confidence is capped at the baseline until
FE-008 calibration earns more (RFC-0001 §6).
"""

from __future__ import annotations

import hashlib
import json

from ..units import build_unit

ENGINE = {"id": "FE-006", "version": "0.1.0"}

# E0 self-report baseline (RFC-0016 parameter).
BASELINE_CONFIDENCE = 0.55

# RFC-0016 mapping table v0.1 — option order follows RFC-0011 Q7-Q9.
AXES: dict[str, tuple[str, tuple[str, str, str, str]]] = {
    "PERSON_BEHAVIOR_DECISION": (
        "decision_latency",
        ("instinct", "data-seeking", "consultative", "postponing"),
    ),
    "PERSON_BEHAVIOR_RISK": (
        "risk_appetite",
        ("risk-seeking", "calculated", "stability-first", "risk-averse"),
    ),
    "PERSON_BEHAVIOR_HORIZON": (
        "planning_horizon",
        ("day-to-day", "weeks-months", "1-3-years", "5-plus-years"),
    ),
}

_POSITIONS = (0.0, round(1 / 3, 4), round(2 / 3, 4), 1.0)

SOURCE_TRADITION = "behavioral self-report, structured questionnaire"


def parameters_hash() -> str:
    """sha256 of the mapping table — changing the table changes the hash forever."""
    payload = {
        "engine": ENGINE,
        "baseline_confidence": BASELINE_CONFIDENCE,
        "positions": _POSITIONS,
        "axes": {k: {"axis": a, "labels": list(l)} for k, (a, l) in AXES.items()},
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()


def encode(units: list[dict]) -> list[dict]:
    """Transform RX behavioral answer units into axis units + composite profile.

    Emits only for answered axes; composite confidence scales with coverage
    (RFC-0016). Never sees identity — inputs are semantic units only.
    """
    phash = parameters_hash()
    axis_units: list[dict] = []

    for unit in units:
        semantic_type = unit.get("semantic_type")
        if semantic_type not in AXES:
            continue
        idx = (unit.get("value") or {}).get("option_index")
        if not isinstance(idx, int) or isinstance(idx, bool) or not 0 <= idx <= 3:
            raise ValueError(
                f"{semantic_type}: value.option_index must be an integer 0..3 "
                "(RFC-0011 option order)"
            )
        axis, labels = AXES[semantic_type]
        axis_units.append(
            build_unit(
                semantic_type=semantic_type,
                entity_ref=unit["entity_ref"],
                engine=ENGINE,
                value={"axis": axis, "position": _POSITIONS[idx], "label": labels[idx]},
                confidence=BASELINE_CONFIDENCE,
                provenance=[unit["id"]],
                transformation_name=f"behavioral-axis-encoding:{axis}",
                transformation_description=(
                    f"maps the RX categorical answer onto the '{axis}' ordinal "
                    "axis, v0.1 mapping table (RFC-0016)"
                ),
                source_tradition=SOURCE_TRADITION,
                parameters_hash=phash,
                consent_scope=unit.get("consent_scope"),
            )
        )

    outputs = list(axis_units)
    if axis_units:
        coverage = len(axis_units) / len(AXES)
        outputs.append(
            build_unit(
                semantic_type="PERSON_BEHAVIOR_PROFILE",
                entity_ref=axis_units[0]["entity_ref"],
                engine=ENGINE,
                value={
                    "axes": {
                        au["value"]["axis"]: {
                            "position": au["value"]["position"],
                            "label": au["value"]["label"],
                        }
                        for au in axis_units
                    },
                    "coverage": round(coverage, 4),
                },
                confidence=BASELINE_CONFIDENCE * coverage,
                provenance=[au["id"] for au in axis_units],
                transformation_name="behavioral-profile-composition",
                transformation_description=(
                    "composes answered behavioral axes into one profile; "
                    "confidence scales with coverage (RFC-0016)"
                ),
                source_tradition=SOURCE_TRADITION,
                parameters_hash=phash,
                consent_scope=axis_units[0].get("consent_scope"),
            )
        )
    return outputs
