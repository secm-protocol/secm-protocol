# DRAFT — Outcome Registry: The Historical Knowledge Brain

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review |
| **Class** | 2 (Substantive) |
| **Authors** | **Vision Keeper (Osvaldo)** — concept; Implementation Workforce (Claude — AI, drafting) |
| **Requires** | RFC-0000, RFC-0001, draft-metadata-schema, draft-privacy-architecture |
| **Created** | 2026-07-08 |

## Summary

A historical data brain that updates as evidence is found and scientifically confirmed.
The more people use the protocol, the richer it becomes — building a knowledge base
capable of powering engines that help people in specific subjects and niches. This is
the component that closes the protocol's learning loop: it connects the Historical
Pattern System (FE-004), the Validation Engine (FE-008) and the Evolution Engine
(FE-009) into a single evidence cycle.

## Motivation

RFC-0000 §17 states that only validated convergence may influence protocol evolution,
and §13 requires confidence-scored outputs — but no component stores **observed
outcomes** to validate against. Without an outcome registry: confidence cannot be
calibrated, engine weights cannot be earned by evidence (RFC-0001 §6), and the protocol
cannot honestly claim to reduce uncertainty. With it, every directional estimation
eventually meets reality, and reality updates the brain.

## Specification

### 1. Outcome records

An outcome is a metadata unit (canonical schema) recording what actually happened,
linked by provenance to the directional estimations that preceded it. Per RFC-0000 §17
it is typed as **subjective perception**, **objective outcome** or **observed evidence** —
never merged.

### 2. Evidence tiers

Knowledge in the brain carries an evidence tier, and only climbs tiers through
confirmation:

| Tier | Meaning |
|---|---|
| **E0** | Reported (unverified feedback) |
| **E1** | Observed (documented objective outcome) |
| **E2** | Statistically validated (pattern significant across population, FE-008) |
| **E3** | Independently replicated / scientifically confirmed |

Convergence weight contributions scale with tier. E0 alone never changes protocol
behavior.

### 3. The learning loop

```
Estimation → Outcome registered → FE-008 calibration →
engine weights recalibrated → FE-004 historical patterns updated →
FE-009 records the evolution → richer estimations
```

Confidence calibration is measured continuously (e.g., calibration error / Brier score:
when the protocol says 70%, it must be right ~70% of the time).

### 4. Network enrichment — with privacy as a hard boundary

The brain grows from **anonymized, aggregated, non-re-identifiable** data only
(Privacy Architecture §4). Individual records stay in the erasable tier and belong to
the person. Population-level patterns — person × place, person × context, trajectory ×
outcome — become collective knowledge only above re-identification thresholds.

### 5. Niche engines

When the brain accumulates E2+ knowledge in a specific domain (a profession, a region,
a life transition), that cluster can be proposed as an **Extension Engine** via the
normal RFC pipeline — engines born from evidence, not from opinion.

## Validation Criteria

- Calibration: measured calibration error decreases as outcome volume grows.
- Tier integrity: no E0/E1 data influences convergence weights.
- Privacy: aggregate extraction passes the re-identification tests of the Privacy
  Architecture.
- Traceability: every brain update traces to the outcomes that justified it.

## Premortem

1. **What could fail?** Feedback loops amplifying popular-but-wrong patterns →
   mitigated by tier system: only E2+ influences behavior, and E3 requires independent
   replication.
2. **Wrong assumptions?** That enough outcomes will be volunteered; mitigation:
   consent-first UX design and value returned to contributors (their own calibrated
   history).
3. **Biases?** Early-adopter population bias → population coverage must be reported
   alongside every aggregate; FE-008 flags low-coverage domains.
4. **Reversibility?** Brain updates are versioned (FE-009); any recalibration can be
   rolled back to a prior registered state.
5. **Explainability?** Every weight change cites its evidence tier and outcome set.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-08 | Draft | — |
