# DRAFT — EE-003 Market Structural Fragility Engine (Bitcoin & Crypto Focus)

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review; implementation gated on source registrations |
| **Class** | 2 (Substantive — Extension Engine, per RFC-0000 §9) |
| **Authors** | **Vision Keeper (Osvaldo)** — goal; Implementation Workforce (Claude — AI, honest redesign and drafting) |
| **Requires** | RFC-0002, RFC-0009, RFC-0014, RFC-0018, RFC-0020; reuses EE-001 (cycles) and EE-002 (concentration) mathematics |
| **Created** | 2026-07-18 |

## Summary

The Vision Keeper's goal: cross all available data — countries, geopolitics, market
structure — to anticipate what happens to Bitcoin, "the way the subprime crisis was
once predicted." This RFC delivers the **honest version of that goal**: the engine
measures **structural fragility** — the measurable preconditions of instability —
and never predicts price. Every probabilistic statement it ever emits must be
pre-registered with falsification criteria and publicly Brier-scored (RFC-0018).

## Why not price prediction — recorded permanently

1. **Constitutional:** RFC-0000 §1 ("SECM is NOT a prediction engine") and §19
   ("SECM does NOT succeed by producing more predictions").
2. **Adversarial efficiency:** BTC is among the most heavily analyzed liquid assets
   on Earth. Signals extractable from public data are competed away by thousands of
   professional quantitative actors with superior data and latency; any residual
   public-data "edge" claim is structurally a survivorship story (see CS-0001).
3. **The subprime lesson, read correctly:** the famous 2008 shorts were not
   data-crossing price predictions. They were **mechanism identification** —
   documented leverage, mispriced risk instruments, and a mechanical trigger (rate
   resets) — held through years of being "wrong" before being right, by people whose
   *subsequent* macro calls mostly failed. The replicable part is mechanism
   monitoring. That is what this engine does.

## Specification (v0.1 scope)

### 1. Inputs — public, registered, verifiable only (RFC-0014 registry)

Candidate sources (each requires Class 2 registration before first ingestion):
derivatives funding rates and open interest (public exchange endpoints); stablecoin
supply and collateral disclosures; on-chain concentration metrics from public
explorers (supply held by largest addresses); exchange volume concentration (HHI —
EE-002 arithmetic); halving-cycle phase (EE-001 arithmetic); global rates and
liquidity (BCB/FRED — partially live via RFC-0020); a dated regulatory/geopolitical
event calendar from primary sources.

### 2. Transformation — fragility indicators, not forecasts

Versioned, documented formulas producing per-dimension fragility readings
(leverage, concentration, collateral quality, liquidity regime, cycle phase), each
citing its inputs. The composite is a **conditions assessment** — "how dry is the
forest" — with explicit uncertainty. It never asserts when or whether ignition
occurs.

### 3. Output

`ECON_FRAGILITY_ASSESSMENT` units (registry amendment on acceptance): domain
(bitcoin/crypto v0.1), per-dimension readings with evidence, composite fragility
band, data coverage statement, and a non-removable disclaimer: *this is a structural
conditions measurement, not a price forecast, not timing, not investment advice.*

### 4. Pre-registration discipline (the CS-0001 rule, made law for this engine)

Any conditional probabilistic statement derived from fragility readings must be
pre-registered per RFC-0018 **before** resolution: explicit claim, resolution date,
falsification criterion, hash-committed. The engine's public Brier record is part of
its output surface. If calibration is no better than naive baselines, the engine
must report exactly that.

### 5. Exclusions — by design, permanently

No price targets. No timing calls. No trade signals. No personalized investment
advice to any user (constitutional and operational boundary). No non-public or
unverifiable data. No narrative sources (attention ≠ truth, RFC-0014 §4).

## Validation Criteria

- Every indicator recomputable by a third party from cited public sources.
- Pre-registration enforcement: no probabilistic output without a registered
  resolution criterion; violations abort emission.
- Calibration reporting present in 100% of assessment outputs once ≥ RFC-0018
  minimum sample exists.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Users read "high fragility" as "sell now" → the disclaimer
   is embedded in the unit itself, and timing is explicitly declared unknowable.
2. **Wrong assumptions?** That fragility indicators carry signal at all — the
   pre-registration + Brier regime measures this instead of assuming it; the engine
   is falsifiable about itself.
3. **Biases?** Doom bias (fragility engines find fragility) → every dimension
   reports both directions and data coverage; calibration exposes systematic alarm.
4. **Reversibility?** Versioned parameters; pure analysis over public data.
5. **Explainability?** Every reading cites formula + sources; every probability
   carries its pre-registration reference.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-18 | Draft, from Vision Keeper goal, honestly redesigned | — |
