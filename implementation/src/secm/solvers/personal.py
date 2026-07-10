"""Personal Solver v0.2 (RFC-0019 + RFC-0021 draft).

Translates one directional estimation into a human-readable reading that
ANSWERS the question: ranked directional hypotheses with for/against
evidence, indicator interpretations and structural risk exposures
(directions layer, RFC-0021) — plus the v0.1 declaration rendering.
Every claim cites its evidence; the constitutional disclaimer is
non-removable; confidence is inherited from the estimation, never higher.
"""

from __future__ import annotations

import hashlib
import json

from ..units import build_unit
from . import directions

ENGINE = {"id": "SOLVER-PERSONAL", "version": "0.2.0"}

SOURCE_TRADITION = "rule-based rendering of protocol estimations"

AXIS_HUMAN = {
    "decision_latency": "decision style under pressure",
    "risk_appetite": "risk posture",
    "planning_horizon": "planning horizon",
}

LABEL_HUMAN = {
    "instinct": "fast, by instinct",
    "data-seeking": "seeks more information first, even at the cost of delay",
    "consultative": "consults trusted people before moving",
    "postponing": "postpones until deciding becomes unavoidable",
    "risk-seeking": "drawn to risk, moves with partial safety",
    "calculated": "calculated - risks only after planning",
    "stability-first": "stability first - risks only when cornered",
    "risk-averse": "avoids risk whenever possible",
    "day-to-day": "lives day to day",
    "weeks-months": "weeks to a few months",
    "1-3-years": "keeps 1-3 year plans",
    "5-plus-years": "holds a 5+ year vision",
}

# Alignment rule table v0.1 - transparent IF-THEN entries, versioned in the
# parameters hash. Adding or changing a rule is Class 2 (RFC-0019).
ALIGNMENT_RULES: tuple[dict, ...] = (
    {
        "id": "R1-long-horizon-measured-risk",
        "when": {
            "planning_horizon": ("1-3-years", "5-plus-years"),
            "risk_appetite": ("calculated", "stability-first"),
        },
        "text": (
            "The declared pattern (long planning horizon + measured risk) is "
            "consistent with gradual, planned moves rather than abrupt changes."
        ),
    },
    {
        "id": "R2-short-horizon-high-risk",
        "when": {
            "planning_horizon": ("day-to-day", "weeks-months"),
            "risk_appetite": ("risk-seeking",),
        },
        "text": (
            "The declared pattern (short horizon + high risk appetite) is "
            "consistent with fast opportunistic moves - and with higher "
            "variance in results."
        ),
    },
    {
        "id": "R3-long-horizon-risk-averse",
        "when": {
            "planning_horizon": ("1-3-years", "5-plus-years"),
            "risk_appetite": ("risk-averse",),
        },
        "text": (
            "The declared pattern (long horizon + risk aversion) is consistent "
            "with slow, protected consolidation; opportunities requiring speed "
            "may pass by design."
        ),
    },
    {
        "id": "R4-postponing-decisions",
        "when": {"decision_latency": ("postponing",)},
        "text": (
            "Declared postponement under pressure is the single pattern most "
            "often in tension with any declared goal that has a deadline."
        ),
    },
)

DISCLAIMER = (
    "SECM estimates directions; it never determines destiny (RFC-0000 §2). "
    "This reading is a hypothesis built from your declarations and available "
    "context - not a verdict. Registering what actually happens is what makes "
    "future readings better."
)

_CONFIDENCE_BANDS = (
    (0.40, "low"),
    (0.60, "moderate-low"),
    (0.75, "moderate"),
    (1.01, "relatively high (still a hypothesis)"),
)


def parameters_hash() -> str:
    payload = {
        "engine": ENGINE,
        "axis_human": AXIS_HUMAN,
        "label_human": LABEL_HUMAN,
        "rules": ALIGNMENT_RULES,
        "bands": _CONFIDENCE_BANDS,
        "disclaimer": DISCLAIMER,
        "directions_table": directions.TABLE_VERSION,
    }
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, default=list).encode()
    ).hexdigest()


def _band(score: float) -> str:
    for ceiling, name in _CONFIDENCE_BANDS:
        if score < ceiling:
            return name
    return _CONFIDENCE_BANDS[-1][1]


def solve(estimation: dict) -> dict:
    """Render one PERSON_DIRECTIONAL_ESTIMATION into a human-readable reading."""
    value = estimation["value"]
    statements: list[dict] = []
    axes: dict[str, str] = {}
    axis_refs: list[str] = []

    for signal in value["signals"]:
        observation = signal["observation"]
        ref = signal["provenance_ref"]
        if signal["semantic_type"] == "PERSON_BEHAVIOR_PROFILE":
            for axis, data in observation["axes"].items():
                axes[axis] = data["label"]
                statements.append(
                    {
                        "text": (
                            f"Declared {AXIS_HUMAN.get(axis, axis)}: "
                            f"{LABEL_HUMAN.get(data['label'], data['label'])}."
                        ),
                        "based_on": [ref],
                    }
                )
            axis_refs.append(ref)
        elif "profile" in observation:
            profile = observation["profile"]
            statements.append(
                {
                    "text": (
                        f"Context: seeking direction in '{profile.get('focus_domain')}'"
                        f" ({profile.get('direction')}), region {profile.get('region')}."
                    ),
                    "based_on": [ref],
                }
            )
        elif "pairing" in observation:
            pairing = observation["pairing"]
            statements.append(
                {
                    "text": (
                        f"Regional indicator '{pairing['indicator']}' = "
                        f"{pairing['indicator_value']} was considered for "
                        f"'{pairing['focus_domain']}'."
                    ),
                    "based_on": [ref],
                }
            )

    annotations = value["convergence"].get("annotations", {})
    if annotations.get("environment_coverage") == "none":
        statements.append(
            {
                "text": (
                    "No regional environment data was available; this reading "
                    "rests on personal declarations only."
                ),
                "based_on": [estimation["id"]],
            }
        )

    matched_rule = False
    for rule in ALIGNMENT_RULES:
        if all(axes.get(axis) in allowed for axis, allowed in rule["when"].items()):
            statements.append(
                {"text": rule["text"], "based_on": axis_refs or [estimation["id"]],
                 "rule_id": rule["id"]}
            )
            matched_rule = True
    if axes and not matched_rule:
        statements.append(
            {
                "text": (
                    "The combined evidence is insufficient for an alignment "
                    "observation under the v0.1 rule table."
                ),
                "based_on": axis_refs,
            }
        )

    score = float(estimation["confidence"])
    reasons = [
        "engine weights are an unvalidated uniform prior (RFC-0017)",
        f"engine coverage factor: {value['convergence']['coverage']['factor']}",
    ]
    if annotations.get("environment_coverage") == "none":
        reasons.append("environment data gap lowered confidence (RFC-0017)")

    # Directions layer (RFC-0021): the part that answers the question.
    directional = directions.rank_hypotheses(estimation)
    if directional["space_id"] is None:
        statements.append(
            {
                "text": (
                    "No decision space exists yet for this question; the reading "
                    "cannot rank directions honestly. Decision spaces are added "
                    "by Class 2 RFC."
                ),
                "based_on": [estimation["id"]],
            }
        )

    return build_unit(
        semantic_type="PERSON_DIRECTIONAL_READING",
        entity_ref=estimation["entity_ref"],
        engine=ENGINE,
        value={
            "question": value["question"],
            "statements": statements,
            "context_interpretations": directional["interpretations"],
            "direction_hypotheses": directional["hypotheses"],
            "risk_exposures": directional["risks"],
            "decision_space": {
                "space_id": directional["space_id"],
                "table_version": directional["table_version"],
                "weight_basis": directions.WEIGHT_BASIS,
            },
            "confidence": {"score": score, "band": _band(score), "reasons": reasons},
            "disclaimer": DISCLAIMER,
        },
        confidence=score,  # inherited, never higher (RFC-0019)
        provenance=[estimation["id"]],
        transformation_name="personal-reading-rendering",
        transformation_description=(
            "deterministic rule-based rendering of a directional estimation "
            "into a human-readable reading (RFC-0019 v0.1)"
        ),
        source_tradition=SOURCE_TRADITION,
        parameters_hash=parameters_hash(),
        consent_scope=estimation.get("consent_scope"),
    )
