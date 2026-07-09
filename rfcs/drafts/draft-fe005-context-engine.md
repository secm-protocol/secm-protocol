# DRAFT — FE-005 Context System: RX Context Profile v0.1

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review |
| **Class** | 2 (Substantive — Foundation Engine specification) |
| **Authors** | Implementation Workforce (Claude — AI, labeled per RFC-0001 §7) |
| **Requires** | RFC-0002, RFC-0003, RFC-0007, RFC-0008, RFC-0011, RFC-0013, RFC-0014 |
| **Created** | 2026-07-09 |

## Summary

Specifies the first working version of FE-005: the transformation that builds a
person-side **context profile** from RX answers and pairs it with whatever
environment-side context units exist (from RFC-0014 ingestion). Honest rule: when the
environment side is empty, the engine says so and confidence reflects it — it never
invents context.

## Motivation

Directional estimation is alignment between person and environment (RFC-0000 §5).
FE-005 is the engine that holds both sides. RFC-0013 fixes it as the second slice
engine.

## Specification

### Inputs

- Person side (RFC-0011, post-bucketing per RFC-0008): `PERSON_LOCATION_CURRENT`
  (region), `PERSON_FOCUS_DOMAIN`, `PERSON_OCCUPATION_FIELD` (optional),
  `PERSON_CONSTRAINTS` (optional), age band derived from `PERSON_BIRTH_DATE` (Tier 0:
  the engine receives the band, never the date).
- Environment side (optional in v0.1): `ECON_INDICATOR`, `PLACE_CITY`, `PLACE_COUNTRY`
  units for the person's region, produced by RFC-0014 ingestion when live.

### Transformation: context profiling v0.1

1. **`PERSON_CONTEXT` profile unit** — normalized person-side context: region, focus
   domain + direction sought, field, age band, constraint set. Provenance lists the
   consumed intake units.
2. **Pairing units** — for each environment unit found for the person's region and
   relevant to the focus domain (relevance map v0.1: a versioned domain→indicator
   table, e.g. `finances → inflation, interest rates`; `career/business → regional
   economic indicators`), one `PERSON_CONTEXT` pairing unit citing both sides in
   provenance.
3. **Empty-environment marker** — when no environment units exist for the region, one
   explicit unit stating so (`value.environment_coverage = "none"`), so downstream
   convergence lowers confidence for reasons visible in the audit trail.

### Confidence

Person-side profile: 0.8 baseline (structured self-declared facts, parameter).
Pairing units: min(person-side, environment unit confidence) × freshness factor
(RFC-0014 staleness rule). Empty-environment marker: confidence 1.0 — absence honestly
stated is a certain fact.

### Determinism and Zero Trust

Deterministic per mapping version; the engine receives semantic units only — never
identity, never raw birth dates or exact locations (RFC-0008 Tier 0 guarantees).

## Validation Criteria

- Outputs validate under RFC-0007 strict mode.
- Determinism test; coverage test (minimum Band 1 intake yields profile + marker).
- Privacy test: no output unit contains sub-region location or exact age.
- Relevance-map versioning: changing the domain→indicator table changes
  parameters_hash.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Relevance map could encode my assumptions about what matters
   per domain → the map is a versioned, benchmarkable parameter — FE-008 calibrates it
   against outcomes; it is never hardcoded belief.
2. **Wrong assumptions?** That regional granularity is enough — bucketing thresholds
   are RFC-0008 parameters, tunable with evidence.
3. **Biases?** Environment data coverage is unequal across regions (rich-country data
   bias) → the empty-environment marker makes coverage gaps visible instead of silent;
   coverage is reported per aggregate (RFC-0009 premortem 3).
4. **Reversibility?** Versioned maps; old units valid under recorded hashes.
5. **Explainability?** Every pairing names both provenance sides; absence of context
   is itself an explainable unit.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-09 | Draft | — |
