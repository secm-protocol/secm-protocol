# DRAFT — Privacy Architecture: Data Protection by Design

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review |
| **Class** | 3 (Constitutional — implements precedence rank 1) |
| **Authors** | Vision Keeper (Osvaldo — requirement); Implementation Workforce (Claude — AI, drafting) |
| **Requires** | RFC-0000, RFC-0001, draft-metadata-schema |
| **Created** | 2026-07-08 |

## Summary

SECM processes personal data: names, birth dates, locations, context, behavior, history.
The Vision Keeper has established that people's data must be protected as a founding
requirement. This draft makes protection structural — not a feature added later — and
resolves the built-in conflict between immutable historical registration (RFC-0000 §14)
and a person's right to erase their data (LGPD/GDPR), using the precedence hierarchy
(RFC-0001 §4: human protection ranks above historical preservation).

## Motivation

A protocol whose mission is to help people cannot be architected in a way that can harm
them. Retrofitting privacy after v1.0 would require breaking the metadata schema, the
knowledge graph and any integrity anchoring — doing it first costs almost nothing.

## Specification

1. **Consent is the root of every personal-data chain.** No metadata unit derived from
   personal data exists without a `consent_scope` reference recording what was consented,
   when, and for which purposes. Processing beyond scope is a protocol violation.
2. **Data minimization.** Engines receive only the semantic identifiers their
   transformation requires (this is Zero Trust, RFC-0000 §15, applied internally).
3. **Two-tier storage:**
   - **Erasable tier:** all personal data and derived personal metadata live in
     erasable storage. A person's erasure request removes their data and all derived
     units in the provenance chain.
   - **Permanent tier:** only content-free artifacts are permanent — hashes,
     version records, DOIs, aggregate statistics that cannot be re-identified.
     Any future blockchain anchoring stores **hashes only**, never content. Proof of
     existence survives erasure; the content does not.
4. **The "historical brain" learns from anonymized aggregates.** Population-level
   patterns (see draft: Outcome Registry) are computed over anonymized, aggregated,
   non-re-identifiable data. Individual records never migrate into permanent collective
   knowledge.
5. **Right of access:** a person can receive every metadata unit derived from their
   data, with its full provenance — the audit trail (RFC-0000 §22) doubles as the
   transparency guarantee to the data subject.

## Validation Criteria

- Erasure test: after an erasure request, no unit in any store resolves to the person;
  permanent-tier artifacts reveal nothing about them.
- Consent test: attempting to create a personal-data unit without `consent_scope` fails
  at the schema level.
- Re-identification test: aggregates published to the permanent tier resist standard
  re-identification attacks (k-anonymity threshold to be fixed at implementation RFC).

## Premortem

1. **What could fail?** Erasure cascades could be incomplete → mitigated by
   provenance-chain traversal tests as a release gate.
2. **Wrong assumptions?** That hash-only anchoring satisfies all jurisdictions; legal
   review required before any public anchoring goes live.
3. **Biases?** Aggregation thresholds may erase small-population signals; thresholds are
   tunable by Class 2 RFC.
4. **Reversibility?** Strengthening privacy is always allowed; weakening it requires
   Class 3 and cannot cross precedence rank 1.
5. **Explainability?** Consent and provenance make every processing step explainable to
   the data subject themself.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-08 | Draft | — |
