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

### Founding rule (Vision Keeper directive)

When a person runs their RX, they provide personal data as **input**. Identifying data
is **deliberately never stored**. What the protocol keeps is behavior, positioning and
context — de-identified — because what serves the mission is understanding direction
(individual and collective), never knowing who the person is.

1. **Ephemeral identity processing (Tier 0).** Identifying inputs — name, birth date,
   precise location, and anything re-identifying — exist only in volatile memory for
   the duration of the computation session. Engines consume them, produce derived
   metadata, and the identifying inputs are destroyed at session end. They are never
   written to durable storage, logs, caches or backups. The derived encodings that
   persist (e.g., a nominal or temporal encoding value) are non-identifying values
   carrying their transformation record, never the raw input.
   - **Honest technical note:** hashing is not anonymization for low-entropy data —
     a hashed name or birth date is trivially reversible by dictionary attack.
     Therefore provenance records for identity-derived units store only the semantic
     type used (e.g., `PERSON_NAME`) and the transformation applied — never the raw
     value and never a naive hash of it.
2. **Consent is the root of every personal-data chain.** No metadata unit derived from
   personal data exists without a `consent_scope` reference recording what was consented,
   when, and for which purposes. Processing beyond scope is a protocol violation.
3. **Data minimization.** Engines receive only the semantic identifiers their
   transformation requires (this is Zero Trust, RFC-0000 §15, applied internally).
   Stored behavioral and contextual metadata is generalized against fingerprinting:
   quasi-identifiers are bucketed after computation (exact birth date → age band,
   precise location → region) before persistence.
4. **Storage tiers:**
   - **Tier 0 — ephemeral (identity):** volatile memory only, destroyed per session
     (rule 1). Nothing identifying survives the RX computation.
   - **Erasable tier (behavior):** de-identified behavioral, positional and contextual
     metadata, keyed only by an anonymous continuity token (rule 5). Erasable on
     request by whoever presents the token.
   - **Permanent tier:** only content-free artifacts — hashes of protocol documents,
     version records, DOIs, aggregate statistics that cannot be re-identified.
     Any future blockchain anchoring stores **hashes only**, never content.
5. **Continuity token — longitudinal linkage without identity.** The learning loop
   (draft: Outcome Registry) needs to connect a person's later outcomes to their
   earlier estimations. Since the protocol stores no identity, linkage works through a
   **random anonymous token generated at RX time and held by the person** — the
   protocol stores only the token, linkable to that person's de-identified metadata but
   to nothing else. Presenting the token reconnects the history; losing it breaks the
   chain permanently — that is the honest price of identity-free design, and it is
   accepted. The token also serves as proof of ownership for erasure and access rights.
6. **The "historical brain" learns from anonymized aggregates.** Population-level
   patterns — behavior × context, positioning × trajectory, mass dynamics — are
   computed over anonymized, aggregated, non-re-identifiable data. Individual records
   never migrate into permanent collective knowledge.
7. **Right of access and erasure — via token.** Whoever presents a continuity token can
   receive every metadata unit linked to it, with full provenance (the audit trail of
   RFC-0000 §22 doubles as the transparency guarantee), and can have all of it erased.

## Validation Criteria

- **Tier 0 test:** after an RX session ends, a full storage audit (databases, logs,
  caches, backups, crash dumps) finds zero identifying inputs. This is a release gate,
  not a promise.
- **Erasure test:** presenting a continuity token and requesting erasure removes every
  linked unit in every store; permanent-tier artifacts reveal nothing about the person.
- **Consent test:** attempting to create a personal-data unit without `consent_scope`
  fails at the schema level.
- **Re-identification test:** stored behavioral metadata and published aggregates
  resist standard re-identification attacks (k-anonymity threshold and bucketing rules
  fixed at implementation RFC).
- **Provenance leak test:** no provenance record of an identity-derived unit contains
  a raw identifying value or a naive hash of one.

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
