# RFC-0019 — Personal Solver v0.1: The Human-Readable Reading

| Field | Value |
|---|---|
| **RFC** | 0019 |
| **Status** | Accepted — 2026-07-09 |
| **Class** | 2 (Substantive — first Solver, per RFC-0000 §10) |
| **Authors** | Implementation Workforce (Claude — AI, labeled per RFC-0001 §7) |
| **Requires** | RFC-0002, RFC-0011, RFC-0013, RFC-0017 |
| **Created** | 2026-07-09 |

## Summary

The first Solver: translates one `PERSON_DIRECTIONAL_ESTIMATION` into a
human-readable **reading** — plain-language statements, each citing the exact
evidence behind it, with confidence stated in words and numbers and the
constitutional disclaimer embedded. Solvers never create knowledge (RFC-0000 §10):
v0.1 is a deterministic, versioned, rule-based renderer — transparent IF-THEN rules,
never generated prose, never hidden wisdom.

## Motivation

The estimation is machine-auditable; people need language. This is the piece that
makes the first end-to-end RX possible — and the piece where invented advice could
sneak in, so v0.1 is deliberately constrained to renderable, auditable rules.

## Specification

### 1. Input / output

`solve(estimation)` → one `PERSON_DIRECTIONAL_READING` unit (registry amendment;
`PERSON_` namespace → consent enforced automatically). Confidence is **inherited from
the estimation, never higher**. Provenance: the estimation id.

### 2. Statements — every sentence cites its evidence

The value carries `statements[]`, each `{text, based_on[]}` where `based_on` lists the
`provenance_ref`s of the signals used. Statement sources, all deterministic:

1. **Declaration rendering** — behavioral axes and context profile restated in plain
   words ("Declared risk posture: calculated — risks only after planning").
2. **Environment rendering** — regional indicators considered, or the honest absence:
   "No regional environment data was available; this reading rests on personal
   declarations only."
3. **Alignment observations** — a small versioned rule table (v0.1: 4 generic rules)
   over axis-label combinations, e.g. *long horizon + measured risk → "the declared
   pattern is consistent with gradual, planned moves rather than abrupt changes."*
   Rules are IF-THEN entries in the `parameters_hash`; adding or changing one is
   Class 2. No rule matched → the reading says the combined evidence is insufficient
   for an alignment observation.

### 3. Confidence, stated honestly

`confidence` block: numeric score, a wording band (low / moderate-low / moderate /
relatively high — the top band still says "hypothesis"), and `reasons[]` naming what
moved it: engine coverage, environment gaps, and always: *"engine weights are an
unvalidated uniform prior (RFC-0017)"*.

### 4. Constitutional disclaimer — non-removable

Every reading embeds: the protocol **estimates directions, never destiny**
(RFC-0000 §2); the reading is a hypothesis; registering the real outcome
(RFC-0018 loop) is what makes future readings better. Locale translations of all
templates are Class 1 once canonical text is approved (RFC-0003 §4).

## Validation Criteria

- Reading validates under RFC-0007 strict mode; confidence equals the estimation's.
- Every statement's `based_on` resolves to signal refs present in the estimation.
- Rule table determinism: same estimation → identical statements.
- Disclaimer present in 100% of readings; absence is a release-blocking failure.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Rule statements read as validated advice → each reading
   carries the unvalidated-prior reason and hypothesis framing; rules are visible
   IF-THEN text, not authority.
2. **Wrong assumptions?** That 4 generic rules are useful — they are a floor to prove
   the pipeline; domain-specific rules come as Class 2 RFCs, ideally evidence-born
   (RFC-0009 §5).
3. **Biases?** Template wording bias → canonical text is versioned and reviewable;
   locale files keep meaning fixed.
4. **Reversibility?** Versioned rule tables; old readings valid under recorded hashes.
5. **Explainability?** A reading is the only user-facing artifact — and every sentence
   in it names its evidence.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-09 | Draft; implementation on feature branch per CONTRIBUTING flow | — |
| 2026-07-09 | **Accepted** — merged to `develop`, 67/67 tests green | Vision Keeper (Osvaldo) |
