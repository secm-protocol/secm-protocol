# DRAFT — EE-004 Intent Signal Engine & Cross-Reference Matrix

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review; implementation gated on source registrations |
| **Class** | 2 (Substantive — Extension Engine, per RFC-0000 §9) |
| **Authors** | **Vision Keeper (Osvaldo)** — requirement ("narratives are part of the game; money always leaves traces"); Implementation Workforce (Claude — AI, drafting) |
| **Requires** | RFC-0002, RFC-0009, RFC-0014, RFC-0018; pairs with EE-002 (concentration) and EE-003 (fragility) |
| **Created** | 2026-07-19 |

## Summary

Two capabilities the protocol lacks, specified together because they only work
together:

1. **Intent signals** — a data class distinct from news and from sentiment:
   *documents in which actors who have the power to move a system state what they
   intend to do*. Not prophecy, not opinion: disclosed intent from actors with
   execution capacity.
2. **The cross-reference matrix** — the rule set that scores **divergences between
   independent data layers**, because the signal is rarely inside one layer; it is in
   the disagreement between layers that most observers read separately.

## Methodological provenance: why The Economist works and The Simpsons does not

The Vision Keeper asked the protocol to study two famous "prediction" phenomena. They
have **opposite** mechanisms, and separating them is the whole point of RFC-0000 §3.

**The Simpsons — pure survivorship, plus expert extrapolation.** ~750 episodes × dozens
of background gags = tens of thousands of implicit "claims"; a handful hit and are
retroactively canonized (identical mechanism to CS-0001). The residual non-random part:
the writing room held doctorates in mathematics and computer science and practiced
**trend extrapolation of already-visible facts** — the 2000 Trump-presidency gag
followed his real 1999 Reform Party exploratory committee; the Disney/Fox gag followed
visible media-consolidation trajectory. **Extractable transformation:** none beyond
what EE-001/EE-003 already do (trend extrapolation). The prophetic framing is discarded.

**The Economist "The World Ahead" — an elite coordination document.** Conspiratorial
readings treat the cover art as encoded prophecy; there is no evidence for that, and
the covers are commissioned illustrations of editorial content. But the publication is
genuinely forward-informative for a reason that requires no mysticism and that Prof.
Jiang's coordination analysis (EE-002) predicts directly: **it is written for, and
partly by, actors who hold execution power — policymakers, central bankers, capital
allocators.** When coordinated actors with the capacity to shape outcomes publish
what they expect and intend, that publication is (a) a disclosure of intent and
(b) partially self-fulfilling. **Extractable transformation: read it as intent
disclosure, never as prophecy.**

This distinction generalizes into the engine below.

## Specification (v0.1)

### 1. Intent signal class

An intent signal is a **dated, public, primary-source document** from an actor with
demonstrable execution power over the domain, stating a future action or expectation.
Registered per RFC-0014, each carries: actor, execution power basis, stated intent,
stated horizon, and — mandatory — a **follow-through record** so FE-008 can score
whether that actor's stated intent historically materializes. An actor whose intent
never materializes converges to zero weight, exactly like any engine.

Candidate registrations (all public, all free):

| Layer | Source | Intent disclosed |
|---|---|---|
| Monetary | FOMC dot plot / minutes; central-bank statements | Where rate-setters intend rates to go |
| Capital allocation | 13F/13D filings (SEC EDGAR); large-holder disclosures | Where institutional capital is already positioned |
| Venture | Published VC theses and portfolio pages | Which sectors will be funded next |
| Crypto supply | Token unlock calendars (DeFiLlama) | Pre-scheduled, publicly known future sell pressure |
| Protocol | Governance proposals before votes | Protocol changes before execution |
| Regulatory | Published regulatory agendas, consultations | Rule changes before they bind |
| Elite consensus | Annual outlook publications (incl. The World Ahead), IMF/BIS reports, Davos agendas | Expectations of coordinated actors |

**Prohibited:** attributing hidden/occult meaning to imagery or symbolism in any
source; treating engagement volume as intent; naming private individuals as
conspiratorial actors (RFC-0000 §20, EE-002 exclusions).

### 2. Cross-reference matrix

Every registered layer produces an independent reading. The engine's output is the
**divergence map**: pairs of layers that disagree, ranked by historical
informativeness of that disagreement. Founding divergence rules (v0.1, each versioned
and individually Brier-scored — labeled `expert-prior-unvalidated` until scored):

| # | Divergence | Reading |
|---|---|---|
| D1 | Institutional inflow **up** while stablecoin supply **contracts** | New external capital arriving while native dry powder leaves; net liquidity may be negative despite bullish headlines |
| D2 | Sentiment recovering while dry powder still contracting | Narrative bottom precedes capital bottom; sentiment alone is not positioning |
| D3 | TVL rising **less** than the price of its underlying assets | Real deposits shrinking behind a USD-denominated illusion |
| D4 | Large scheduled unlock + retail euphoria + positive funding | Known future supply meeting leveraged demand: maximum fragility |
| D5 | 13F accumulation + flow turning + negative funding | Positioned capital versus punished leverage: the mirror of D4 |
| D6 | Stated intent (rates/regulation) diverging from market-implied pricing | The gap itself is the tradable-information object — and the falsifiable one |

Each divergence emits a metadata unit citing every source value that produced it. No
divergence is ever emitted without all constituent layers present and dated —
**coverage gaps are declared, never interpolated** (RFC-0015 marker discipline).

### 3. Mandatory pre-registration

Any probabilistic statement derived from a divergence follows RFC-0018 and CS-0002:
explicit claim, resolution date, falsification criterion, hash-committed **before**
resolution. Divergence rules that fail to beat naive baselines are demoted publicly.

## Validation Criteria

- Every divergence recomputable by a third party from cited public sources.
- Follow-through scoring exists for every registered intent actor before their signals
  carry any weight.
- No emission without full layer coverage; partial coverage produces an explicit gap
  marker instead.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Divergence rules are hand-authored priors that may encode the
   author's bias → each is individually scored and demotable; none carries weight
   before scoring.
2. **Wrong assumptions?** That stated intent predicts action — precisely what the
   follow-through record measures instead of assuming.
3. **Biases?** Over-reading elite documents as omniscient; the follow-through record
   is the antidote (elites are frequently wrong, and their misses are recorded too).
4. **Reversibility?** Pure analysis over public data; versioned rule tables.
5. **Explainability?** Every divergence names its layers, values, dates and sources.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-19 | Draft | — |
