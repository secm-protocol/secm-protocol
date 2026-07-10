# DRAFT — Structural-First Priority Amendment

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review (implementation on `feature/rfc-0021-structural-engines`) |
| **Class** | 3 (Constitutional — amends RFC-0013 priority order) |
| **Authors** | Chief Architecture Intelligence (GPT — AI, relayed by Vision Keeper); Vision Keeper (Osvaldo) — adoption decision; Implementation Workforce (Claude — AI, reconciliation and drafting) |
| **Requires** | RFC-0000, RFC-0001, RFC-0012, RFC-0013 |
| **Created** | 2026-07-09 |

## Summary

The Vision Keeper relayed an architectural directive from the Chief Architecture
Intelligence arguing that the protocol must build a person's **structural metadata**
before any question-answering layer. This RFC adopts that intent, reconciled with the
constitution the Vision Keeper already ratified: no new Foundation Engine is created
(RFC-0000 §8 fixes FE-001..FE-009 identity), and no AI proposal carries supersession
authority over prior ratified decisions (RFC-0001 §7) — the reordering is adopted
because the Vision Keeper decided to adopt it, on 2026-07-09.

## Motivation

RFC-0013 deliberately chose FE-005 (Context) and FE-006 (Behavioral) as the first two
engines, to exercise consent, provenance and real-world data early. That choice paid
off: RX-000001 surfaced a real architectural gap (readings answered nothing) within
the same day. But it also means FE-001 (Nominal Encoding) and FE-002 (Temporal
Encoding) — named in RFC-0000 §8 since Genesis — remain unbuilt. The directive's core
claim has merit: "who is this person structurally" is a real, missing layer, and
building it does not require inventing new constitutional structure.

## What is adopted, and what is not

**Adopted:**
- Priority: implement FE-001 and FE-002 next, as the next structural-identity engines.
- Principle: metadata before direction, restated as already-largely-true of the
  existing pipeline (RFC-0000 §1, §13) and reinforced going forward.
- The "Personal Metadata Graph" concept, mapped onto the **already-reserved RFC-0004
  slot** (Universal Knowledge Graph) rather than a new structure — v0.1 scope: a
  read-side aggregation over existing metadata units by `entity_ref`, not new storage.

**Not adopted, with reasons:**
- **No FE-000.** RFC-0000 §8 fixes Foundation Engine identity; inventing a new engine
  number is an unforced constitutional change with no benefit — everything requested
  (nominal, temporal, structural, behavioral, contextual, historical, environmental,
  linguistic layers) already maps onto FE-001 through FE-006 as named at Genesis.
- **No unilateral supersession.** Per RFC-0001 §7, AI proposals carry no special
  weight and enter the same RFC process as any other. This document is adopted by
  Vision Keeper decision, not by the directive's own claim of authority.
- **RFC-0013 and RFC-0018/0019 (the vertical slice) are not reverted.** They shipped
  real value (a working end-to-end pipeline, a real bug found and fixed the same day).
  They remain accepted history; this RFC only reorders what comes *next*.

## Specification

1. Implement **FE-001 Nominal Encoding System v0.1** (RFC-0022 draft) and
   **FE-002 Temporal Encoding System v0.1** (RFC-0023 draft) — both consuming Tier-0
   ephemeral inputs (`PERSON_NAME`, `PERSON_BIRTH_DATE`) already defined in RFC-0011,
   never exposing mystical terminology (RFC-0000 §4), confidence deliberately low and
   labeled unvalidated (no established evidence connects these historical
   transformations to real outcomes — RFC-0001 §6 governs their path to any weight).
2. Add a minimal **Personal Metadata aggregation** (`secm.graph`), scoped to RFC-0004:
   groups a person's existing metadata units by namespace. No new storage; a query
   over what already exists.
3. **RFC-0021 "Directional Hypotheses" (the not-yet-numbered draft from RX-000001
   feedback) is PAUSED, not rejected.** It remains on its feature branch, unmerged,
   pending this structural foundation. It answered a real problem (readings that said
   nothing) and its evidence-linked hypothesis design is sound; the CAI's separate
   suggestion — that hypothesis ranking belongs in the CKE (Protocol Core, RFC-0012)
   rather than the Solver — is noted as a good idea for that draft's eventual revision.
4. FE-001/FE-002 outputs are **not yet wired into CKE convergence** — RFC-0017 fixed
   `EXPECTED_ENGINES` to the slice pair deliberately; extending it is a future Class 2
   decision once these engines exist and their weight-earning path is considered.

## Validation Criteria

- FE-001 and FE-002 produce units validating under RFC-0007 strict mode.
- No end-user-facing string in either engine matches banned terminology (Life Path,
  Soul Number, Expression Number, astrology, Kabbalah, gematria — RFC-0000 §4).
- Output values are irreversible to the raw identifying input by construction
  (stronger than hashing, per RFC-0008's own warning that hashing low-entropy personal
  data is not anonymization).

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Treating this as license to keep reprioritizing on every new
   external directive → the Immutable Core and RFC-0001 §7 remain the check: AI input
   is always advisory, the Vision Keeper's ratified RFCs stand until *he* reopens them.
2. **Wrong assumptions?** That FE-001/002 belong before further Solver work — they
   are additive (new metadata), not blocking; the paused hypotheses draft can resume
   in parallel whenever the Vision Keeper prefers.
3. **Biases?** none beyond the founder's own priority call, which is his to make.
4. **Reversibility?** Full — nothing prior is deleted; this is sequencing, not erasure.
5. **Explainability?** This document itself is the explanation: what was adopted, what
   was not, and why, in writing.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-09 | Draft, adopting CAI directive per Vision Keeper decision ("adotar as instruções") | Vision Keeper (Osvaldo) |
