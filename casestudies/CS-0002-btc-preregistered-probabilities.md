# CS-0002 — BTC: Pre-Registered Probabilistic Statements (Calibration Exercise)

| Field | Value |
|---|---|
| **Case study** | 0002 — the protocol puts its own numbers on the record |
| **Status** | **Pre-registered 2026-07-18** — statements may never be edited, only resolved |
| **Authors** | Implementation Workforce (Claude — AI); demanded by Vision Keeper (Osvaldo) |
| **Method** | Base-rate analysis over cycle history (n=3, stated), current structural data (see sources), market-implied probabilities where liquid markets exist |
| **Purpose** | **Calibration measurement of the method — explicitly NOT investment advice, NOT trade signals.** Nobody should size a position off this document; its purpose is to produce a scoreable Brier record. |

## Context snapshot (2026-07-18, sourced)

BTC ≈ $63–65k. ATH $125,836 (2025-10-06) → current drawdown ≈ −50%. Cycle position:
~27 months post-halving (2024-04), ~9 months post-peak. Peak occurred ~17.5 months
post-halving — third consecutive cycle peaking in the 17–18 month window (n=3).
June 2026: worst ETF-outflow month on record (−$4.5B); 8-week outflow streak broken
this week (+$1.2B/7d). Fed 3.50–3.75%, 2026 inflation revised up to 3.6%,
market-implied ~46% probability of a hike on 2026-07-29.

## Pre-registered statements

Resolution source for price statements: CoinMarketCap BTC/USD daily OHLC (intraday
touch counts). Each statement carries a point estimate and an honesty band.

| ID | Statement | P (band) | Resolves |
|---|---|---|---|
| **S1** | BTC trades below **$55,000** at any point before 2027-01-01 | **0.50** (0.40–0.60) | 2027-01-01 |
| **S2** | BTC trades below **$40,000** at any point before 2027-07-01 | **0.25** (0.15–0.40) | 2027-07-01 |
| **S3** | BTC sets a **new ATH** (> $125,836) before 2027-01-01 | **0.07** (0.03–0.12) | 2027-01-01 |
| **S4** | BTC sets a new ATH before 2028-07-01 | **0.45** (0.30–0.60) | 2028-07-01 |
| **S5** | Fed **hikes** at the 2026-07-29 FOMC | **0.46** (adopted from market) | 2026-07-29 |

### Reasoning, stated so it can be attacked

- **S1/S2:** the three prior post-peak years all continued lower after a −50%
  drawdown, bottoming −77% to −84% from ATH, ~12–14 months after the peak (analog
  window: Q4-2026). Offsetting: structural regime change (ETF/institutional bid did
  not exist in prior bears) and the first flow stabilization in two months. Hence
  probabilities near coin-flip for S1 and well below analog-implied for S2 —
  the regime-change discount is explicit, not decorative.
- **S3/S4:** no prior cycle reclaimed its ATH sooner than ~27 months after the peak
  (2021→2024: ~28mo; 2017→2020: ~36mo). October 2025 + 27mo = January 2028. S4's
  window ends mid-2028, straddling the earliest analog reclaim — hence near 50/50.
- **S5:** for events with liquid prediction/rate markets, the protocol's best
  estimate **is** the market price. Anyone claiming a better number is claiming to
  beat the world's most heavily arbitraged aggregator — a claim that requires a
  Brier ledger, not confidence.

### Sample-size warning, permanent

Every cycle-analog statement above rests on **n=3**. Three observations establish a
rhyme, not a law. The ETF-era regime change weakens the analogy in an unknowable
direction. This is the maximum honest precision available from public data — anyone
offering tighter certainty from the same data is selling, not measuring.

## Scoring

On each resolution date, outcomes are appended below and Brier-scored
(RFC-0018 arithmetic). The protocol's record stands public — right or wrong.

## Resolution log

| Date | Statement | Outcome | Brier |
|---|---|---|---|
| *(appended on resolution — never edited above this line)* | | | |
