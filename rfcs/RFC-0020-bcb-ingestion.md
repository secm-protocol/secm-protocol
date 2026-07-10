# RFC-0020 — First Live Ingestion Pipeline: Banco Central do Brasil (SGS)

| Field | Value |
|---|---|
| **RFC** | 0020 |
| **Status** | Accepted — 2026-07-09 |
| **Class** | 2 (Substantive — first RFC-0014 pipeline + FE-005 amendment) |
| **Authors** | Implementation Workforce (Claude — AI, labeled per RFC-0001 §7) |
| **Requires** | RFC-0002, RFC-0007, RFC-0014, RFC-0015 |
| **Created** | 2026-07-09 |

## Summary

The protocol's first live feed: a scheduled GitHub Actions pipeline ingesting three
official Banco Central do Brasil series — Selic target (`interest_rate`), IPCA
(`inflation`), USD/BRL (`exchange_rate`) — as canonical `ECON_INDICATOR` units,
validated by the RFC-0007 validator before anything is stored. Also amends FE-005
with **hierarchical region matching**, so national indicators (`BR`) pair with
sub-regions (`BR-Sudeste`).

## Motivation

RFC-0014 defines the architecture; this ships the first real source — exactly the
three indicators the FE-005 relevance map already consumes for finances/business
domains. API verified live on 2026-07-09 (Selic 14.25%, IPCA 0.58%, USD 5.1329).

## Specification

1. **Source:** BCB SGS open-data API, registered in
   [`ingestion/SOURCE-REGISTRY.md`](../../ingestion/SOURCE-REGISTRY.md) (RFC-0014 §2).
   Series 432, 433, 1. Source class: official statistics → E1 ceiling.
2. **Pipeline (`secm.ingestion.bcb`):** fetches the latest observations (requests
   `ultimos/5` and takes the most recent — the single-item endpoint proved flaky in
   live verification), normalizes decimal formats, and emits `ECON_INDICATOR` units:
   region `BR`, engine `INGEST-BCB`, confidence **0.95** (parameter; official source,
   still not a measurement of truth), provenance = the registry entry ID.
3. **Validation gate:** every unit must pass the RFC-0007 validator in strict mode
   **inside the pipeline** — an invalid unit aborts the run. Nothing unvalidated is
   ever stored.
4. **Storage v0.1:** `data/environment/bcb-latest.json`, committed to `develop` by the
   scheduled workflow (public, non-personal, auditable via git history). A proper
   storage layer is future Class 2 work.
5. **Schedule:** GitHub Actions cron, daily 09:00 UTC, plus manual dispatch.
6. **FE-005 amendment — hierarchical region matching:** a country-level environment
   unit (region `BR`) pairs with any of its sub-regions (`BR-*`). Exact match still
   applies otherwise. FE-005 version bumps to 0.2.0; on acceptance, RFC-0015 receives
   a status-history amendment line. Without this, national indicators would silently
   never pair — a real bug found by shipping something real.

## Validation Criteria

- Offline: unit construction, decimal parsing (`"11,25"` and `"0.58"`), strict
  validation, indicator names ⊂ FE-005 relevance map, hierarchical pairing test.
- Live: one successful scheduled run committing validated units.
- Staleness: units carry `created_at`; FE-005 freshness factors apply downstream.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** API shape changes silently → the strict validation gate
   aborts the run loudly; the workflow surfaces the failure.
2. **Wrong assumptions?** That national-level indicators are useful context for
   sub-regional questions — true for macro rates (they bind nationally), but the
   pairing is labeled with its region so the audit trail shows granularity.
3. **Biases?** Single-country coverage at launch → the registry lists candidate
   global sources; coverage gaps remain visible via FE-005 markers.
4. **Reversibility?** Data commits are plain git history; the workflow can be
   disabled in one commit.
5. **Explainability?** Every unit names its series, registry entry, reference date
   and run.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-09 | Draft; implementation on feature branch per CONTRIBUTING flow | — |
| 2026-07-09 | **Accepted** — merged to `develop`, 73/73 tests, first live run committed | Vision Keeper (Osvaldo) |
