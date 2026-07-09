# DRAFT — Protocol Licensing

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review |
| **Class** | 3 (Constitutional — legal foundation of the no-owner principle) |
| **Authors** | Implementation Workforce (Claude — AI, labeled per RFC-0001 §7) |
| **Requires** | RFC-0000, RFC-0001 |
| **Created** | 2026-07-08 |

## Summary

The repository is public but has **no license** — which legally means "all rights
reserved," the exact opposite of a protocol that has no owner. This draft proposes the
legal instruments that make the Architect's Charter principle 1 enforceable in the real
world: **CC BY 4.0** for protocol documents (RFCs, constitution, manifesto) and
**Apache License 2.0** for all future code.

## Motivation

Without a license: nobody may legally reproduce the constitution, mirror the protocol
(breaking PRESERVATION.md layer 4), or contribute derivative work. Contributions become
legally ambiguous. A protocol designed to survive decades and outlive its founders
needs licenses that make capture by any company, person or AI impossible.

## Specification

1. **Documents (RFCs, constitution, manifesto, governance):** Creative Commons
   Attribution 4.0 International (CC BY 4.0). Anyone may copy, mirror, translate and
   build upon the documents — attribution to the SECM Protocol is required, ownership
   claims are impossible.
2. **Code (all future implementations in this organization):** Apache License 2.0.
   Chosen over MIT for its **explicit patent grant** — no contributor can later assert
   patents against protocol users — and over GPL to keep Solvers and Extension Engines
   buildable by anyone, commercially or not, which serves adoption and therefore the
   mission.
3. **Contributor terms:** contributions are accepted under the same licenses
   (inbound = outbound). No CLA transferring ownership to anyone — there is no one to
   transfer to.
4. Repository mechanics: `LICENSE` (Apache 2.0) + `LICENSE-DOCS` (CC BY 4.0) at root,
   with a note in README stating which applies to what.

## Validation Criteria

- GitHub license detection recognizes the repository licensing.
- A third party can legally mirror the full repository (layer 4 preservation) without
  asking permission — verified by the license texts themselves.

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** License choice could deter some contributors → both licenses
   are among the most widely accepted in open source; risk is minimal.
2. **Wrong assumptions?** That Apache 2.0 suits all future code artifacts; specific
   components may propose different terms via Class 3 RFC if ever justified.
3. **Biases?** Permissive licensing favors commercial adopters → deliberate: adoption
   serves the mission; the protocol's integrity is protected by governance, not by
   copyleft.
4. **Reversibility?** Licenses on published versions are irrevocable by design — that
   is their purpose. Future versions may relicense only via Class 3 amendment.
5. **Explainability?** Both licenses are human-readable standards with decades of
   legal interpretation.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-08 | Draft | — |
