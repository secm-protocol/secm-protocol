# SCREEN-01 — Crypto Value Screen and the Capture-Rate Correction

Methodology note produced 2026-07-19 from live public data (DeFiLlama fees API +
CoinGecko market caps). Feeds EE-003/EE-004 when implemented. **Research screen, not
a recommendation — no asset here is endorsed.**

## The naive screen everyone runs

Rank protocols by market cap ÷ annualized **fees generated** (P/Fees), crypto's
closest analogue to a P/E ratio. Result from live data (mcap > $80M, fees > $200k/30d,
48 matched pairs):

| Protocol | Ticker | P/Fees | Mcap | Fees (ann.) |
|---|---|---|---|---|
| Maple Finance | SYRUP | 1.8x | $219M | $120M |
| Uniswap | UNI | 2.4x | $2,316M | $978M |
| Pump.fun | PUMP | 2.6x | $786M | $297M |
| Aave | AAVE | 4.1x | $1,454M | $353M |
| Raydium | RAY | 4.2x | $194M | $47M |
| PancakeSwap | CAKE | 6.6x | $456M | $69M |
| Hyperliquid | HYPE | 20.5x | $13,953M | $681M |

Read naively, Uniswap looks like the second cheapest asset in the entire sector and
Hyperliquid looks ~8x more expensive.

## Why the naive screen is wrong — the capture rate

**Fees generated ≠ revenue to the protocol ≠ value accruing to the token.** Three
distinct layers; almost every public "crypto P/E" chart conflates layer 1 with layer 3.

The gap is measurable, and Uniswap is the cleanest demonstration available. Uniswap
activated its fee switch in December 2025 (UNIfication: 100M UNI ≈ $596M burned, fee
routing to a burn/token-jar mechanism across 11 chains through mid-2026). Yet the
**protocol revenue run-rate that reaches the mechanism is ≈ $26–27M/year**, against
≈ $978M in gross fees — because the overwhelming majority of fees are paid to
liquidity providers, not to the protocol.

| Layer | Uniswap (annualized) |
|---|---|
| 1. Gross fees generated | ~$978M |
| 3. Revenue reaching token mechanism | **~$26.5M** |
| **Capture rate** | **≈ 2.7%** |

Corrected valuation: $2,316M ÷ $26.5M ≈ **87x revenue** — not 2.4x. The naive screen
was off by a factor of ~36.

## The inversion

Applying the correction reorders the entire table. A protocol whose fees route
substantially to the token (buyback/burn designs such as Hyperliquid's assistance-fund
mechanism) has a capture rate near unity, so its P/Fees ≈ its P/Revenue. A protocol
with a 2.7% capture rate must be re-rated ~36x worse.

**Consequence: an asset appearing ~8x more expensive on the naive screen can be several
times cheaper on a capture-adjusted basis.** This reordering is invisible to anyone
reading fee charts alone, and it is derivable entirely from public data.

## Required verification per protocol (never skip)

1. **Capture rate** — what fraction of gross fees provably reaches token holders?
   Read the governance proposal and the on-chain mechanism, not the marketing page.
2. **Circulating vs fully diluted** — this screen uses circulating mcap; scheduled
   unlocks (public calendars) can multiply the real denominator.
3. **Fee durability** — is the fee stream structural or a function of a transient
   mania? A launchpad earning during a memecoin cycle is not an annuity.
4. **Name-match integrity** — 48 of 500 assets matched automatically; joins by name
   can mis-associate. Verify each candidate manually before it means anything.

## Status

Founding screen methodology. Ratios above are a **starting point for research only**;
no ranking here constitutes a conclusion. When EE-003/EE-004 are implemented, this
screen runs on schedule with capture rate as a required field, and every derived
probabilistic claim is pre-registered per RFC-0018.
