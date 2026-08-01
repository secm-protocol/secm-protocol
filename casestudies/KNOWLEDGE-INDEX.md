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

### M6. The mechanism gate (time lens)
Apply to every cycle or trend claim, in any domain: **a cycle is real only if its
producing mechanism can be named.**

| Cycle | Mechanism | Status |
|---|---|---|
| Seasons | orbital tilt / solar angle | physical — real |
| Halving | emission rule every 210,000 blocks | protocol — real |
| Elections | constitutional term | legal — real |
| Token unlock | vesting contract | contractual — real |
| "4-year crypto cycle" | none stated | pattern in noise until named |

Corollary: sort every finding into **dated + mechanism** (actionable), **cyclical
without mechanism** (noise), **undated** (context only). Direction without timing is
worthless — being early is operationally indistinguishable from being wrong.

### M7. Layer separation (perception lens)
Apply to every metric: **is this changing the thing, or changing how the thing is
seen?** Both layers are real and both move capital; conflating them is the recurring
error.

| | Substance strong | Substance weak |
|---|---|---|
| **Perception strong** | already priced — nothing to do | **trap zone** (ONDO +20% / 0% capture; KAITO +106% / no revenue) |
| **Perception weak** | **value zone** (Canton: 100% capture, −16% price) | correctly ignored |

The divergence *between* layers is the signal — this is the general form of which
EE-004's D1–D6 are instances. Combined with M6: a value-zone finding still requires a
**dated catalyst with a named mechanism** to become actionable, otherwise it is a
correct thesis with no clock.

**Provenance:** M6 and M7 are decompositions of two "forbidden teachings" catalogued in
1 Enoch's Book of the Watchers (astrology → calendar/timing; cosmetics → appearance
management), per RFC-0000 §3–4: extract the transformation, discard the belief. The
text's own thesis — capability delivered without the discernment to carry it — is why
these lenses ship bound to M5 (keep score) rather than alone.

### M8. Network provenance mapping (the smiling face is rarely the structure)
For any project, asset or institution, the visible figurehead is one node, not the map.
Trace four layers:

1. **Origin capital at the pivotal moment** — who funded the founder *before it was
   obvious*, not who invests now.
2. **The funder's other positions** — what else that capital network touches.
3. **Structural dependencies** — custody, reserves, settlement rails, board interlocks.
4. **What it actually reveals** — alignment and access, which is **not** control.

**Calibration rule (mandatory, or the method self-destructs):** a grant, an early
investment, a board seat and a controlling stake are four different things with four
different implications. Overstating the link destroys credibility; ignoring it misses
real structure. State which one you found.

**Worked example — Ethereum (all verified 2026-07-31):**

| Layer | Finding |
|---|---|
| Visible face | Vitalik Buterin |
| Origin capital | **Thiel Fellowship, $100,000, 2014** — enabled dropping out of Waterloo to build Ethereum full-time |
| Funder's network | Thiel co-founded PayPal (Confinity/X.com merger with Musk, 2000); co-founded **Palantir**, which signed a **strategic partnership with Israel's Ministry of Defense in January 2024**, announced at Palantir's board meeting in Tel Aviv following a meeting between Israeli defence officials and Thiel + Karp; valued in tens of millions |
| Current institutional layer | BlackRock's BUIDL launched on Ethereum first; Coinbase custodies the major ETFs; Circle's reserves managed by BlackRock; DTCC tokenization runs on Besu, an Ethereum client (CS-0003) |
| **Honest reading** | **Not control.** Thiel does not control Ethereum, and a 2014 fellowship grant conveys no governance rights. What it documents is that the same capital network behind payments infrastructure and defence-intelligence infrastructure identified and enabled the founder of the leading smart-contract network at its pivotal moment — and that a decade later, the largest asset manager on earth built its tokenization stack on that same network. **Alignment and access, traced through public record.** |

**Why this matters operationally:** provenance predicts *which direction an institution
bends under pressure* better than its stated mission does. It is also fully traceable
from public sources — fellowship announcements, corporate filings, custody agreements,
press releases — which is exactly why it is under-used.

**Brazilian equivalent tooling (regional application):** CNPJ/QSA (Receita Federal),
state Junta Comercial filings, Portal da Transparência, TCE decisions, Diário Oficial,
CEIS/CNEP, TSE donation records. Detection patterns: shared addresses across
unrelated CNPJs; the same accountant or lawyer across entities; administrators
appearing across many unrelated companies (professional nominee marker); companies
winning contracts shortly after incorporation; ownership changes clustered right after
an administration change.

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
