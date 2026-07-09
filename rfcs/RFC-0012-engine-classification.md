# RFC-0012 — Engine Classification: Transformation Engines vs Protocol Core Services

| Field | Value |
|---|---|
| **RFC** | 0012 |
| **Status** | Accepted — 2026-07-09 |
| **Class** | 3 (Constitutional — touches Foundation Engine structure) |
| **Authors** | Implementation Workforce (Claude — AI, labeled per RFC-0001 §7) |
| **Requires** | RFC-0000, RFC-0001 |
| **Created** | 2026-07-08 |

## Summary

RFC-0000 §8 lists nine Foundation Engines, but they are two different kinds of thing.
FE-001..FE-006 are **transformation engines**: they receive input and produce metadata.
FE-007 (Convergence), FE-008 (Validation) and FE-009 (Evolution) operate **on the
outputs of the other engines** — they are protocol infrastructure. This draft proposes
classifying them accordingly, without removing anything.

## Motivation

The rule "no new Foundation Engine after v1.0" protects protocol identity — correct for
the encoders. But applied to FE-007/008/009 it would freeze the convergence algorithm,
validation methodology and evolution mechanics forever. Those must be versionable and
improvable through the RFC process, or the protocol cannot follow its own §14.

## Specification

1. **Foundation Engines (identity, permanent):** FE-001..FE-006. Frozen after v1.0 per
   RFC-0000 §8. Weights in convergence remain governed by FE-008 (RFC-0001 §6).
2. **Protocol Core Services (infrastructure, versionable):** Convergence, Validation,
   Evolution — relocated to the Protocol Core layer, which already exists in the
   constitutional architecture (RFC-0000 §7). Their *existence* is constitutional and
   permanent; their *strategies and algorithms* are versioned artifacts evolved via
   Class 2 RFCs.
3. IDs preserved for historical continuity (FE-007/008/009 remain valid aliases).

## Validation Criteria

- The layered architecture diagram (RFC-0000 §7) maps every component to exactly one layer.
- A convergence-strategy upgrade can be proposed, benchmarked and adopted via Class 2
  RFC without touching any constitutional text.

## Premortem

1. **What could fail?** Perceived as weakening the constitution → mitigated: nothing is
   removed; the three services become *more* protected (constitutional existence) while
   their algorithms become honestly improvable.
2. **Wrong assumptions?** That no transformation engine will ever need core privileges;
   if one does, that is a Class 3 discussion.
3. **Biases?** None identified beyond architectural taste; decision rests with the
   Vision Keeper.
4. **Reversibility?** Full — classification is documentation-level until v1.0.
5. **Explainability?** Improves it: each component's role becomes unambiguous.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-08 | Draft | — |
| 2026-07-09 | **Accepted** (en-bloc Vision Keeper approval) | Vision Keeper (Osvaldo) |
