# DRAFT — RX Input Specification: Minimum and Maximum Intake

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review |
| **Class** | 2 (Substantive) |
| **Authors** | **Vision Keeper (Osvaldo)** — requirement; Implementation Workforce (Claude — AI, analysis and drafting) |
| **Requires** | RFC-0000, draft-metadata-schema, draft-privacy-architecture |
| **Created** | 2026-07-08 |
| **Seeds** | RFC-0003 (Universal Semantic Layer) — first identifier registry |

## Summary

Defines what a person provides to start an RX analysis: a **minimum band of 5 inputs**
(enough to run a first estimation), an **optimal band of ~15 data points** (peak
analysis performance), and a **hard cap of 20** (beyond which performance degrades).
Every input maps to a semantic identifier, the engines that consume it, and its privacy
treatment. Inputs that identify the person are ephemeral (Tier 0); what persists is
behavior, positioning and context.

## Motivation

Intake design is a performance decision, not a form design detail:

- **Too few inputs** → engines starve; convergence rests on weak signal.
- **Too many inputs** → abandonment rises steeply with form length; tired users give
  noisy answers; weak signals dilute convergence; and each extra field raises
  re-identification risk.
- **Structured beats free text** for the mission: mass-behavior learning requires
  answers that are comparable across the population. Free text is accepted in exactly
  one place, because FE-003 (Linguistic Analysis) is its dedicated consumer.

## Specification

### Band 1 — Minimum (5 inputs, required)

The smallest set that lets every identity-independent engine produce at least one
metadata unit and routes the analysis to a Solver:

| # | Input | Semantic ID | Consumed by | Privacy treatment |
|---|---|---|---|---|
| 1 | Full birth name | `PERSON_NAME` | FE-001 | **Tier 0** — computed, then destroyed; nothing stored |
| 2 | Birth date | `PERSON_BIRTH_DATE` | FE-002, FE-005 | **Tier 0** — persisted only as age band |
| 3 | Birth location (city, country) | `PERSON_BIRTH_LOCATION` | FE-005 | **Tier 0** — persisted only as country/macro-region |
| 4 | Current location (city) | `PERSON_LOCATION_CURRENT` | FE-005 | Persisted as region (bucketed) |
| 5 | Focus domain — the area where the person seeks direction (career, business, education, finances, relationships, relocation, personal development) | `PERSON_FOCUS_DOMAIN` | Solver routing, FE-005 | Categorical, persisted |

Without a focus domain there is no direction to estimate — an RX always answers a
question, it never scans a life.

### Band 2 — Optimal (+10 → ~15 data points, recommended)

Where analysis performance peaks. These are the inputs expected to carry the strongest
validated signal (behavior and positioning), consistent with weights being earned
through evidence (RFC-0001 §6):

| # | Input | Semantic ID | Consumed by | Privacy treatment |
|---|---|---|---|---|
| 6 | Occupation / field of activity (categorical) | `PERSON_OCCUPATION_FIELD` | FE-005, FE-006 | Categorical, persisted |
| 7 | Education level (categorical) | `PERSON_EDUCATION_LEVEL` | FE-005 | Categorical, persisted |
| 8–14 | **Behavioral core** — 7 structured single-choice questions: decision style under pressure; risk posture; habit consistency; social positioning; response to failure; planning horizon; energy allocation | `PERSON_BEHAVIOR_{DECISION, RISK, HABIT, SOCIAL, FAILURE, HORIZON, ENERGY}` | FE-006 | Categorical, persisted |
| 15 | Declared goal within the focus domain (structured choice) | `PERSON_GOAL` | FE-005, Solver | Categorical, persisted |

The behavioral core is the heart of the RX: it is deliberately structured (not free
text) so that individual answers aggregate into population-level patterns — the mass
dynamics the protocol exists to learn.

### Band 3 — Maximum (+5 → hard cap 20, optional)

| # | Input | Semantic ID | Consumed by | Privacy treatment |
|---|---|---|---|---|
| 16 | Trajectory: major transitions in the last 5 years (structured: type + count — moves, job changes, ventures started/ended, ruptures) | `PERSON_TRAJECTORY_5Y` | FE-004, FE-006 | Categorical, persisted |
| 17 | Current constraints (multi-select bands: financial, family, time, mobility) | `PERSON_CONSTRAINTS` | FE-005 | Banded, persisted |
| 18 | **Language sample** — one open question ("describe your current moment in your own words", 100–300 words) | `PERSON_LANGUAGE_SAMPLE` | FE-003 | Processed to linguistic metadata; **raw text destroyed (Tier 0)** — free text can contain identifying details |
| 19 | Continuity token from a previous RX (reconnects history) | `CONTINUITY_TOKEN` | FE-008 loop, FE-004 | Random token only |
| 20 | Reserved — fixed at implementation RFC | — | — | — |

**Hard cap: 20 data points per RX.** Requests for more inputs in future versions must
prove, via FE-008 benchmark, that the added signal outweighs added abandonment, noise
and re-identification risk (RFC-0001 §6: measurable or it doesn't ship).

### Prohibited inputs — by design, at any band

Government IDs, exact address, phone/e-mail (account mechanics live outside the
protocol), exact income (bands only, if ever), health data, religion, ethnicity, sexual
orientation, political affiliation, biometrics. These are excluded regardless of
analytical temptation: sensitive categories violate precedence rank 1 and add
re-identification risk the mission does not need. The protocol wants behavior and
positioning — never who the person is.

### Intake rules

1. Band 1 alone must produce a valid (lower-confidence) RX. Confidence scoring reflects
   input coverage honestly: fewer inputs → wider uncertainty, stated to the user.
2. Every persisted answer is a canonical metadata unit (draft-metadata-schema) with
   `consent_scope` set at intake.
3. Band composition and question wording are versioned; changing them is Class 2
   (population comparability breaks silently otherwise).

## Validation Criteria

- Coverage test: with Band 1 only, every identity-independent engine emits ≥1 unit and
  a Solver produces an estimation with honest (wide) confidence.
- Performance curve: A/B measurement of completion rate and estimation calibration per
  band size; the optimal band is retuned from evidence, not intuition.
- Privacy: intake passes the Tier 0 audit and re-identification tests of the Privacy
  Architecture for every band.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** The behavioral core questions could be poorly worded and
   measure nothing → mitigated: wording is versioned, benchmarked against outcomes, and
   replaceable by Class 2 RFC.
2. **Wrong assumptions?** That 20 is the right cap — it is a starting hypothesis; the
   performance curve test exists to move it with evidence.
3. **Biases?** Category lists (occupation, goals) may encode cultural bias → lists are
   versioned, reviewed, and extendable per locale without changing semantic IDs.
4. **Reversibility?** Bands and questions are versioned artifacts; old RX records state
   which intake version produced them.
5. **Explainability?** Each input maps to named engines and named metadata — the user
   can be shown exactly what each answer feeds.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-08 | Draft | — |
