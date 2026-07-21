# RANKING-01 — Structured Ranking by Probability of Thesis Durability

Produced 2026-07-19 from SCREEN-01→04. **Research judgment, not a recommendation, not
a price forecast, no asset endorsed.** Ranked on *probability the underlying economics
persist*, which is a different question from *probability the token appreciates*.

## Why the distinction is the whole job

A token's return decomposes into (a) durability of the cash flow, (b) share of it
reaching holders, (c) dilution, and (d) **change in what the market will pay for it** —
the multiple. Screens measure (a)–(c) with public data. Item (d) is sentiment and is
not forecastable from these inputs. Ranking (a)–(c) is defensible analysis; claiming
to rank (d) would be the survivorship error documented in CS-0001.

## Scoring dimensions

| Dimension | Question |
|---|---|
| **Durability** | Is revenue tied to the real economy or to speculative cycles? |
| **Capture quality** | Structural (burn/mint, protocol-level) or a reversible policy? |
| **Dilution** | FDV/mcap overhang |
| **Valuation** | FDV-adjusted price to holders revenue |
| **Position** | Competitive standing and switching costs |

## Ranking

### 1. Canton (CC) — strongest structural case
Durability **high**: fees arise from institutional settlement activity (DTCC, JPMorgan,
Franklin Templeton, Visa, Broadridge as infrastructure participants), a demand source
uncorrelated with crypto speculation and carrying very high switching costs once
adopted. Capture **structural** (burn-and-mint, not a reversible governance policy).
Dilution **none** (1.00; no pre-mine, no VC allocation). Valuation **7.3x** — the
cheapest capture-adjusted figure in the entire study, on $674M/yr of holders revenue,
an order of magnitude larger than any other name with real capture.
**Key risk:** depth of adoption is unverified from public data — "participant" may mean
production throughput or exploratory membership; a NASDAQ treasury vehicle (CNTN)
introduces reflexivity in both directions; −16% over 30d.
**What would change the view:** evidence that fee volume is subsidised/incentivised
rather than organic production usage.

### 2. Pendle (PENDLE) — best positioned in the sector with momentum
Durability **medium-high**: yield tokenisation is a genuine primitive, and the adjacent
sector (restaking, +11.7% 7d) is the strongest-flowing category measured. Capture
**79%**, $8M/yr. Dilution 1.64.
**Key risk:** demand is derivative of yield-bearing asset supply; a collapse in staking
yields compresses the entire business. Valuation ~58x FDV-adjusted is not cheap.
**What would change the view:** sustained contraction in restaking TVL.

### 3. Convex (CVX) — highest mechanism certainty, capped ceiling
Durability **medium**: mechanism has operated for years; capture **98%** is among the
best measured; dilution minimal (1.09); valuation 15.6x.
**Key risk:** structurally a derivative of Curve. Its ceiling is Curve's relevance,
which has been eroding against newer AMM designs. High confidence it keeps working;
low probability of large growth.
**What would change the view:** Curve share stabilising or reversing.

### 4. Geodnet (GEOD) — cheapest real-capture name, highest execution risk
Durability **medium**: revenue ($9M/yr) comes from real-world customers (precision
GPS/RTK for surveying, agriculture, autonomous systems) — non-speculative demand, which
is a genuine quality marker. Capture 80%; valuation ~9.7x on mcap.
**Key risk:** dilution 2.12 (≈112% more supply pending) is the largest overhang in this
tier; $87M cap means real liquidity constraints; DePIN unit economics remain unproven
at scale.
**What would change the view:** the unlock schedule — timing and size must be checked
before this ranking means anything.

### 5. GMX — cheap, fully diluted, declining share
Durability **medium-low**: survived multiple cycles, fully diluted (1.00), real revenue,
valuation 11.8x.
**Key risk:** losing perpetuals share to newer venues; capture only 27%. The thesis is
"decline is already in the price," which is a weaker thesis than growth.

## Excluded, with reasons

| Asset | Reason |
|---|---|
| Pump.fun | Largest holders revenue at low multiple ($164M, 10.2x) but **revenue is entirely memecoin-cycle dependent** — high cash flow, low durability. Cheap for a reason. |
| ONDO, Aethir, Virtuals, Akash, The Graph | **0% capture** — the token is not a claim on the business, regardless of business quality. Aethir's $36M/yr with zero capture is the sharpest example. |
| KAITO | No measurable revenue, FDV 4.14×, +106% in 30d — the exact inverse of this framework. |
| Injective, Filecoin | Clean structures (100% capture) but 166x and 202x on current holders revenue — priced for growth that must still materialise. |

## The professional truth about "analysts who are always right"

They do not exist. Documented forecasting research places skilled discretionary hit
rates in the ~55–60% range; the durable edge comes from **position sizing and payoff
asymmetry**, not accuracy — being wrong small and right big. Any operator presenting an
unbroken record is presenting a curated subset (CS-0001, PROPHET-AUDIT). This ranking
is accordingly a **prioritisation of research effort**, not a set of conclusions, and
its own accuracy is unknown until scored — which is what RFC-0018 pre-registration
exists to do.
