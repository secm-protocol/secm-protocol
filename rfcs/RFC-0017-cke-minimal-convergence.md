# RFC-0017 — CKE Minimal Convergence: The Directional Estimation v0.1

| Field | Value |
|---|---|
| **RFC** | 0017 |
| **Status** | Accepted — 2026-07-09 |
| **Class** | 2 (Substantive — Protocol Core service, per RFC-0012) |
| **Authors** | Implementation Workforce (Claude — AI, labeled per RFC-0001 §7) |
| **Requires** | RFC-0002, RFC-0003, RFC-0007, RFC-0012, RFC-0013, RFC-0015, RFC-0016 |
| **Created** | 2026-07-09 |

## Summary

The heart of SECM (RFC-0000 §13): the Convergence Knowledge Engine never trusts a
single engine — it searches for convergence. v0.1 consumes the outputs of the slice
engines (FE-005, FE-006) and produces one **directional estimation unit**: explainable,
weighted, versioned, traceable, confidence-scored, never deterministic. It is the
evidence bundle the Personal Solver will translate for humans — the CKE itself is
domain-agnostic and never gives advice (Solvers apply, RFC-0000 §10).

## Motivation

With the two engines live, their outputs must converge into one auditable estimation.
This is where the protocol's explainability promise is kept or broken: every
estimation must cite exactly which metadata units support it, from which engines, at
which weights, and why the confidence is what it is.

## Specification

### Honesty rules (constitutional, before any math)

1. **Weights are earned, and nothing is earned yet.** FE-008 has authority over engine
   weights (RFC-0001 §6), and no outcome data exists. Therefore v0.1 uses a **uniform
   prior weight of 1.0 per engine, permanently labeled** `"uniform-prior-unvalidated"`
   inside every estimation. The protocol never pretends its weights are science before
   calibration makes them so.
2. **Convergence cannot manufacture certainty.** Estimation confidence never exceeds
   the strongest component's confidence, and is protocol-capped at **0.95**
   (parameter) — an estimation is a hypothesis by constitution (§13), never a verdict.

### Inputs

Metadata units produced by the slice engines for one RX session — recommended:
the FE-006 `PERSON_BEHAVIOR_PROFILE` composite and all FE-005 outputs. Units from
engines outside the slice set are ignored in v0.1 (Zero Trust: the CKE consumes only
engines it knows). The FE-005 `PERSON_CONTEXT` **profile** unit is mandatory — it
carries the question (focus domain + direction sought).

### Transformation: weighted evidence bundle v0.1

1. **Signals** — every consumed unit becomes a signal entry citing: source engine,
   semantic type, full observation value, unit confidence, engine weight (with basis
   label), and the unit id (`provenance_ref`). The estimation is self-contained: an
   auditor can read it without fetching anything else.
2. **Annotations** — the FE-005 empty-environment marker is **not** a signal (its 1.0
   confidence states an absence; letting it enter the mean would raise estimation
   confidence — exactly backwards). It becomes a convergence annotation and applies
   the environment-gap factor below.
3. **Confidence formula (v0.1, all parameters versioned in `parameters_hash`):**

```
component  = unit_confidence × engine_weight        (weight = 1.0 prior)
base       = weighted_mean(components)
coverage   = engines_contributing / engines_expected (slice: 2)
gap        = 0.85 if environment_coverage == "none" else 1.0
confidence = min(base × coverage × gap, max(unit confidences), 0.95)
```

### Output

One `PERSON_DIRECTIONAL_ESTIMATION` unit (registry amendment: new identifier in the
`PERSON_` namespace — consent enforcement applies automatically). Value carries:
`question`, `signals[]`, and a `convergence` block (method, engine weights with basis,
coverage, annotations). Provenance lists every consumed unit id. Emitted by
engine id `CKE` (Protocol Core, RFC-0012 — versionable, never frozen).

## Validation Criteria

- Estimation validates under the RFC-0007 validator, strict registry mode.
- Formula tests: coverage factor with one engine missing; environment-gap penalty;
  cap at strongest component; protocol ceiling; determinism of value payloads.
- Explainability test: every signal's `provenance_ref` resolves to a consumed unit.
- Missing FE-005 profile → explicit error (no estimation without a question).

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** The formula's simplicity could be mistaken for validated
   science → every estimation carries the `uniform-prior-unvalidated` label
   internally; removing that label requires FE-008 calibration data (Class 2).
2. **Wrong assumptions?** That a linear weighted mean is the right combiner — it is a
   v0.1 placeholder; the CKE is Protocol Core and its strategy is versionable by
   Class 2 RFC with benchmark proof (RFC-0012).
3. **Biases?** Coverage penalty may under-reward sparse-but-strong evidence → the cap
   rule keeps strong single signals from being inflated, and calibration will tune
   the factors.
4. **Reversibility?** All parameters live in `parameters_hash`; old estimations remain
   valid under their recorded version.
5. **Explainability?** The estimation embeds its full evidence, weights, labels and
   arithmetic inputs — it is its own audit trail.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-09 | Draft; implementation started on feature branch per CONTRIBUTING flow | — |
| 2026-07-09 | **Accepted** — implementation merged to `develop`, 49/49 tests green | Vision Keeper (Osvaldo) |
