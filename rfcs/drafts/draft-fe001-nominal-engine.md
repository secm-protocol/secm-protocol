# DRAFT — FE-001 Nominal Encoding System v0.1

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review (implementation on `feature/rfc-0021-structural-engines`) |
| **Class** | 2 (Substantive — Foundation Engine specification, per RFC-0021 priority amendment) |
| **Authors** | Implementation Workforce (Claude — AI, labeled per RFC-0001 §7) |
| **Requires** | RFC-0002, RFC-0003, RFC-0007, RFC-0008, RFC-0011, draft-structural-first-priority |
| **Created** | 2026-07-09 |

## Summary

Specifies the first working version of FE-001, named in RFC-0000 §8 since Genesis and
never implemented until now. Decomposes the classical Pythagorean letter-value table
— the exact example RFC-0000 §4 uses to illustrate "extract the transformation, not
the belief" — into a neutral computational transformation over the person's declared
name (RFC-0011 Q1).

## Motivation

The protocol's structural understanding of a person was missing its first layer:
nominal structure. RFC-0000 §4 explicitly sanctions this extraction; this RFC
specifies it honestly, including the confidence honesty the constitution requires.

## Specification

### Input

`PERSON_NAME` (RFC-0011 Q1) — **Tier 0, ephemeral** (RFC-0008): consumed in-memory for
this transformation only, never stored, never logged.

### Transformation: letter-value reduction v0.1

Classical Pythagorean table, A–Z mapped 1–9 repeating (A=1...I=9, J=1...R=9, S=1...Z=8)
— decomposed as pure arithmetic, the historical origin cited plainly, the mystical
interpretation never adopted (RFC-0000 §4).

1. Sum letter-values over **all letters**, **vowels only** (A E I O U), and
   **consonants only**.
2. Reduce each sum by repeated digit-sum to a single digit, halting early at repdigit
   multiples of 11 (11, 22, 33) — a defining property of the classical algorithm being
   decomposed, carrying no claimed significance here.

### Output

One `PERSON_NOMINAL_STRUCTURE` unit (registry addition): `total_reduction`,
`vowel_reduction`, `consonant_reduction`. Neutral field names only — **never** "Life
Path", "Soul Number", "Expression Number," internally or externally (RFC-0000 §4).

### Confidence — honest by construction

Baseline **0.15** (parameter) — deliberately lower than FE-006's self-report baseline
(0.55): this is an **unvalidated historical transformation with zero established
evidence** connecting it to any real-world outcome, weaker even than noisy self-report.
It rises only through FE-008 calibration (RFC-0001 §6), never by assertion.

### Privacy

Output values are **irreversible by construction**: a name collapses to one of ~12
possible single values per field, which cannot recover the original name — a stronger
guarantee than hashing (RFC-0008 explicitly warns that hashing low-entropy personal
data like names is not anonymization).

## Validation Criteria

- Deterministic: same name → identical output.
- Validates under RFC-0007 strict mode.
- No banned terminology anywhere in code, output, or documentation.
- Round-trip privacy test: output values cannot be reversed to the input name.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Read as "numerology with new names" → the confidence baseline,
   the explicit "unvalidated" framing, and FE-008 gating are the structural defenses;
   this is precisely what RFC-0000 §3–4 designed for.
2. **Wrong assumptions?** That letter-value arithmetic carries signal at all — v0.1
   makes no such claim; it only makes the transformation available for FE-008 to test.
3. **Biases?** The table is Latin-alphabet specific; non-Latin names require a future
   Class 2 extension, noted honestly rather than silently mishandled.
4. **Reversibility?** Full — engine version and table are parameters.
5. **Explainability?** Every unit names its exact transformation and historical
   origin; nothing is hidden.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-09 | Draft | — |
