# SCREEN-02 — Full Three-Layer Cross-Reference with Dilution Adjustment

Run 2026-07-19 on live public data: DeFiLlama (`fees`, `dailyHoldersRevenue`) +
CoinGecko (market cap, FDV, 30d change). 500 assets screened → 20 with verifiable
holders revenue > $250k/30d and mcap > $50M. **Research screen. Not a recommendation.
No asset here is endorsed.**

## Method

Three layers, computed separately (SCREEN-01 established why conflating them fails):

1. **Fees** — gross paid by users (mostly to liquidity/supply side)
2. **Holders revenue** — what provably reaches token holders (buyback, burn, dividend)
3. **Capture rate** = layer 2 ÷ layer 1

Then the correction almost nobody applies on top of the correction almost nobody
applies: **dilution**. Market cap ignores tokens not yet circulating. The honest
denominator is FDV.

```
FDV-adjusted P/HoldersRevenue  =  (mcap / holders_revenue_annualized) × (FDV / mcap)
```

## Results (sorted by FDV-adjusted P/HREV)

| Protocol | Ticker | P/HREV | Capture | FDV/MC | **FDV-adj** | HREV/yr | 30d |
|---|---|---|---|---|---|---|---|
| Canton | CC | 7.3x | **100%** | **1.00** | **7.3x** | $674M | −16% |
| Pump.fun | PUMP | 4.8x | 55% | 2.12 | **10.2x** | $164M | +31% |
| GMX | GMX | 11.8x | 27% | **1.00** | **11.8x** | $6M | +8% |
| Convex | CVX | 14.3x | **98%** | 1.09 | **15.6x** | $8M | 0% |
| deBridge | DBR | 12.1x | *152%* | 1.69 | 20.4x | $8M | +13% |
| Geodnet | GEOD | 9.9x | 80% | 2.12 | 21.0x | $9M | −3% |
| PancakeSwap | CAKE | 33.6x | 20% | 1.04 | 34.9x | $13M | +1% |
| edgeX | EDGE | 13.0x | 18% | 2.86 | 37.2x | $11M | +2% |
| Maple | SYRUP | 63.6x | **3%** | 1.07 | 68.0x | $4M | +41% |
| Uniswap | UNI | 50.3x | **5%** | 1.43 | 71.9x | $45M | +21% |
| Aerodrome | AERO | 41.1x | 73% | 2.00 | 82.2x | $11M | −17% |
| Lighter | LIT | 23.6x | 76% | **4.00** | 94.4x | $25M | +49% |
| TRON | TRX | 98.9x | 100% | 1.00 | 98.9x | $315M | +1% |
| **Hyperliquid** | HYPE | 28.3x | 71% | **4.29** | **121.4x** | $487M | −9% |
| Injective | INJ | 165.9x | 100% | 1.00 | 165.9x | $3M | +6% |
| Aave | AAVE | 207.8x | **2%** | 1.04 | 216.1x | $7M | +27% |

## The inversions this exposes

The naive fee screen (SCREEN-01) and the corrected screen disagree violently:

| Asset | Naive P/Fees | FDV-adj P/HREV | Error factor |
|---|---|---|---|
| Maple | 1.8x ("cheapest in crypto") | 68.0x | **38x** |
| Uniswap | 2.4x | 71.9x | **30x** |
| Aave | 4.1x | 216.1x | **53x** |
| Hyperliquid | 20.5x ("expensive") | 121.4x | 6x |
| Canton | 7.4x | **7.3x** | **1.0x — no correction needed** |

Two structural findings:

- **Low capture is the dominant value trap.** Uniswap, Maple and Aave generate large
  fees that overwhelmingly do not reach token holders (5%, 3%, 2%). Every "crypto P/E"
  chart ranking them cheap is measuring the wrong layer.
- **High capture plus high dilution is the second trap.** Hyperliquid's 71% capture is
  genuinely strong, but with FDV 4.29× circulating mcap, the fully-diluted multiple is
  121x. Dilution silently undoes capture quality. Lighter (76% capture, 4.00 FDV/MC)
  has the same structure.

## Outlier verification

Canton's figures were extraordinary enough to require external checks before being
reported: institutional L1 built by Digital Asset with DTCC, JPMorgan, Franklin
Templeton, Visa and Broadridge as infrastructure participants; ~$65.5M monthly fees
from institutional transaction activity rather than speculative volume;
**burn-and-mint equilibrium** (fees burned → structural 100% capture); **no pre-mine
and no VC allocation**, which independently explains FDV/MC = 1.00. Canton Strategic
Holdings listed on NASDAQ (CNTN) after a $545M private placement. The data survives
scrutiny; the caveats in the next section still apply in full.

## What this screen CANNOT see — permanent caveats

1. **Efficiency.** A low multiple may be correctly priced for risks the screen cannot
   observe. Cheap is not the same as mispriced.
2. **Durability.** 30-day revenue annualized assumes conditions persist. A launchpad
   earning during a memecoin cycle is not an annuity; institutional throughput and
   speculative throughput have different half-lives.
3. **Capture > 100%** (deBridge, 152%) means payouts exceed fees — subsidy, not
   profit. Structurally unsustainable and a red flag, not a bargain.
4. **Counterparty, contract, governance and regulatory risk** are entirely outside
   this screen.
5. **Liquidity.** Small caps cannot absorb size without slippage — which is also
   precisely why they are ignored by large funds.
6. **Join integrity.** Name-based matching across two APIs; every candidate requires
   manual confirmation before it means anything.

## Status

Reproducible screen, versioned. When EE-003/EE-004 are implemented this runs on
schedule and every derived probabilistic claim is pre-registered per RFC-0018.
