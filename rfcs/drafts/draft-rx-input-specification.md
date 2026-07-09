# DRAFT — RX Input Specification: The 10-Question Intake

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review |
| **Class** | 2 (Substantive) |
| **Authors** | **Vision Keeper (Osvaldo)** — requirements and 10-question cap; Implementation Workforce (Claude — AI, analysis and drafting) |
| **Requires** | RFC-0000, RFC-0002, draft-privacy-architecture |
| **Created** | 2026-07-08 |
| **Seeds** | RFC-0003 (Universal Semantic Layer) — first identifier registry |

## Summary

Defines what a person provides to start an RX analysis. **Founding UX rule, set by the
Vision Keeper: an RX never asks more than 10 questions — beyond that is tedium — and
filling only the minimum already produces a valid analysis.** The minimum band is 5
required questions; the full RX is 10. Identifying inputs are ephemeral (Tier 0); what
persists is behavior, positioning and context.

## Motivation

Intake design is a performance decision:

- **Too few inputs** → engines starve; convergence rests on weak signal.
- **Too many inputs** → abandonment rises steeply with form length; tired users give
  noisy answers; weak signals dilute convergence; each extra field raises
  re-identification risk.
- **Structured beats free text** for the mission: mass-behavior learning requires
  answers comparable across the population. Free text is accepted in exactly one
  question, because FE-003 (Linguistic Analysis) is its dedicated consumer.

## Specification

### Band 1 — Minimum (questions 1–5, required)

Enough for a valid, lower-confidence RX:

| Q | Input | Semantic ID | Consumed by | Privacy treatment |
|---|---|---|---|---|
| 1 | Full birth name | `PERSON_NAME` | FE-001 | **Tier 0** — computed, then destroyed; nothing stored |
| 2 | Birth date | `PERSON_BIRTH_DATE` | FE-002, FE-005 | **Tier 0** — persisted only as age band |
| 3 | Birth location (city, country) | `PERSON_BIRTH_LOCATION` | FE-005 | **Tier 0** — persisted only as country/macro-region |
| 4 | Current location (city, country) | `PERSON_LOCATION_CURRENT` | FE-005 | Persisted as region (bucketed) |
| 5 | Focus domain **and direction sought** (grouped single choice) | `PERSON_FOCUS_DOMAIN` | Solver routing, FE-005 | Categorical, persisted |

An RX always answers a question — it never scans a life. Q5 captures both the domain
and what the person seeks within it, in one question.

### Band 2 — Full RX (questions 6–10, optional)

| Q | Input | Semantic ID | Consumed by | Privacy treatment |
|---|---|---|---|---|
| 6 | Field of activity (categorical) | `PERSON_OCCUPATION_FIELD` | FE-005, FE-006 | Categorical, persisted |
| 7 | Decision style under pressure | `PERSON_BEHAVIOR_DECISION` | FE-006 | Categorical, persisted |
| 8 | Risk posture | `PERSON_BEHAVIOR_RISK` | FE-006 | Categorical, persisted |
| 9 | Planning horizon | `PERSON_BEHAVIOR_HORIZON` | FE-006 | Categorical, persisted |
| 10 | Language sample — one open question, 100–300 words | `PERSON_LANGUAGE_SAMPLE` | FE-003 | Processed to linguistic metadata; **raw text destroyed (Tier 0)** |

**Hard cap: 10 questions per RX (Vision Keeper decision, 2026-07-08).** Any future
request to add or swap questions must prove via FE-008 benchmark that the added signal
outweighs abandonment, noise and re-identification cost — and passes Class 2 consensus.

### Not questions — mechanisms (outside the count)

- **Consent** (`consent_scope`): presented at intake as terms, not as a question.
- **Continuity token:** a returning person may present their token to reconnect
  history. Presenting a code is not answering a question. This is also how the protocol
  learns **trajectory**: instead of asking about the past (a question this cap
  eliminated), it observes real trajectory across returning RXs — observed evidence
  (E1) instead of self-report (E0), which is stronger data at zero question cost.

### Engine coverage under the cap — stated honestly

- FE-003 produces intake metadata **only when Q10 is answered**; otherwise it
  contributes nothing to that RX and confidence reflects it.
- FE-004's individual-level input comes from continuity-token returns, not from intake;
  its population-level input comes from the historical brain (draft-outcome-registry).
- The behavioral core was compressed from 7 planned questions to 3 (Q7–Q9: decision,
  risk, horizon — the highest expected signal for directional estimation). The four cut
  dimensions (habit consistency, social positioning, response to failure, energy
  allocation) keep reserved semantic IDs and may only enter by benchmark-proven swap,
  never by raising the cap.

### Prohibited inputs — by design, at any band

Government IDs, exact address, phone/e-mail (account mechanics live outside the
protocol), exact income, health data, religion, ethnicity, sexual orientation,
political affiliation, biometrics. The protocol wants behavior and positioning — never
who the person is.

### Intake rules

1. Band 1 alone must produce a valid RX. Confidence scoring reflects input coverage
   honestly: fewer answers → wider uncertainty, stated to the user.
2. Every persisted answer is a canonical metadata unit (RFC-0002) with
   `consent_scope` set at intake.
3. Question wording and option lists are versioned; changing them is Class 2
   (population comparability breaks silently otherwise).

## Appendix — Questionnaire v0.1 (canonical wording, EN)

Locale translations (first: PT-BR) must preserve meaning exactly; translations are
Class 1 once the canonical text is approved.

**Q1.** What is your full name as given at birth? *(text — never stored)*

**Q2.** What is your date of birth? *(date — never stored; only your age band is kept)*

**Q3.** Where were you born? *(city, country — never stored; only macro-region is kept)*

**Q4.** Where do you live now? *(city, country — kept only as region)*

**Q5.** Where do you want direction right now? *(choose one)*
- Career — grow on my current path
- Career — change direction
- Start or grow something of my own
- Finances — organize / recover
- Finances — build and multiply
- Education — what to study next
- Relationships — personal
- Relationships — professional
- Relocation — whether and where to move
- Personal direction — general

**Q6.** What is your field of activity? *(choose one)*
Technology · Health · Education · Commerce/Retail · Industry · Services · Finance ·
Creative/Media · Public sector · Agriculture · Logistics/Transport · Currently none ·
Other

**Q7.** When you must decide under pressure, what do you actually do most often?
- Decide fast, by instinct
- Look for more information, even if it delays the decision
- Consult people I trust before moving
- Postpone until deciding becomes unavoidable

**Q8.** Which sentence best describes your relationship with risk?
- Risk attracts me — I move with only partial safety
- I take calculated risks, but only after planning
- I prefer stability; I take risk only when cornered
- I avoid risk whenever possible

**Q9.** How far ahead do you genuinely plan?
- I live day to day
- Weeks to a few months
- I keep 1–3 year plans
- I hold a 5+ year vision that guides today's choices

**Q10.** *(optional)* In your own words: describe your current moment and what you want
to change. *(100–300 words — processed and destroyed; only linguistic metadata is kept)*

## Validation Criteria

- Coverage test: with Band 1 only, every applicable engine emits ≥1 unit and a Solver
  produces an estimation with honest (wide) confidence.
- Performance curve: completion rate and estimation calibration measured per band;
  question swaps require benchmark evidence.
- Privacy: intake passes the Tier 0 audit and re-identification tests of the Privacy
  Architecture for every band.
- Comparability: option lists map to stable semantic IDs across wording versions and
  locales.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Q7–Q9 could be poorly worded and measure nothing → wording is
   versioned, benchmarked against outcomes, replaceable by Class 2 swap.
2. **Wrong assumptions?** That 3 behavioral questions carry enough signal — the
   reserved IDs allow benchmark-proven swaps within the cap if not.
3. **Biases?** Category lists (Q5, Q6) may encode cultural bias → lists are versioned
   and extendable per locale without changing semantic IDs.
4. **Reversibility?** Bands and questions are versioned; old RX records state which
   intake version produced them.
5. **Explainability?** Each question maps to named engines and named metadata — the
   user can be shown exactly what each answer feeds.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-08 | Draft | — |
| 2026-07-08 | Hard cap set at 10 questions; minimum must suffice | **Vision Keeper** |
