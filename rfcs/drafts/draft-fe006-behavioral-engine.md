# DRAFT — FE-006 Behavioral System: RX Behavioral Encoding v0.1

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review |
| **Class** | 2 (Substantive — Foundation Engine specification) |
| **Authors** | Implementation Workforce (Claude — AI, labeled per RFC-0001 §7) |
| **Requires** | RFC-0002, RFC-0003, RFC-0007, RFC-0011, RFC-0013 |
| **Created** | 2026-07-09 |

## Summary

Specifies the first working version of FE-006: the transformation that turns the RX
behavioral answers (Q7–Q9) into canonical behavioral metadata. Deliberately small,
fully deterministic, honest about being self-report data.

## Motivation

RFC-0013 fixes FE-006 as one of the two slice engines. Its inputs already exist
(RFC-0011 Q7–Q9); its output feeds the CKE. This is the shortest path from an answered
questionnaire to convergence-ready behavioral metadata.

## Specification

### Inputs (semantic units, per Zero Trust — the engine never sees identity)

`PERSON_BEHAVIOR_DECISION`, `PERSON_BEHAVIOR_RISK`, `PERSON_BEHAVIOR_HORIZON` — the
categorical answers of RX Q7–Q9 (RFC-0011). All optional; the engine emits only for
answered questions.

### Transformation: ordinal axis mapping v0.1

Each answer maps deterministically onto a named axis with ordinal positions
{0.0, 1/3, 2/3, 1.0}, ordered per RFC-0011 option order:

| Axis | 0.0 | 1/3 | 2/3 | 1.0 |
|---|---|---|---|---|
| `decision_latency` | instinct (fast) | data-seeking | consultative | postponing |
| `risk_appetite` | risk-seeking | calculated | stability-first | risk-averse |
| `planning_horizon` | day-to-day | weeks–months | 1–3 years | 5+ years |

### Outputs

One metadata unit per answered axis (`semantic_type` = the input identifier;
`value` = `{axis, position, label}`), plus one composite `PERSON_BEHAVIOR_PROFILE`
unit (registry addition required) whose provenance lists the axis units.

- `transformation.source_tradition` = "behavioral self-report, structured questionnaire".
- `transformation.parameters_hash` = sha256 of the mapping table version — changing
  the table is Class 2 and produces a new hash, auditable forever.

### Confidence — honest by construction

Self-report is E0 evidence (RFC-0009): baseline confidence **0.55** per axis
(parameter), composite confidence scaled by coverage (3/3 answered = baseline;
fewer = proportionally lower). Confidence rises above baseline only when FE-008
calibration earns it (RFC-0001 §6). The engine never pretends self-report is
observed truth.

### Determinism

Same inputs + same mapping version → byte-identical outputs (except `id`/`created_at`).
No randomness, no hidden state.

## Validation Criteria

- Every output validates under the RFC-0007 validator (strict registry mode).
- Determinism test: repeated runs produce identical value payloads.
- Coverage test: 0–3 answers produce 0–3 axis units + composite iff ≥1 axis exists.
- Confidence never exceeds baseline in v0.1.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Ordinal positions may imply false equidistance between
   options → v0.1 states this openly; positions are parameters recalibrated by FE-008
   against outcomes, not assumptions.
2. **Wrong assumptions?** That 3 axes suffice — reserved identifiers (RFC-0003) allow
   benchmark-proven swaps within the 10-question cap.
3. **Biases?** Option wording bias imported from RFC-0011 → wording is versioned;
   population comparability is tracked per intake version.
4. **Reversibility?** Mapping tables are versioned; old units remain valid under their
   recorded parameters_hash.
5. **Explainability?** Every unit names its axis, label, mapping version and source
   tradition.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-09 | Draft | — |
