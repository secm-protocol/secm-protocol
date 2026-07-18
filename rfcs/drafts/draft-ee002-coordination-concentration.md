# DRAFT — EE-002 Coordination Concentration Engine

| Field | Value |
|---|---|
| **Status** | Draft — **deferred by design**: implementation gated on data prerequisites |
| **Class** | 2 (Substantive — Extension Engine, per RFC-0000 §9) |
| **Authors** | **Vision Keeper (Osvaldo)** — source material; Implementation Workforce (Claude — AI, drafting) |
| **Requires** | RFC-0002, RFC-0009, RFC-0014, RFC-0012, and live network/ownership/lobbying data |
| **Created** | 2026-07-09 |

## Summary

A second Extension Engine candidate: quantifies **coordination concentration** in a
domain, institution, or market — how much control sits with a small, coordinated
actor-network versus how diffuse it is — using real, public, verifiable datasets
(ownership concentration, board-interlock network centrality, lobbying-expenditure
concentration). It formalizes the mechanism popularized in conspiratorial framing as
"secret societies control everything" into its measurable, falsifiable core.

## Honest provenance of the idea

Source: Prof. Jiang's lecture "Templários, Bafomé e o Poder" analyzes secret-society
conspiracy theories as a "metaphorically true" compression of a real dynamic — small,
motivated, coordinated groups systematically outcompete large diffuse ones, and this
effect compounds as systems scale. The lecturer himself states plainly there is no
evidence for the literal claims (centuries-long society continuity, demon
invocation, Baphomet worship) and that this framing is intentionally metaphorical, not
factual.

Decomposed per RFC-0000 §3–4, the extractable computational transformation is **not**
occult continuity. It is three established, independently-verified academic theories:

- **Michels' Iron Law of Oligarchy** (1911) — large organizations are structurally
  driven toward control by a coordinated minority.
- **Olson's Logic of Collective Action** (1965) — concentrated-interest groups
  systematically defeat diffuse-interest groups because they can coordinate and avoid
  the free-rider problem; empirically the standard explanation for why concentrated
  lobbies out-influence diffuse public interest across policy domains.
- **Stigler's Theory of Economic Regulation** (1971) / Pareto's circulation of elites
  — regulatory capture and elite succession without structural change in who holds
  concentrated power.

These are real, testable, decades-replicated theories — nothing here requires belief
in secret societies, only network structure and coordination costs.

## Motivation

If concentration of coordination capacity in a person's domain or region is
measurable, it is genuine directional context: entering a market/industry where
control is highly concentrated in a small coordinated network behaves differently
than entering a diffuse, competitive one — for opportunity, negotiating leverage, and
risk.

## Specification (v0.2 scope)

1. **Inputs:** declared, registered datasets only (RFC-0014 source registry) —
   candidates: market-concentration indices (e.g. Herfindahl-Hirschman Index, already
   used by antitrust regulators), public lobbying-expenditure disclosures, board
   interlock / corporate network datasets, legislative-outcome-vs-lobbying-concentration
   studies. No proprietary, non-public, or unverifiable source is ever used.
2. **Transformation:** standard network-concentration and market-concentration
   arithmetic (HHI computation, network centrality measures over public interlock
   data) — well-established, auditable formulas, not interpretation.
3. **Output:** a `ECON_COORDINATION_CONCENTRATION` unit (registry amendment on
   acceptance): domain/region, concentration index, network centrality summary,
   source dataset citations. Confidence reflects data coverage and recency — never
   asserted as revealing intent or hidden agency.
4. **Hard gate:** no output is produced for a domain/region without a registered,
   public, verifiable dataset covering it. Silence over invention, as always.
5. **Weight:** earned via FE-008 like every engine (RFC-0001 §6).

## What this engine will never be

No claims of secret-society continuity, ritual, demonic influence, or hidden agency
behind concentration patterns. No naming or profiling of specific living individuals
as members of any occult or conspiratorial group — that is unverifiable and outside
the protocol's mandate (RFC-0000 §20). The engine measures **structural concentration
of coordination capacity**, a property of networks and markets, never a claim about
belief systems or intentions.

## Validation Criteria

- HHI and centrality computations verified against known reference datasets.
- No output without a registered public source citation.
- No end-user-facing or internal terminology referencing secret societies, occult
  practice, or named living individuals as conspiratorial actors.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Being read as validating conspiratorial framing → the RFC
   text and every output explicitly separates the measurable mechanism (network/
   market concentration) from the unfalsifiable mystical layer, which is rejected.
2. **Wrong assumptions?** That concentration data alone implies coordinated intent —
   it does not; the engine reports structural concentration, not motive.
3. **Biases?** Coverage will be uneven (some markets/regions have public interlock
   data, most don't) — coverage gaps are reported explicitly, never silently filled.
4. **Reversibility?** Pure analysis over public data; nothing destructive.
5. **Explainability?** Every concentration figure cites its formula and source
   dataset — fully recomputable by anyone.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-09 | Draft, deferred until data prerequisites are met | — |
