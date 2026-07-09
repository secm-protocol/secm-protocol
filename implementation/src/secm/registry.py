"""Universal Semantic Layer v0.1 identifier registry.

Source of truth: rfcs/RFC-0003-semantic-layer.md.
Identifiers name meaning, not wording. Nothing is ever deleted — only deprecated.
"""

from __future__ import annotations

import re

# Naming rule: SCREAMING_SNAKE_CASE, ASCII only (draft-semantic-layer §1).
NAMING_RULE = re.compile(r"^[A-Z][A-Z0-9]*(_[A-Z0-9]+)*$")

# First segment of every identifier must be a registered namespace.
NAMESPACES = ("PERSON", "ORG", "PLACE", "EVENT", "TECH", "ECON", "SCI", "PROTOCOL")

ACTIVE = "Active"
RESERVED = "Reserved"  # registered, benchmark-gated (RX behavioral swaps)

# Registry v0.1 (draft-semantic-layer §3).
REGISTRY: dict[str, str] = {
    # Person — identity-derived (Tier 0 inputs, ephemeral)
    "PERSON_NAME": ACTIVE,
    "PERSON_BIRTH_DATE": ACTIVE,
    "PERSON_BIRTH_LOCATION": ACTIVE,
    # Person — positioning and context
    "PERSON_LOCATION_CURRENT": ACTIVE,
    "PERSON_FOCUS_DOMAIN": ACTIVE,
    "PERSON_OCCUPATION_FIELD": ACTIVE,
    "PERSON_GOAL": ACTIVE,
    "PERSON_CONSTRAINTS": ACTIVE,
    "PERSON_CONTEXT": ACTIVE,
    "PERSON_HISTORY": ACTIVE,
    "PERSON_TRAJECTORY_5Y": ACTIVE,
    # Person — behavioral (RX active)
    "PERSON_BEHAVIOR_DECISION": ACTIVE,
    "PERSON_BEHAVIOR_RISK": ACTIVE,
    "PERSON_BEHAVIOR_HORIZON": ACTIVE,
    # Person — behavioral composite (added per RFC-0016)
    "PERSON_BEHAVIOR_PROFILE": ACTIVE,
    # Person — CKE output (added per RFC-0017); PERSON_ namespace so consent
    # enforcement applies automatically to estimations
    "PERSON_DIRECTIONAL_ESTIMATION": ACTIVE,
    # Person — behavioral (reserved, benchmark-gated swaps)
    "PERSON_BEHAVIOR_HABIT": RESERVED,
    "PERSON_BEHAVIOR_SOCIAL": RESERVED,
    "PERSON_BEHAVIOR_FAILURE": RESERVED,
    "PERSON_BEHAVIOR_ENERGY": RESERVED,
    # Person — linguistic
    "PERSON_LANGUAGE_SAMPLE": ACTIVE,
    # Graph entities (RFC-0000 §12)
    "ORG_ENTITY": ACTIVE,
    "PLACE_CITY": ACTIVE,
    "PLACE_COUNTRY": ACTIVE,
    "TECH_ENTITY": ACTIVE,
    "ECON_INDICATOR": ACTIVE,
    "SCI_DISCOVERY": ACTIVE,
    "EVENT_HISTORICAL": ACTIVE,
    # Protocol mechanics
    "PROTOCOL_CONTINUITY_TOKEN": ACTIVE,
    "PROTOCOL_CONSENT_SCOPE": ACTIVE,
    "PROTOCOL_OUTCOME": ACTIVE,
    "PROTOCOL_EVIDENCE_TIER": ACTIVE,
    # Added per RFC-0018 (calibration measurement)
    "PROTOCOL_CALIBRATION_REPORT": ACTIVE,
    # Added per RFC-0019 (Personal Solver reading); PERSON_ namespace so
    # consent enforcement applies automatically
    "PERSON_DIRECTIONAL_READING": ACTIVE,
}


def conforms_to_naming_rule(identifier: str) -> bool:
    """True when the identifier follows §1 naming rules and uses a known namespace."""
    if not NAMING_RULE.match(identifier):
        return False
    return identifier.split("_", 1)[0] in NAMESPACES


def is_registered(identifier: str) -> bool:
    return identifier in REGISTRY


def is_personal(identifier: str) -> bool:
    """PERSON_* units derive from personal data — consent_scope is mandatory
    (RFC-0002 rule 5; Privacy Architecture, precedence rank 1)."""
    return identifier.startswith("PERSON_")
