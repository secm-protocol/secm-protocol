# SECM Environmental Ingestion — Public Source Registry

Constitutional basis: RFC-0014 §2 — **no undeclared sources, ever**. A hidden feed is
a hidden transformation (RFC-0000 §22). Registry changes are Class 2. Breadth is
unlimited for trustworthy sources (Vision Keeper directive, 2026-07-09); this registry
gates trust, never breadth.

## Registered sources

| ID | Source | Feed | Indicator | Cadence | License/terms | Source class | Feeds |
|---|---|---|---|---|---|---|---|
| bcb-sgs-432 | Banco Central do Brasil — SGS | Série 432 (Meta Selic, % a.a.) | `interest_rate` | daily | BCB open data | official statistics (E1) | `ECON_INDICATOR` |
| bcb-sgs-433 | Banco Central do Brasil — SGS | Série 433 (IPCA, variação mensal %) | `inflation` | monthly | BCB open data | official statistics (E1) | `ECON_INDICATOR` |
| bcb-sgs-1 | Banco Central do Brasil — SGS | Série 1 (câmbio USD/BRL) | `exchange_rate` | daily | BCB open data | official statistics (E1) | `ECON_INDICATOR` |

API: `https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados/ultimos/{n}?formato=json`

**Live verification 2026-07-09:** Selic meta 14.25% a.a.; IPCA 0.58% (May/2026);
USD/BRL 5.1329. Region emitted: `BR` (national level).

## Candidate sources (not yet registered — each requires Class 2 registration)

IBGE aggregated-data API (regional statistics) · World Bank Open Data · IMF ·
UN Data · Eurostat · GDELT (structured news events).
