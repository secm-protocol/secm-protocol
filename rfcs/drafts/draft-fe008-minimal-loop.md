# DRAFT — FE-008 Minimal Validation Loop: Outcomes and Calibration v0.1

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review (implementation on `feature/rfc-0018-0019-slice-completion`) |
| **Class** | 2 (Substantive — Protocol Core service, per RFC-0012) |
| **Authors** | Implementation Workforce (Claude — AI, labeled per RFC-0001 §7) |
| **Requires** | RFC-0002, RFC-0009, RFC-0012, RFC-0013, RFC-0017 |
| **Created** | 2026-07-09 |

## Summary

The embryo of the historical brain (RFC-0009, minimal form): register real-world
**outcomes** against directional estimations and **measure** confidence calibration.
v0.1 measures only — it never recalibrates weights, because recalibration without
sufficient data would be exactly the fake science the constitution forbids.

## Motivation

Without outcomes, the protocol cannot honestly claim to reduce uncertainty (RFC-0001
§6). This RFC closes the loop at its smallest honest size: outcome in, calibration
number out, and an explicit "insufficient data" status until the sample earns more.

## Specification

### 1. Outcome registration

`register_outcome(estimation, outcome_type, evidence_tier, success, note)` produces a
`PROTOCOL_OUTCOME` unit linked by provenance to the estimation:

- `outcome_type` ∈ {subjective_perception, objective_outcome, observed_evidence} —
  the RFC-0000 §17 triad, never merged.
- `evidence_tier` ∈ {**E0, E1 only**}. E2/E3 are *earned* by statistical validation
  and independent replication (RFC-0009); they can never be declared at registration.
- `result.success` is boolean in v0.1 (calibration needs binary resolution first;
  richer outcome shapes are future Class 2 work).
- Outcomes derived from personal estimations **must carry the estimation's
  `consent_scope`** — registration without it fails (precedence rank 1; enforced in
  code because `PROTOCOL_*` is outside the validator's automatic PERSON_* rule).

### 2. Calibration measurement

`calibration_report(estimations, outcomes)` pairs outcomes to estimations by
`estimation_ref` and produces a `PROTOCOL_CALIBRATION_REPORT` unit (registry
amendment) with: sample size, **Brier score** (mean of (confidence − outcome)²), mean
confidence, outcome rate, and a status field:

- `status = "insufficient-data"` while sample < **30** (parameter). No conclusion may
  be drawn, and the report says so itself.
- `status = "measured"` at or above the minimum.
- `recalibration = "not-implemented-in-v0.1"` — weight changes require their own
  Class 2 RFC with measured data behind them (RFC-0001 §6).

### 3. Out of scope

Persistent storage, population aggregation, E2 promotion, weight recalibration —
each is future work gated on real data existing.

## Validation Criteria

- Outcome and report units validate under the RFC-0007 validator (strict mode).
- Tier gate: E2/E3 registration attempts fail. Consent gate: estimation without
  consent fails registration.
- Brier arithmetic verified against hand-computed vectors; report status flips at
  exactly the minimum sample.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Self-reported successes inflating calibration → outcome_type
   and tier are recorded per outcome; E0 self-reports are visible as such in every
   report's provenance.
2. **Wrong assumptions?** Binary success oversimplifies reality → explicit v0.1
   limitation; richer shapes are future RFCs.
3. **Biases?** Survivorship (only happy users report) → sample composition is
   auditable via outcome_type/tier counts; RFC-0009 population rules apply later.
4. **Reversibility?** Pure functions, no storage; nothing to roll back.
5. **Explainability?** Every report cites the outcome units behind every number.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-09 | Draft; implementation on feature branch per CONTRIBUTING flow | — |
