# DRAFT — Environmental Ingestion: The Protocol Updates Its World Model

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review |
| **Class** | 2 (Substantive) |
| **Authors** | **Vision Keeper (Osvaldo)** — concept; Implementation Workforce (Claude — AI, drafting) |
| **Requires** | RFC-0000, draft-metadata-schema, draft-outcome-registry, draft-privacy-architecture |
| **Created** | 2026-07-09 |

## Summary

The RX analyzes people against their environment: places, culture, politics, economy,
religion — everything societies and organizations do. A protocol whose world model is
frozen degrades silently. This draft defines **scheduled, automated ingestion
pipelines** that feed the protocol current population-level context — the same
scheduled-automation mechanism commonly used to trigger daily social media posts
(GitHub Actions cron), pointed **inward** instead of outward: instead of publishing,
the protocol feeds itself.

## Motivation

Directional estimation is alignment between person and environment (RFC-0000 §5). The
person's side arrives fresh with every RX; the environment's side must also stay
alive. Manual updates do not scale and silently lapse. Automated ingestion keeps the
context layer current — under constitutional constraints that prevent it from becoming
a firehose of noise.

## Specification

### 1. Trigger mechanism

Ingestion runs as **scheduled jobs** (initially GitHub Actions `schedule:` workflows;
the mechanism is replaceable — the contract is the schedule, not the vendor). Each run
is logged, versioned and reproducible.

### 2. Public source registry

Every feed is declared in a public registry before first ingestion: name, URL/API,
license and terms compliance, update cadence, source class, and which semantic
identifiers it feeds (e.g., `ECON_INDICATOR`, `PLACE_CITY`, `EVENT_HISTORICAL`).
**No undeclared sources** — a hidden feed is a hidden transformation (RFC-0000 §22).
Registry changes are Class 2.

### 3. Data lands as canonical metadata

Ingested data becomes standard metadata units: `entity_ref` = graph entities,
provenance = the registry entry + run id, engine = the ingestion pipeline version.
**Never personal data.** Ingestion touches only population-level, public,
institutional-scale information — societies, places, economies, organizations — never
individuals.

### 4. Evidence tiers are enforced at the gate

- **Official/statistical sources** (statistics bureaus, central banks, scientific
  publications): enter at **E1** (observed, documented).
- **Attention signals** (trends, engagement, media volume): enter at **E0**, and are
  labeled as *attention metadata*. **Attention measures what is loud, not what is
  true.** The convergence engine must never treat attention as evidence of fact — it
  is context about where collective focus is, nothing more.
- Nothing ingested changes engine weights or protocol behavior without FE-008
  validation (RFC-0000 §17: feedback is metadata, not truth). Climbing tiers requires
  the Outcome Registry's confirmation process.

### 5. Staleness is visible

Every context unit carries its ingestion timestamp. Estimations exposed to users
reflect context freshness in their confidence — stale context widens uncertainty
honestly instead of pretending the world hasn't moved.

### 6. Dependency

This RFC defines architecture. Live pipelines require the vertical slice (storage +
FE-005 Context) to exist first. Nothing ships before its implementation RFC.

## Validation Criteria

- **Reproducibility:** the same feed snapshot always produces identical metadata units.
- **Auditability:** every context unit traces to a registry entry and a logged run.
- **Personal-data test:** ingestion output contains zero person-level records.
- **Tier enforcement:** attention-class sources cannot produce units above E0;
  automated feeds cannot produce units above E1.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Poisoned or manipulated feeds steering context → mitigations:
   public source registry with review, multiple independent sources per domain,
   E-tier caps, FE-008 gate before any behavioral influence.
2. **Wrong assumptions?** That sources stay available — feeds die; mitigation:
   staleness labeling and graceful degradation, never silent reuse of dead data.
3. **What biases may emerge?** Source selection bias (whose statistics? whose media?)
   → the registry is public, Class 2 governed, and must state coverage limitations per
   source; attention metadata is structurally segregated from factual metadata.
4. **How is reversibility guaranteed?** Ingested units are versioned and provenance-
   chained; a compromised source's entire output is identifiable and removable in one
   operation.
5. **How is explainability preserved?** Any estimation influenced by ingested context
   can name the exact sources, runs and tiers behind it.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-09 | Draft | — |
