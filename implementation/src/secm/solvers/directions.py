"""Directional hypotheses layer — RFC-0021 v0.2.

Decision spaces, indicator interpretation and structural risk exposure.
Every table here is an expert-authored, versioned prior — labeled
unvalidated until outcome calibration (RFC-0018) earns more. Tables are
public and Class 2 governed: author bias is answerable to review, and
opposing evidence is always rendered.
"""

from __future__ import annotations

TABLE_VERSION = "0.2.0"
WEIGHT_BASIS = "expert-prior-unvalidated"

STRONG, MODERATE, WEAK = 2.0, 1.0, 0.5

# ---------------------------------------------------------------------------
# Indicator interpretation thresholds (neutral implications, never commands).
# ---------------------------------------------------------------------------

def interpret_indicators(pairings: dict[str, float]) -> list[dict]:
    """Turn paired indicator values into direction-relevant implications."""
    interpretations = []
    rate = pairings.get("interest_rate")
    if rate is not None:
        if rate >= 12.0:
            interpretations.append({
                "indicator": "interest_rate", "value": rate, "level": "extreme",
                "implication": (
                    "debt-servicing cost is extreme: existing debt grows fast by "
                    "itself, new borrowing is strongly contraindicated, and "
                    "creditors have elevated incentive to renegotiate"
                ),
            })
        elif rate >= 8.0:
            interpretations.append({
                "indicator": "interest_rate", "value": rate, "level": "elevated",
                "implication": "debt cost is elevated; borrowing deserves caution",
            })
        else:
            interpretations.append({
                "indicator": "interest_rate", "value": rate, "level": "moderate",
                "implication": "debt cost is moderate by historical standards",
            })
    inflation = pairings.get("inflation")
    if inflation is not None:
        level = "high" if inflation >= 0.7 else "moderate" if inflation >= 0.3 else "low"
        interpretations.append({
            "indicator": "inflation", "value": inflation, "level": level,
            "implication": {
                "high": "purchasing power is eroding fast; idle cash loses value quickly",
                "moderate": "purchasing power erosion is moderate",
                "low": "purchasing power erosion is currently low",
            }[level],
        })
    fx = pairings.get("exchange_rate")
    if fx is not None and fx >= 5.0:
        interpretations.append({
            "indicator": "exchange_rate", "value": fx, "level": "weak-brl",
            "implication": (
                "the BRL is weak against the USD: income streams denominated or "
                "linked to USD gain local value"
            ),
        })
    return interpretations


# ---------------------------------------------------------------------------
# Decision space: finances / organize-recover (v0.2 founding space).
# Each evidence link: (condition_id, weight, human description).
# Conditions are evaluated against a normalized context dict.
# ---------------------------------------------------------------------------

FINANCES_ORGANIZE_RECOVER = {
    "space_id": "finances/organize-recover",
    "hypotheses": [
        {
            "id": "H1-stabilize-first",
            "direction": (
                "Stabilize base cash flow before any strategic move: know exactly "
                "what enters and leaves each month, and stop new leaks first."
            ),
            "support": [
                ("horizon_short", STRONG,
                 "a day-to-day planning horizon favors direction that pays off in "
                 "weeks, not years"),
                ("rate_extreme", MODERATE,
                 "with extreme debt cost, every unstabilized month compounds "
                 "against you"),
                ("direction_recover", MODERATE,
                 "organize/recover questions start from visibility and control"),
            ],
            "oppose": [],
        },
        {
            "id": "H2-restructure-debt",
            "direction": (
                "Prioritize renegotiating and consolidating existing debt: at "
                "extreme rates, reducing the interest line beats almost any "
                "earning move of the same size."
            ),
            "support": [
                ("rate_extreme", STRONG,
                 "at extreme rates, renegotiation leverage is historically at its "
                 "highest — creditors prefer restructured debt over default"),
                ("direction_recover", STRONG,
                 "declared goal is organize/recover: the debt line is the goal"),
                ("risk_calculated", MODERATE,
                 "a declared calculated-risk posture matches negotiation over "
                 "gambles"),
            ],
            "oppose": [],
        },
        {
            "id": "H3-expand-income-capacity",
            "direction": (
                "Expand income using skills you already have, at near-zero "
                "capital cost — especially income linked to strong currencies."
            ),
            "support": [
                ("field_technology", MODERATE,
                 "declared field (technology/Web3) monetizes without upfront "
                 "capital"),
                ("fx_weak_brl", MODERATE,
                 "weak BRL raises the local value of USD-linked skill income"),
                ("decision_instinct", WEAK,
                 "fast instinctive execution helps in opportunity-driven income"),
            ],
            "oppose": [
                ("horizon_short", WEAK,
                 "income expansion needs some weeks of consistent execution"),
            ],
        },
        {
            "id": "H4-high-risk-recovery-bet",
            "direction": (
                "Attempt fast recovery through leveraged or high-volatility bets."
            ),
            "support": [
                ("decision_instinct", WEAK,
                 "instinctive deciders are drawn to fast-resolution moves"),
            ],
            "oppose": [
                ("rate_extreme", STRONG,
                 "leverage at extreme rates makes losing bets catastrophic, not "
                 "just painful"),
                ("risk_calculated", STRONG,
                 "your own declared risk posture (calculated) contradicts this "
                 "direction"),
                ("debt_distress", STRONG,
                 "documented pattern: recovery bets made under debt distress "
                 "systematically overweight hope and underweight downside"),
            ],
        },
    ],
}

DECISION_SPACES = {
    ("finances", "organize-recover"): FINANCES_ORGANIZE_RECOVER,
}

# ---------------------------------------------------------------------------
# Structural risk exposure (documented predatory/risk patterns).
# Human protection is precedence rank 1 (RFC-0001 §4).
# ---------------------------------------------------------------------------

STRUCTURAL_RISKS = [
    {
        "id": "SR1-quick-recovery-schemes",
        "applies_when": ["debt_distress", "field_technology"],
        "warning": (
            "Quick-recovery schemes — including crypto ponzi and 'guaranteed "
            "yield' patterns — disproportionately target people in debt "
            "distress, and target them harder inside crypto/Web3 circles. "
            "Any offer whose urgency grows with your desperation fits the "
            "documented pattern."
        ),
    },
    {
        "id": "SR2-revolving-credit-spiral",
        "applies_when": ["debt_distress", "rate_extreme"],
        "warning": (
            "At extreme base rates, revolving credit (credit card, overdraft) "
            "compounds into the fastest-growing debt class in Brazil — the "
            "documented spiral pattern for indebted households."
        ),
    },
    {
        "id": "SR3-peak-rate-borrowing",
        "applies_when": ["rate_extreme"],
        "warning": (
            "New borrowing contracted at peak rates locks today's extreme cost "
            "into your future even if rates later fall."
        ),
    },
]


# ---------------------------------------------------------------------------
# Condition evaluation and ranking.
# ---------------------------------------------------------------------------

def build_conditions(estimation_value: dict, interpretations: list[dict]) -> set[str]:
    """Normalize estimation signals + interpretations into condition ids."""
    conditions: set[str] = set()
    question = estimation_value.get("question", {})
    if question.get("direction") in ("organize-recover",):
        conditions.add("direction_recover")
        conditions.add("debt_distress")  # organize-recover declares distress

    for signal in estimation_value.get("signals", []):
        observation = signal.get("observation", {})
        axes = observation.get("axes")
        if axes:
            if axes.get("decision_latency", {}).get("label") == "instinct":
                conditions.add("decision_instinct")
            if axes.get("risk_appetite", {}).get("label") == "calculated":
                conditions.add("risk_calculated")
            if axes.get("planning_horizon", {}).get("label") in ("day-to-day", "weeks-months"):
                conditions.add("horizon_short")
            if axes.get("planning_horizon", {}).get("label") in ("1-3-years", "5-plus-years"):
                conditions.add("horizon_long")
        profile = observation.get("profile")
        if profile and profile.get("field") == "technology":
            conditions.add("field_technology")

    for interp in interpretations:
        if interp["indicator"] == "interest_rate" and interp["level"] == "extreme":
            conditions.add("rate_extreme")
        if interp["indicator"] == "exchange_rate" and interp["level"] == "weak-brl":
            conditions.add("fx_weak_brl")
    return conditions


def rank_hypotheses(estimation: dict) -> dict:
    """Produce interpretations, ranked directional hypotheses and risk exposures.

    Returns {} when no decision space exists for the question — the reading
    then says so honestly instead of inventing direction.
    """
    value = estimation["value"]
    question = value.get("question", {})
    space = DECISION_SPACES.get((question.get("focus_domain"), question.get("direction")))

    pairings: dict[str, float] = {}
    for signal in value.get("signals", []):
        pairing = signal.get("observation", {}).get("pairing")
        if pairing:
            pairings[pairing["indicator"]] = pairing["indicator_value"]
    interpretations = interpret_indicators(pairings)

    if space is None:
        return {"interpretations": interpretations, "hypotheses": [], "risks": [],
                "space_id": None, "table_version": TABLE_VERSION}

    conditions = build_conditions(value, interpretations)
    base_confidence = float(estimation["confidence"])

    ranked = []
    for hypothesis in space["hypotheses"]:
        support_hits = [
            {"condition": c, "weight": w, "because": text}
            for c, w, text in hypothesis["support"] if c in conditions
        ]
        oppose_hits = [
            {"condition": c, "weight": w, "because": text}
            for c, w, text in hypothesis["oppose"] if c in conditions
        ]
        support = sum(h["weight"] for h in support_hits)
        oppose = sum(h["weight"] for h in oppose_hits)
        total = support + oppose
        ratio = (support / total) if total else 0.0
        ranked.append({
            "id": hypothesis["id"],
            "direction": hypothesis["direction"],
            "net_score": round(support - oppose, 4),
            "confidence": round(min(base_confidence * ratio, base_confidence), 4),
            "weight_basis": WEIGHT_BASIS,
            "evidence_for": support_hits,
            "evidence_against": oppose_hits,
        })
    ranked.sort(key=lambda h: h["net_score"], reverse=True)

    risks = [
        {"id": r["id"], "warning": r["warning"]}
        for r in STRUCTURAL_RISKS
        if all(c in conditions for c in r["applies_when"])
    ]
    return {
        "interpretations": interpretations,
        "hypotheses": ranked,
        "risks": risks,
        "space_id": space["space_id"],
        "table_version": TABLE_VERSION,
    }
