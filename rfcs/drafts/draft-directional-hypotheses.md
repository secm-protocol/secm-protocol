# DRAFT — Directional Hypotheses v0.2: Readings That Answer the Question

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review (implementation on `feature/rfc-0021-directional-hypotheses`) |
| **Class** | 2 (Substantive — Solver v0.2 + interpretation layer) |
| **Authors** | **Vision Keeper (Osvaldo)** — requirement, from RX-000001 field feedback; Implementation Workforce (Claude — AI, design) |
| **Requires** | RFC-0011, RFC-0017, RFC-0019, RFC-0020 |
| **Created** | 2026-07-09 |

## Summary

The first real RX (RX-000001) exposed an architectural failure recorded here honestly:
the v0.1 reading restated inputs and answered nothing — "a speaker who talks and says
nothing" (Vision Keeper). RFC-0000 §1 promises **explainable directional hypotheses**;
v0.1 delivered an evidence mirror. This RFC adds the three missing layers: decision
spaces (ranked candidate directions), indicator interpretation (numbers become
implications), and structural risk exposure (documented manipulation/risk patterns
that target people in the reading's situation).

## Specification

### 1. Decision spaces

For each (focus_domain, direction) pair, a versioned finite set of **candidate
directions**. v0.2 ships the space for `finances / organize-recover` (4 candidates:
stabilize-first, restructure-debt, expand-income-capacity, high-risk-recovery-bet).
Each candidate carries **evidence links**: conditions over signals/interpretations
that support or oppose it, with weights (strong 2.0 / moderate 1.0 / weak 0.5).

Scoring: `net = Σ support − Σ oppose`; ranking by net; per-hypothesis confidence =
estimation confidence × support ratio, **never above the estimation's confidence**.
Every link fired is listed in the reading — for and against. Tables are
expert-authored, versioned in `parameters_hash`, and **labeled unvalidated** until
outcome calibration (RFC-0018) earns more. New spaces are Class 2 additions.

### 2. Indicator interpretation

Versioned threshold tables turn paired indicators into direction-relevant
implications (e.g., `interest_rate ≥ 12` → "extreme debt-servicing cost; new
borrowing contraindicated; renegotiation leverage elevated"; `exchange_rate ≥ 5` →
"USD-linked income streams gain BRL value"). Interpretations are neutral,
evidence-linked statements — never commands.

### 3. Structural risk exposure

A versioned table of **documented risk patterns** with applicability conditions —
e.g., "quick-recovery schemes (including crypto ponzi patterns) disproportionately
target people in debt distress; exposure elevated when the person operates in
crypto/Web3". Human protection is precedence rank 1: warning about known predatory
patterns is protocol duty, not editorializing.

### 4. Boundaries (unchanged constitution)

Hypotheses ranked, never verdicts; no specific products, assets or trades are ever
named (the protocol informs direction categories, not transactions); disclaimer
non-removable; confidence inherited and decomposed per hypothesis.

## Validation Criteria

- RX-000001 inputs produce a reading with ≥3 ranked hypotheses, each citing its
  for/against evidence; the empty "insufficient" phrasing may appear only when a
  domain has no decision space yet.
- Determinism; strict validation; per-hypothesis confidence ≤ reading confidence.
- Risk exposures fire only when their conditions hold.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Expert-authored links read as validated science → every
   hypothesis carries the unvalidated label and its evidence list; calibration
   reranks with data.
2. **Wrong assumptions?** Weights are hand-set priors → parameters versioned;
   FE-008 outcome data is the correction path.
3. **Biases?** Author bias in decision spaces → tables are public, cited, Class 2
   reviewed; opposing evidence is always rendered.
4. **Reversibility?** Versioned tables; v0.1 readings remain valid under their hash.
5. **Explainability?** Improves it: direction claims now carry explicit for/against
   chains instead of silence.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-09 | Draft, from RX-000001 field feedback | — |
