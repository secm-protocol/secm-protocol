# DRAFT — EE-001 Cycle Analysis Engine: Periodicity in Real Time Series

| Field | Value |
|---|---|
| **Status** | Draft — **deferred by design**: implementation gated on data prerequisites |
| **Class** | 2 (Substantive — first Extension Engine, per RFC-0000 §9) |
| **Authors** | **Vision Keeper (Osvaldo)** — concept; Implementation Workforce (Claude — AI, drafting) |
| **Requires** | RFC-0002, RFC-0009, RFC-0014, and live time-series data |
| **Created** | 2026-07-09 |

## Summary

The first Extension Engine candidate: spectral/cycle analysis over the **real time
series** the protocol accumulates — economic indicators (RFC-0014 ingestion),
population outcome patterns (RFC-0009 brain), and later individual trajectory rhythms
(continuity-token returns). It detects statistically significant periodicities and
emits them as cycle-phase context metadata that FE-005 can pair into estimations.

## Honest provenance of the idea

Inspired by Nikola Tesla's **documented** engineering legacy: resonance, frequency,
alternating current — real, testable physics. The famous "energy, frequency and
vibration" quote attributed to Tesla has **no verified primary source**, and the
protocol does not adopt quotes or beliefs; it decomposes mechanisms (RFC-0000 §3).
The extractable computational transformation is spectral analysis of periodic
phenomena — nothing more, and that is enough.

## Motivation

Cycles are real and documented where this engine will look: business and interest-rate
cycles, seasonality in economic indicators, weekly/annual rhythms in mass behavior.
Knowing the cycle phase of a region's environment is genuine directional context
("this indicator is historically near a contraction phase") that no current engine
provides.

## Specification (v0.1 scope)

1. **Inputs:** time series of `ECON_INDICATOR` units per region/indicator (RFC-0014)
   and aggregated outcome-pattern series (RFC-0009, anonymized aggregates only).
   Individual trajectory rhythms are explicitly **phase 2** — they require many
   continuity-token returns to exist.
2. **Transformation:** spectral analysis (Fourier-family / periodogram) plus
   significance testing: a detected periodicity is emitted **only** when it passes a
   permutation-based significance threshold and persists out-of-sample. Cycle-hunting
   in noise finds ghosts; the significance gate is the exorcist.
3. **Outputs:** `ECON_CYCLE_PHASE` units (registry amendment on acceptance): indicator,
   region, detected period, current phase, significance level — never personal data.
4. **Hard data gate:** no series shorter than **3× the longest candidate period** may
   be analyzed (you cannot claim an annual cycle from 14 months of data). Below the
   gate the engine emits nothing — absence over invention, as always.
5. **Weight:** earned via FE-008 like every engine (RFC-0001 §6). Extension Engine
   pipeline applies in full: technical, architectural, security, benchmark,
   explainability validations + consensus (RFC-0000 §9).

## What this engine will never be

No "personal frequencies," no numerological vibration, no 3-6-9 patterns, no cosmic
framing — RFC-0000 §20 applies, and user-facing terminology stays neutral (§4). If a
proposed use cannot name the measured time series behind it, it does not belong here.

## Validation Criteria

- Synthetic-signal test: engine recovers known periodicities injected into synthetic
  series, and stays silent on white noise (false-positive rate below threshold).
- Out-of-sample persistence: detected cycles must hold on data the detector never saw.
- Every emitted unit names its series, window, period, phase and significance.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Spurious periodicities from multiple comparisons → permutation
   significance + out-of-sample gate; silence is the default.
2. **Wrong assumptions?** That cycles detected in the past persist — regime changes
   break cycles; staleness and rolling revalidation apply (RFC-0014 §5 spirit).
3. **Biases?** Esoteric misreading of "cycles" by users → neutral terminology and the
   explicit exclusion section above are part of the specification, not decoration.
4. **Reversibility?** Pure analysis over stored series; versioned parameters; nothing
   destructive.
5. **Explainability?** Every cycle claim cites its data window and significance — an
   auditor can recompute it.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-09 | Draft, deferred until data prerequisites are met | — |
| 2026-07-09 | Concept approved for the pipeline ("se for de valor e ajudar, sim") | Vision Keeper (Osvaldo) |
