# KNOWLEDGE INDEX — Accumulated Research Memory

The historical brain (RFC-0009) applied to this protocol's own research. Load this file
first when resuming analysis: it holds the **reusable methods and validated heuristics**,
not just conclusions. Conclusions expire; methods compound.

Last updated: 2026-07-25.

---

## PART 1 — Reusable methods (the durable asset)

### M1. Prophet verification — 6 steps
Full protocol: `PROPHET-AUDIT.md`. Demand the falsifiable object -> decode the ID
timestamp (X: `(id>>22)+1288834974657` ms; TikTok: `id>>32` s) -> establish the base rate
at the moment of the claim -> demand prediction-set completeness -> test resolution
elasticity -> follow the monetization funnel.

**Core law:** on any platform allowing silent deletion, completeness is unobtainable, so
no viral forecaster can exceed evidence tier **E0** — by structure, not by fraud.

### M2. Crypto valuation — three layers, never one
Full protocol: `SCREEN-01`, `SCREEN-02`. Fees generated != protocol revenue != revenue
reaching token holders. Then correct for dilution (FDV/mcap).

```
Honest multiple = (mcap / holders_revenue_annualized) x (FDV / mcap)
```

Data: DeFiLlama `overview/fees` with `dataType=dailyHoldersRevenue`; CoinGecko markets.
**Measured error of the naive screen: up to 53x** (Aave 4.1x -> 216x).

### M3. Cross-layer divergence
Full protocol: `draft-ee004-intent-signals.md`. Signal lives in disagreement *between*
independent layers, not inside one. Founding rules D1-D6 (institutional inflow vs
stablecoin contraction; sentiment vs dry powder; TVL in USD vs in tokens; unlock +
euphoria + positive funding; 13F accumulation + flow turn + negative funding; stated
intent vs market pricing).

### M4. Intent signals, not prophecy
Elite publications and institutional filings are **disclosures of intent by actors with
execution power** — not foresight. Read the FOMC dot plot, 13F filings, VC theses,
unlock calendars, governance proposals and regulatory agendas as intent. Every actor
requires a follow-through record before their intent carries weight.

### M5. Pre-registration
Any probabilistic claim: explicit statement, resolution date, falsification criterion,
hash-committed *before* resolution. Scored by Brier afterwards. Absence of this is the
single reliable marker separating method from marketing.

---

## PART 2 — Validated heuristics

| # | Heuristic | Established in |
|---|---|---|
| H1 | Interrogative headlines ("Is a crisis brewing?") cannot resolve false — unfalsifiable by construction | CS-0004 |
| H2 | Symbols present in every year (tanks, missiles, satellites, dollar signs) carry zero predictive information | CS-0004 |
| H3 | Virality precedes and is independent of correctness — fame is harvested before resolution | CS-0001 |
| H4 | Serial bottom/top calls guarantee a hit that memory keeps, plus misses that memory drops | Doctor Profit analysis |
| H5 | Real revenue with 0% capture = the token is not a claim on the business | SCREEN-02, SCREEN-04 |
| H6 | Strong capture undone by high FDV/mcap = second-order trap | SCREEN-02 (HYPE 71% capture, 4.29 FDV) |
| H7 | Capture > 100% is subsidy, not profit — red flag, not bargain | SCREEN-02 (deBridge 152%) |
| H8 | Institutional money frequently sits in products with no investable token | SCREEN-03 (BUIDL, USYC, Spiko) |
| H9 | In observed samples, 30-day price momentum correlates *inversely* with cash-flow backing | SCREEN-04 (KAITO +106%, no revenue) |
| H10 | Capture activation is a discrete, publicly observable event (governance forum -> vote -> execution) — watch the forum, not the chart | SCREEN-04 |
| H11 | The binding constraint on AI infrastructure is grid interconnection, not chips | SCREEN-05 |
| H12 | Skilled discretionary forecasting runs ~55-60% hit rate; superforecasters beat classified-access analysts by ~30%, not 300%. Edge comes from sizing and asymmetry, not accuracy | CS-0004, RANKING-01 |

---

## PART 3 — Case files

| File | Subject | Status |
|---|---|---|
| `CS-0001` | World Cup prophet | **RESOLVED — prophecy failed** (Spain 1-0 Argentina, ET). PR-1 Brier 0.0004; PR-2/PR-3 standing |
| `CS-0002` | BTC probabilistic statements S1-S5 | **OPEN** — see Part 4 |
| `CS-0004` | Economist forecasting scorecard | Complete — no public accuracy ledger exists across 40 editions |
| `PROPHET-AUDIT` | Reusable verification protocol | Active method |
| `SCREEN-01` .. `SCREEN-05` | Valuation, sectors, AI infra, energy stack | Reproducible screens |
| `RANKING-01` | Durability ranking | Canton -> Pendle -> Convex -> Geodnet -> GMX |
| CS-0003 | Doctor Profit prospective ledger | **NOT STARTED** — requires Vision Keeper to supply calls as they publish |

---

## PART 4 — Open positions awaiting resolution (score these when due)

| ID | Statement | Estimate | Resolves |
|---|---|---|---|
| S5 | Fed hikes at July FOMC | 0.46 | **2026-07-29** |
| S1 | BTC below $55k | 0.50 | 2027-01-01 |
| S3 | BTC new ATH | 0.07 | 2027-01-01 |
| S2 | BTC below $40k | 0.25 | 2027-07-01 |
| S4 | BTC new ATH | 0.45 | 2028-07-01 |
| D-AI-1 | Stablecoin supply reaches ~$420B (industry projection) vs measured $306.6B and contracting | contradiction | 2026-12-31 |
| PR-2 | Goalpost displacement by World Cup account | expected | observation window closed |

**Discipline:** every one of these gets scored on its date, including the ones that go
against us. An unscored prediction set is exactly the failure this entire body of work
documents.

---

## PART 5 — Live data sources (verified working)

| Source | Endpoint / access | Provides |
|---|---|---|
| DeFiLlama fees | `api.llama.fi/overview/fees` (+`dataType=dailyHoldersRevenue`) | 3-layer revenue, 2,443 protocols |
| DeFiLlama protocols | `api.llama.fi/protocols` | TVL, category, 7d change (**no mcap, no 30d**) |
| DeFiLlama stablecoins | `stablecoins.llama.fi/stablecoincharts/all` | Aggregate supply — dry powder |
| CoinGecko markets | `api.coingecko.com/api/v3/coins/markets` | mcap, FDV, 30d change |
| Alternative.me | `api.alternative.me/fng` | Fear & Greed |
| BCB SGS | `api.bcb.gov.br/dados/serie/bcdata.sgs.{432,433,1}` | Selic, IPCA, FX — **ingested daily by the protocol's own bot** |
| Good Judgment Open | `gjopen.com` | Calibrated crowd probabilities, dated questions |

**Known pitfalls:** name-based joins across APIs fail silently (Chainlink, Ethena, Lido,
Ether.fi returned false negatives — join failures, not absence of revenue). CoinGecko
serves deprecated entries (Centrifuge $0 mcap). Every candidate requires manual
verification before any conclusion.

---

## PART 6 — Anti-patterns catalogued

1. **Survivorship** — population-scale prediction volume guarantees hits; the crowd
   searches retroactively and finds the winner (CS-0001).
2. **Bidirectional coverage** — "Option A or Option B", then narrate the one that landed.
3. **Serial calls** — call the bottom monthly; one will be right.
4. **Telegraphed intent as prophecy** — repackage a publicly announced plan as vision
   (Venezuela/TikTok case).
5. **Elasticity** — claims that cannot fail cannot inform.
6. **Missing denominator** — publish predictions, never resolutions. Present at every
   prestige tier, from anonymous accounts to 40-year institutional annuals.
