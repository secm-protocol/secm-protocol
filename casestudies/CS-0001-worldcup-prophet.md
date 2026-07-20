# CS-0001 — The World Cup Prophet: A Pre-Registered Case Study

| Field | Value |
|---|---|
| **Case study** | 0001 — survivorship-manufactured precognition |
| **Status** | **Pre-registered 2026-07-18, BEFORE resolution** (final: 2026-07-19 ~16h BRT) |
| **Authors** | Vision Keeper (Osvaldo) — subject selection; Implementation Workforce (Claude — AI, forensics and drafting) |
| **Method** | RFC-0009 evidence tiers + RFC-0018 pre-commitment, applied manually pending implementation |

## Why this exists

A viral X post (account `@actuallyimthe`, "dilema") created **2021-07-11 23:28:28 UTC**
(timestamp cryptographically embedded in Snowflake id `1414366007888650241` —
unforgeable) states that Argentina beats Spain 3–2 in the 2026 World Cup final. The
finalists were confirmed on 2026-07-15; the final is **tomorrow**. The crowd treats
this single surviving anecdote (evidence tier **E0**) as proof of precognition (**E3**).

SECM registers its analysis **today, before the match**, with explicit falsifiable
statements — doing exactly what the "prophet" ecosystem never does. Whatever happens
tomorrow, this document cannot be quietly edited: its hash and git timestamp exist now.

## Established forensic facts (verifiable by anyone)

1. Tweet creation 2021-07-11 23:28 UTC — the night of the Euro 2020 final, one day
   after Argentina won the Copa América: peak global volume of celebratory
   future-glory posts about Argentina.
2. Wayback Machine holds **zero snapshots of the account 2017–2025**; the tweet was
   first archived 2025-12-08. External record can neither confirm nor refute deleted
   sibling predictions. X permits trace-free deletion; the account has ~7,300 posts.
3. Press coverage (TMC and others) performed no forensic verification.
4. Precedent: every recent World Cup has produced an equivalent retro-discovered
   "prophet" (2022: the 2015 Polanco tweet — Newsweek, CBS Sports). This is a
   recurring population phenomenon, not a unique event.

## Probability decomposition (as of 2021, honestly estimated)

- P(final is exactly Argentina × Spain), July-2021 information: **~1/40 – 1/70**
  (both were visibly top-tier: Argentina had just won the Copa América; Spain was a
  Euro semifinalist with an emerging golden generation).
- P(Argentina wins | that final): **~0.5**.
- P(exact score 3–2 in a final): **~2–4%** (occurred once in WC final history, 1954).
- Full parlay: **~1/3,000 – 1/10,000**.
- Population of prediction-posts per cycle: plausibly **tens of thousands**. Expected
  full-parlay hits somewhere on the platform: **≥1**. Expected finalists-only hits:
  **hundreds**. The crowd's post-hoc search selects the winner; the losers are never
  searched for. P(you win) ≈ 0; P(someone wins) ≈ 1.

## Pre-registered statements (resolution: 2026-07-19)

- **PR-1.** Our estimate, registered before the match: P(Argentina wins in regulation
  by exactly 3–2) ≈ **1.5–2.5%**. If it happens, it is *consistent with
  population-scale survivorship* (≥1 expected full-parlay hit platform-wide) and is
  **not** evidence of precognition. If it does not happen, the same conclusion holds.
  The case study's conclusion is therefore **invariant to the result** — that is the
  point: the anecdote carries no evidential weight either way (E0).
- **PR-2 (behavioral, falsifiable).** If the score is not exactly 3–2, the account
  and its amplifiers will reframe the finalists-only hit as full vindication
  (goalpost displacement). Check the account within 72h of the final.
- **PR-3 (mechanism, falsifiable).** No verifiable evidence of *pre-commitment
  completeness* (a provably complete, undeletable set of the account's 2021
  predictions) will surface. Without completeness, no calibration is computable and
  the tier remains E0 permanently.

## The lesson this case anchors

A prediction is evidence **only** when the complete prediction set was committed
before the outcome and cannot be pruned. Platforms with free deletion structurally
cannot produce E2+ forecasting evidence, regardless of timestamps. SECM's outcome
registry (RFC-0009/0018) and hash-anchored preservation exist precisely to provide
what X cannot: completeness, not just timestamps.

## Resolution log

| Date | Event | Outcome |
|---|---|---|
| 2026-07-18 | Pre-registration committed | this document |
| 2026-07-19 | **Final played: Spain 1–0 Argentina (extra time)** | **Prophecy FAILED** |

### Resolution detail

The claim was "Argentina beats Spain 3–2." Actual result: **Spain won 1–0 in extra
time**. The prediction was correct on the pair of finalists and wrong on both the
winner and the score — i.e. wrong on every component that carried the improbability.

### Scoring of pre-registered statements

| ID | Our registered estimate | Outcome | Result |
|---|---|---|---|
| **PR-1** | P(Argentina wins exactly 3–2) ≈ **0.02** | Did not occur | **Brier = (0.02 − 0)² = 0.0004** |
| **PR-2** | Goalpost displacement to "called the finalists" framing if score missed | Resolution window open (72h from 2026-07-19) | Pending observation |
| **PR-3** | No verifiable pre-commitment completeness will surface | No such evidence exists as of resolution | Standing |

### Honest reading of our own score — the same standard applied to ourselves

A Brier of 0.0004 on PR-1 is **not** evidence that this method predicts football. It is
one statement, n=1. Claiming skill from a single low-probability call is precisely the
survivorship error this case study documents, and the protocol refuses to commit it in
its own favour. What the exercise *does* establish is procedural, and that is the point:

1. **The conclusion was registered as invariant to the outcome** before the outcome
   existed. The anecdote was E0 whether the score hit or missed; it missed, and the
   classification did not need to move.
2. **The asymmetry is now documented.** ~95k reposts and ~282k likes accrued to the
   claim *before* resolution, on the strength of the finalists-only match. The
   improbable component — the part that would have demanded explanation — failed.
   Virality preceded, and was independent of, correctness.
3. **The mechanism held.** Population-scale prediction volume guarantees partial hits;
   partial hits are amplified retroactively; the complete prediction set remains
   unauditable on a platform permitting silent deletion. Nothing about the resolution
   changes the tier: **E0**, permanently, for want of completeness.

The value of this case study was never in guessing a scoreline. It was in demonstrating
that a claim can be timestamped, viral, and celebrated as precognition while being
unfalsifiable *as evidence* — and that pre-registration is what separates a measurable
forecast from a story told after the fact.
