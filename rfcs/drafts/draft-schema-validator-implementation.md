# DRAFT — Reference Implementation: RFC-0002 Metadata Unit Validator

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review (implementation on `feature/rfc-0007-schema-validator`, merge gated on acceptance) |
| **Class** | 2 (Substantive — first protocol code) |
| **Authors** | Implementation Workforce (Claude — AI, labeled per RFC-0001 §7) |
| **Requires** | RFC-0002 (accepted), draft-semantic-layer |
| **Created** | 2026-07-09 |

## Summary

The first piece of the vertical slice: a reference implementation of the RFC-0002
canonical metadata unit — the validator every engine, the CKE and every Solver will
depend on. It implements RFC-0002 exactly as specified, nothing beyond it.

## Motivation

Everything in the protocol produces or consumes metadata units. If the envelope is not
enforced in code, RFC-0002 is prose. This validator is the smallest artifact that turns
the constitution into running software, and every future engine builds on it.

## Specification

### Language and dependencies

- **Python 3.11+**, **standard library only** for the core (no dependencies to audit,
  runs anywhere, maximizes readability — a reference implementation optimizes for
  auditability per RFC-0000 §22). `pytest` for tests only.
- The protocol remains language-independent (RFC-0000 §11): this is *a* reference
  implementation, not *the* implementation. Future ports (e.g., Rust for performance)
  are new Class 2 RFCs validated against the same test vectors.

### Layout

```
implementation/
  pyproject.toml
  src/secm/
    __init__.py
    registry.py    # Universal Semantic Layer v0.1 identifiers (per draft-semantic-layer)
    schema.py      # RFC-0002 envelope validation
  tests/
    test_schema.py
```

### Behavior

- `validate(unit) -> list[str]` returns an empty list for a valid unit, otherwise
  plain-language error strings — explainable by construction, no opaque booleans.
- Enforces every RFC-0002 rule: required envelope fields; semver `schema_version` with
  unknown-major rejection; UUID `id`; non-empty `entity_ref`; semantic identifier
  naming rules and namespaces; `engine` id+version; the four mandatory `transformation`
  fields including `source_tradition` and a sha256 `parameters_hash`; `confidence` in
  [0, 1]; non-empty `provenance`; ISO-8601 `created_at`; **`consent_scope` mandatory
  for `PERSON_*` units** (privacy rank 1).
- Registry strict mode (identifier must be registered) ships **off** by default and
  turns on when RFC-0003 (semantic layer) is accepted; naming-rule conformance is
  always enforced.

### Out of scope (deferred to their own RFCs)

Storage, engines, convergence, ingestion, Tier 0 session handling. This RFC is the
envelope only.

## Validation Criteria

- Full pytest suite green on Python 3.11 (Windows and Linux).
- A canonical valid example unit validates; every single-field corruption of it fails
  with a specific, human-readable error.
- `PERSON_*` unit without `consent_scope` is rejected; non-personal unit without it
  passes.
- Unknown schema major version is rejected (RFC-0002 versioning rule).

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Validator drift from RFC-0002 text → the test suite is written
   field-by-field against the RFC; any spec change is a Class 2 RFC that must update
   both together.
2. **Wrong assumptions?** That Python suffices long-term — it does not need to; test
   vectors are the portable contract for future ports.
3. **Biases?** None identified; the validator adds no semantics beyond the spec.
4. **Reversibility?** Full — versioned package, pre-merge branch, no data produced.
5. **Explainability?** Errors are plain sentences naming the exact violated rule.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-09 | Draft; implementation started on feature branch per CONTRIBUTING flow | — |
