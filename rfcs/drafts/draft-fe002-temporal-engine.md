# DRAFT — FE-002 Temporal Encoding System v0.1

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review (implementation on `feature/rfc-0021-structural-engines`) |
| **Class** | 2 (Substantive — Foundation Engine specification, per RFC-0021 priority amendment) |
| **Authors** | Implementation Workforce (Claude — AI, labeled per RFC-0001 §7) |
| **Requires** | RFC-0002, RFC-0003, RFC-0007, RFC-0008, RFC-0011, draft-structural-first-priority |
| **Created** | 2026-07-09 |

## Summary

Specifies FE-002, named in RFC-0000 §8 since Genesis. Decomposes birth-date arithmetic
— digit-sum reduction plus the plain calendar weekday of birth — into neutral
computational transformations over `PERSON_BIRTH_DATE` (RFC-0011 Q2).

## Motivation

Companion to FE-001: the second structural-identity layer, using the same reduction
algorithm on the date instead of the name, plus one genuinely deterministic calendar
fact.

## Specification

### Input

`PERSON_BIRTH_DATE` (RFC-0011 Q2) — **Tier 0, ephemeral** (RFC-0008): consumed
in-memory only, never stored.

### Transformation v0.1

1. **`date_reduction`:** sum all digits of the date as DDMMYYYY, reduce via the same
   digit-sum algorithm as FE-001 (repdigit-11-multiple halt).
2. **`birth_weekday`:** the calendar day of the week (Monday–Sunday) — plain,
   deterministic arithmetic, no interpretive claim attached.

### Output

One `PERSON_TEMPORAL_STRUCTURE` unit (registry addition): `date_reduction`,
`birth_weekday`.

### Confidence — honest by construction

Baseline **0.15** for both fields (shared with FE-001): `date_reduction` for the same
reason as FE-001 (unvalidated historical transformation); `birth_weekday` is
arithmetically certain but its **relevance** to anything about the person is equally
unvalidated, so it is held to the same honest confidence as a signal, not as a
computation.

### Privacy

Same guarantee as FE-001: outputs collapse to one of a small set of values,
irreversible to the original date — stronger than hashing for this low-entropy input
(RFC-0008).

## Validation Criteria

- Deterministic; validates under RFC-0007 strict mode.
- `birth_weekday` matches the proleptic Gregorian calendar exactly (verified against
  Python's standard library as ground truth).
- No banned terminology anywhere.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Same risk class as FE-001 — mitigated identically (low
   confidence, explicit unvalidated framing, FE-008 gating).
2. **Wrong assumptions?** That the Gregorian calendar is universally applicable —
   true for RFC-0011's date input format; calendar-system extensions are future work.
3. **Biases?** None beyond the shared reduction algorithm's origin, disclosed openly.
4. **Reversibility?** Full — versioned parameters.
5. **Explainability?** Every unit names its exact transformation.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-09 | Draft | — |
