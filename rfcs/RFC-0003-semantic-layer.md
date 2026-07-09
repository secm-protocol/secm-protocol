# RFC-0003 — Universal Semantic Layer: Identifier Registry

| Field | Value |
|---|---|
| **RFC** | 0003 |
| **Status** | Accepted — 2026-07-09 |
| **Class** | 2 (Substantive) |
| **Authors** | Implementation Workforce (Claude — AI, labeled per RFC-0001 §7) |
| **Requires** | RFC-0000 §11, RFC-0002 |
| **Created** | 2026-07-08 |

## Summary

RFC-0000 §11 establishes that the protocol has no human language: internally it speaks
only semantic identifiers. This draft defines the identifier system — naming rules,
namespaces, lifecycle and governance — and opens the registry with the identifiers
already in use by the RX Input Specification. It works like IANA works for the
Internet: a boring, disciplined registry that everything else depends on.

## Motivation

Without a governed registry, engines invent incompatible names, locales drift apart,
and population comparability — the foundation of the historical brain — silently
breaks. The registry must exist before the first line of engine code.

## Specification

### 1. Naming rules

- `SCREAMING_SNAKE_CASE`, ASCII only, English canonical.
- First segment is the **namespace**: `PERSON_`, `ORG_`, `PLACE_`, `EVENT_`, `TECH_`,
  `ECON_`, `SCI_`, plus `PROTOCOL_` for internal mechanics.
- Identifiers name **meaning, not wording**: question phrasing and locale translations
  change; the identifier never does.

### 2. Lifecycle

`Proposed → Active → Deprecated` — never deleted. Deprecated identifiers remain
resolvable forever (historical records reference them). Registry changes are Class 2.

### 3. Initial registry (v0.1)

**Person — identity-derived (Tier 0 inputs, ephemeral):**
`PERSON_NAME` · `PERSON_BIRTH_DATE` · `PERSON_BIRTH_LOCATION`

**Person — positioning and context:**
`PERSON_LOCATION_CURRENT` · `PERSON_FOCUS_DOMAIN` · `PERSON_OCCUPATION_FIELD` ·
`PERSON_GOAL` · `PERSON_CONSTRAINTS` · `PERSON_CONTEXT` · `PERSON_HISTORY` ·
`PERSON_TRAJECTORY_5Y`

**Person — behavioral (RX active):**
`PERSON_BEHAVIOR_DECISION` · `PERSON_BEHAVIOR_RISK` · `PERSON_BEHAVIOR_HORIZON` ·
`PERSON_BEHAVIOR_PROFILE` *(composite, added per RFC-0016)*

**Person — behavioral (reserved, benchmark-gated swaps):**
`PERSON_BEHAVIOR_HABIT` · `PERSON_BEHAVIOR_SOCIAL` · `PERSON_BEHAVIOR_FAILURE` ·
`PERSON_BEHAVIOR_ENERGY`

**Person — linguistic:**
`PERSON_LANGUAGE_SAMPLE`

**Graph entities (RFC-0000 §12):**
`ORG_ENTITY` · `PLACE_CITY` · `PLACE_COUNTRY` · `TECH_ENTITY` ·
`ECON_INDICATOR` · `SCI_DISCOVERY` · `EVENT_HISTORICAL`

**Protocol mechanics:**
`PROTOCOL_CONTINUITY_TOKEN` · `PROTOCOL_CONSENT_SCOPE` · `PROTOCOL_OUTCOME` ·
`PROTOCOL_EVIDENCE_TIER`

### 4. Locale independence

Human languages bind to identifiers through versioned locale files
(`locales/pt-BR.yml`, …). Translations are Class 1 once canonical wording exists;
new identifiers are Class 2. Population data aggregates by identifier, never by
wording — comparability across languages is structural.

## Validation Criteria

- Uniqueness and naming-rule conformance enforced by an automated registry check.
- Every metadata unit's `semantic_type` resolves to an Active or Deprecated identifier.
- Round-trip: RX intake in any locale produces identical identifier streams for
  identical answers.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Namespace sprawl → new namespaces require Class 2 with
   justification.
2. **Wrong assumptions?** English-canonical could embed anglophone bias → identifiers
   name concepts, wording lives in locales; the registry is reviewable by any culture.
3. **Biases?** Person-centric registry skew → graph namespaces are first-class from
   v0.1.
4. **Reversibility?** Nothing is deleted; deprecation preserves history.
5. **Explainability?** Every identifier has a registry entry stating its meaning and
   consuming engines.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-08 | Draft | — |
| 2026-07-09 | **Accepted** (en-bloc Vision Keeper approval) | Vision Keeper (Osvaldo) |
| 2026-07-09 | Registry amendment: `PERSON_BEHAVIOR_PROFILE` added per RFC-0016 | Class 2, via RFC-0016 acceptance |
| 2026-07-09 | Registry amendment: `PERSON_DIRECTIONAL_ESTIMATION` added per RFC-0017 | Class 2, via RFC-0017 acceptance |
| 2026-07-09 | Registry amendments: `PROTOCOL_CALIBRATION_REPORT` (RFC-0018), `PERSON_DIRECTIONAL_READING` (RFC-0019) | Class 2, via acceptances |
