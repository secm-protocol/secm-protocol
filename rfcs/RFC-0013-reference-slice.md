# RFC-0013 — v1.0 Reference Implementation Slice

| Field | Value |
|---|---|
| **RFC** | 0013 |
| **Status** | Accepted — 2026-07-09 (slice scope fixed: FE-005 + FE-006 → CKE minimal → FE-008 loop → Personal Solver) |
| **Class** | 2 (Substantive) |
| **Authors** | Implementation Workforce (Claude — AI, labeled per RFC-0001 §7) |
| **Requires** | RFC-0000, RFC-0001, RFC-0002 |
| **Created** | 2026-07-08 |

## Summary

Delivery strategy for v1.0: instead of building all nine engines in breadth, build one
**thin vertical slice** end-to-end — schema → two engines → convergence → validation →
one Solver — working on a narrow, real use case. This tests the architecture against
reality where correcting is cheap, before scaling in breadth. Bitcoin shipped a
whitepaper and one minimal working client, not ten complete modules.

## Motivation

The greatest architectural risk is discovering in month twelve that the metadata
envelope, the convergence interface or the validation loop doesn't fit reality. A
vertical slice surfaces that in weeks. It also gives the protocol its first
demonstrable, benchmarkable artifact — the seed of credibility.

## Specification

The slice (exact scope to be fixed by the Vision Keeper):

1. **Canonical metadata schema** (RFC-0002) — implemented and enforced.
2. **Two Foundation Engines** — proposed: FE-005 (Context System) and FE-006
   (Behavioral System), because they exercise consent, provenance and real-world data
   from day one.
3. **CKE minimal convergence** — combines the two engines' metadata into one
   explainable, confidence-scored directional estimation.
4. **FE-008 minimal loop** — outcomes registered (RFC-0009, minimal form),
   calibration measured.
5. **One Solver** — proposed: Personal Solver, single narrow question type.

Everything else — remaining engines, knowledge graph at scale, blockchain anchoring,
mirrors — comes after the slice proves the pipeline.

Each component of the slice still requires its own Class 2 RFC before code
(Charter principle 3); this draft only fixes the order of work.

## Validation Criteria

- A real input traverses input → metadata → convergence → estimation → outcome →
  calibration with zero manual steps and a complete provenance chain.
- The estimation output validates against RFC-0000 §13: explainable, weighted,
  versioned, traceable, confidence-scored, non-deterministic.
- Erasure request on the test subject removes every derived unit (privacy gate).

## Premortem

1. **What could fail?** Slice too narrow to be convincing → mitigated: it must run on a
   real use case, not synthetic data.
2. **Wrong assumptions?** Engine pair choice may be suboptimal; the pair is a
   parameter for the Vision Keeper, not a commitment.
3. **Biases?** Designing the schema around the first two engines → mitigated by schema
   round-trip tests against all nine engine specs on paper.
4. **Reversibility?** Full — the slice is v0.x; nothing in it is constitutionally frozen.
5. **Explainability?** The slice's first benchmark *is* explainability end-to-end.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-08 | Draft | — |
| 2026-07-09 | **Accepted** (en-bloc Vision Keeper approval); proposed engine pair FE-005 + FE-006 confirmed | Vision Keeper (Osvaldo) |
