# SCREEN-03 — Institutional Sector Rotation and the Investability Gap

Run 2026-07-19, live public data (DeFiLlama protocols/categories/fees/holdersRevenue +
CoinGecko). **Research screen. Not a recommendation. No asset endorsed.**

## Sector rotation (TVL-weighted, 7d — the only momentum window the API exposes)

| Sector | TVL | 7d | Protocols |
|---|---|---|---|
| Restaking | $9.2B | **+11.7%** | 9 |
| RWA Lending | $0.7B | +7.8% | 9 |
| Restaked BTC | $0.9B | +6.0% | 3 |
| Payments | $0.3B | +5.5% | 4 |
| Risk Curators | $7.9B | +5.1% | 34 |
| Lending | $40.8B | +4.4% | 138 |
| Staking Pool | $10.5B | +4.0% | 15 |
| **RWA** | **$25.5B** | −0.5% | 82 |
| Prediction Market | $0.4B | **−15.1%** | 10 |

## The investability gap — the finding that reframes the thesis

The institutional/RWA sector is genuinely large ($25.5B). But ranking its largest
protocols by TVL reveals that **most institutional capital sits in products that have
no investable token**:

| Protocol | TVL | Token |
|---|---|---|
| BlackRock BUIDL | $3.34B | **none** |
| Circle USYC | $2.96B | **none** |
| Tether Gold | $2.90B | XAUt (gold claim) |
| Ondo Yield Assets | $2.56B | ONDO |
| Paxos Gold | $1.82B | PAXG (gold claim) |
| Centrifuge | $1.63B | CFG |
| Spiko | $1.23B | **none** |
| Blockchain Capital | $0.97B | BCAP |
| WisdomTree | $0.78B | **none** |
| Invesco USTB | $0.67B | **none** |

**Conclusion: "institutions are entering" is true and simultaneously not directly
tradable.** They are buying tokenized treasuries and funds — instruments whose
economics accrue to the issuer, not to a governance token. Narrative exposure and
economic exposure are different things.

## The flagship trap: ONDO

| Metric | Value |
|---|---|
| Market cap | $1,976M |
| FDV / mcap | 2.05 (≈105% more supply pending) |
| Fees generated (ann.) | $82M |
| **Revenue reaching holders (ann.)** | **$0 — 0% capture** |
| 30d price | **+20%** |

ONDO is the most-cited RWA token, is on essentially every institutional-narrative list,
and rose 20% in 30 days while routing **zero** economics to the token. Compare with the
SCREEN-02 traps (Uniswap 5%, Maple 3%, Aave 2%): ONDO is the limiting case. Price is
tracking narrative, not cash flow. That can persist — narrative is a real market force —
but it must not be mistaken for value accrual.

## Where sector flow, real capture and low dilution actually intersect

| Asset | Capture | FDV/MC | Note |
|---|---|---|---|
| Canton (CC) | **100%** | **1.00** | Institutional L1; burn-and-mint; DTCC/JPMorgan/Franklin Templeton/Visa as infra participants; no pre-mine, no VC allocation |
| Pendle (PENDLE) | 79% | 1.64 | Yield infrastructure; $8M holders revenue on $10M fees |

That is the entire intersection at this screen's thresholds. It is a very short list —
which is itself the finding.

## Data limitations (must not be read as findings)

Name-based joins failed for Chainlink, Ethena, Lido, Ether.fi and EigenCloud — these
returned `n/a`, which means **the join did not match**, NOT that they lack revenue.
Several of them demonstrably generate fees. Centrifuge resolved to a deprecated
CoinGecko entry ($0 mcap) and must be re-checked manually. Any conclusion about these
names requires a manual pass.

## The structural tension worth stating plainly

This screen selects for cash flow, capture and low dilution. Historically, the largest
percentage moves in crypto come from narrative and reflexivity — precisely the
characteristics this screen filters out. "Structurally sound" and "maximum upside" are
not the same selection criterion, and no dataset can convert one into the other.
