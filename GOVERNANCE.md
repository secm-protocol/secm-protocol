# SECM Governance

Governance mechanics are constitutionally defined in [RFC-0000](rfcs/RFC-0000-genesis.md)
(principles) and [RFC-0001](rfcs/RFC-0001-constitution.md) (operational rules). This file
is a human-readable summary — if it ever conflicts with the RFCs, the RFCs win.

## Roles

| Role | Holder (current) | Authority |
|---|---|---|
| **Vision Keeper** | Osvaldo | Final decision authority (Phase 1). Guardian of purpose: "does this still serve the mission?" |
| **Chief Architecture Intelligence (CAI)** | AI (advisory) | Architecture analysis, RFC drafting, coherence review. Proposes, never decides. |
| **Implementation Workforce** | AI (advisory) | Implements approved RFCs exactly as specified. Code, tests, documentation, benchmarks. |
| **Research / Validation / Security Workforces** | AI + future contributors | Research, attempt to break the protocol, find vulnerabilities. Report, never decide. |
| **Maintainer Council** | — (Phase 2, not yet triggered) | Collective decision body once ≥3 sustained human maintainers exist. |

Constitutional rule: **no AI possesses decision authority**. AI-authored proposals are
labeled as such and enter the same process as any proposal.

## How a change happens

1. Classify the change (RFC-0001 §5):
   - **Class 1 (trivial)** — review + merge, no RFC.
   - **Class 2 (substantive)** — RFC required.
   - **Class 3 (constitutional)** — RFC + amendment process with mandatory review period.
2. Class 2/3 proposals start as a file in `rfcs/drafts/` using [RFC-TEMPLATE](rfcs/RFC-TEMPLATE.md).
3. Pipeline (RFC-0000 §14): Proposal → Validation → Benchmark → Sandbox → Consensus →
   Implementation → Historical Registration.
4. Consensus = Vision Keeper approval (Phase 1), recorded in the RFC status history.
5. Accepted drafts receive the next RFC number. Rejected and superseded drafts are
   archived, never deleted.

## Conflict resolution

Precedence hierarchy (RFC-0001 §4):
**human protection > explainability/auditability > evidence > historical preservation > efficiency.**
Interpretations are recorded with reasoning and become precedent.

## What can never change

The Immutable Core (RFC-0001 §1): the mission, the human-centered principle, the list of
things SECM will never become, and the final constitutional statement of RFC-0000.
