# RFC-0002 — Protocol Language: Canonical Metadata Schema

| Field | Value |
|---|---|
| **RFC** | 0002 |
| **Status** | Accepted — 2026-07-09 |
| **Class** | 2 (Substantive) |
| **Authors** | Implementation Workforce (Claude — AI, labeled per RFC-0001 §7) |
| **Requires** | RFC-0000, RFC-0001 |
| **Created** | 2026-07-08 |

## Summary

RFC-0000 §6 defines metadata as the fundamental unit of SECM, but no formal definition
of a metadata unit exists. This draft proposes the canonical envelope every engine must
produce and every consumer (CKE, Solvers, Validation) must accept. It is the protocol's
packet format: everything else depends on it, so it must be specified first.

## Motivation

Without a canonical unit: engines produce incompatible outputs, convergence cannot weigh
them, validation cannot trace them, and auditability (RFC-0000 §22) is a promise instead
of a property of the data. With provenance embedded in every unit, "everything must
remain auditable" becomes structurally guaranteed — and gives any future integrity layer
(e.g., blockchain anchoring) a well-defined object to hash.

## Specification

Every metadata unit is a versioned, immutable record:

```json
{
  "schema_version": "0.1.0",
  "id": "uuid-v7",
  "entity_ref": "graph node id (Person, Organization, City, ...)",
  "semantic_type": "identifier from the Universal Semantic Layer (e.g. PERSON_CONTEXT)",
  "engine": { "id": "FE-005", "version": "0.1.0" },
  "transformation": {
    "name": "human-readable name of the transformation applied",
    "description": "what computation was performed, stated plainly",
    "source_tradition": "origin of the mechanism (e.g. network analysis, Pythagorean encoding)",
    "parameters_hash": "sha256 of the exact parameters used"
  },
  "value": {},
  "confidence": 0.0,
  "provenance": ["ids of input metadata units this was derived from"],
  "created_at": "ISO-8601 timestamp",
  "consent_scope": "reference to the consent under which personal data was processed"
}
```

Rules:

1. **No unit without provenance.** Root units reference their raw-input descriptor.
   For identifying inputs, the descriptor records only the semantic type (e.g.,
   `PERSON_NAME`) and the transformation applied — never the raw value, never a naive
   hash of it (Privacy Architecture, Tier 0: identifying inputs are ephemeral).
2. **No unit without an explicit transformation description** — including
   `source_tradition`, so the origin of every mechanism is auditable end-to-end
   (RFC-0000 §4 + §22: neutral exposure at UI level, full transparency at audit level).
3. **Units are immutable.** Corrections create new units that supersede old ones via
   provenance; history is never rewritten (RFC-0000 §14).
4. **Confidence is mandatory** and must be calibratable (see draft: Outcome Registry).
5. **`consent_scope` is mandatory for any unit derived from personal data**
   (see draft: Privacy Architecture; RFC-0001 §4 rank 1).

## Validation Criteria

- Round-trip test: every Foundation Engine output validates against the schema.
- Traceability test: from any convergence output, the full provenance chain reconstructs
  to raw-input descriptors with zero gaps.
- Schema versioning test: consumers reject units with unknown major versions.

## Premortem

1. **What could fail?** Schema too rigid for future engines → mitigated by semantic
   versioning and an extensible `value` field.
2. **Wrong assumptions?** That one envelope fits all engines; the reference slice
   (see draft) exists to test this cheaply.
3. **Biases?** Envelope design biased toward person-entities; graph entity types from
   RFC-0000 §12 are all first-class in `entity_ref`.
4. **Reversibility?** Schema changes are Class 2 RFCs; old units remain valid under
   their recorded `schema_version`.
5. **Explainability?** The `transformation` block makes every unit self-explaining.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-08 | Draft | — |
| 2026-07-09 | **Accepted** | Vision Keeper (Osvaldo) |
