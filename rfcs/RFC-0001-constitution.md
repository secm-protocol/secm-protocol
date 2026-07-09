# RFC-0001 — Operational Constitution

| Field | Value |
|---|---|
| **RFC** | 0001 |
| **Title** | Operational Constitution: Governance Mechanics |
| **Status** | Draft — awaiting Vision Keeper ratification |
| **Class** | 3 (Constitutional) |
| **Authors** | Vision Keeper (Osvaldo); drafted by Implementation Workforce (Claude) |
| **Requires** | RFC-0000 |
| **Created** | 2026-07-08 |

## Summary

RFC-0000 defines the mission, philosophy and principles of SECM. This RFC defines the
**operational mechanics** that make those principles executable: who decides, how rules
are amended, what happens when principles conflict, how success is measured, and which
changes require which process. It closes the three structural gaps identified before v1.0
(undefined consensus, no amendment process, no precedence rule) and adds two practical
mechanisms (measurable success criteria, tiered change classes).

Nothing in this RFC modifies the mission or philosophy of RFC-0000.

---

## 1. Immutable Core

The following elements of RFC-0000 are **immutable** — they may never be amended,
suspended or reinterpreted away, by anyone, under any process:

- §2 — Core Mission (*reduce the waste of human potential through explainable knowledge convergence*)
- §5 — Human-Centered Principle
- §20 — Things SECM Will Never Become
- §24 — Final Constitutional Statement

Everything else in the protocol, including this RFC, is amendable under §3 below.

## 2. Governance Phases and Consensus Definition

"Protocol Consensus" (RFC-0000 §9, §14) is defined per governance phase:

### Phase 1 — Founding (current)

- The **Vision Keeper** holds final decision authority over all change classes.
- The Chief Architecture Intelligence and all workforces are **advisory**: they propose,
  analyze and implement; they never decide.
- Consensus = explicit written approval by the Vision Keeper, recorded in the RFC's
  status history.

### Phase 2 — Council

Triggered when the project has **three or more human maintainers** with sustained
contribution (defined as meaningful contributions across at least 6 months), formalized
by a Class 3 decision.

- **Class 2 (substantive) changes:** simple majority of the Maintainer Council.
- **Class 3 (constitutional) changes:** two-thirds supermajority of the Council **and**
  Vision Keeper assent while the founding Vision Keeper is active.
- Tie-breaking: the Vision Keeper; after the founding Vision Keeper's tenure, the
  Council must define a successor mechanism by Class 3 decision **before** the transition.

No phase transition is automatic. Every transition is itself a Class 3 decision.

## 3. Amendment Process

Real constitutions survive because they can be amended — with a high bar.

1. Amendment proposals are Class 3 RFCs and must include a mandatory **premortem**
   (RFC-0000 §18).
2. **Review period:** minimum 30 days in Phase 1, 90 days in Phase 2, between publication
   of the proposal and the consensus decision. No fast track exists for Class 3.
3. Approved amendments never rewrite history: the amended text is published as a new RFC
   that supersedes specific sections, and the original remains archived (Historical
   Registration, RFC-0000 §14).
4. The Immutable Core (§1 above) is outside the reach of this process.

## 4. Precedence Hierarchy

When two protocol principles conflict in a concrete decision, the higher rank prevails:

1. **Human protection and dignity** — including privacy, data protection and the right
   of a person to control their own data.
2. **Explainability and auditability** — no capability justifies a hidden transformation.
3. **Evidence and validation** — validated evidence outranks tradition, convenience and
   authority.
4. **Historical preservation** — records are kept, but never at the cost of ranks 1–3
   (e.g., personal data is erasable; only content-free proofs are permanent — see
   draft: Privacy Architecture).
5. **Performance and efficiency** — always last. Never traded against the ranks above.

**Interpreter:** conflicts are resolved by the Vision Keeper (Phase 1) or the Council
(Phase 2). Every interpretation is recorded with its reasoning and becomes precedent.

## 5. Change Classes

RFC-0000 §22 rule 1 ("no feature before RFC") is operationalized in three classes, so
that the rule is always followed instead of routinely violated:

| Class | Scope | Process |
|---|---|---|
| **1 — Trivial** | Typos, formatting, comments, non-behavioral refactors, documentation clarity | Review + merge. No RFC. |
| **2 — Substantive** | New engines, schema changes, algorithm changes, new Solvers, anything behavioral | RFC required. Full pipeline: Proposal → Validation → Benchmark → Sandbox → Consensus → Implementation → Historical Registration. |
| **3 — Constitutional** | Governance, principles, precedence, Foundation Engine identity, phase transitions | RFC + Amendment Process (§3). |

If classification is disputed, the higher class applies.

## 6. Measurable Success and Validation Authority

RFC-0000 §19 defines success qualitatively. This section makes it enforceable:

1. Every success claim of the protocol must be operationalized into a **measurable
   benchmark** — e.g., confidence calibration error against observed outcomes,
   directional estimation accuracy tracked over time, reproducibility of convergence
   results.
2. **Validation authority:** the Validation Engine (FE-008) has authority over the
   convergence **weight** of every engine — Foundation Engines included. Foundation
   Engine *identity* is permanent (RFC-0000 §8); Foundation Engine *weight* in
   convergence is earned through validated evidence and recalibrated as evidence
   accumulates. An engine whose transformations demonstrate no validated signal
   converges toward zero weight without ceasing to exist.
3. No engine, author or tradition is exempt from measurement. This is what
   permanently separates SECM from belief systems (RFC-0000 §20).

## 7. AI Authority Limits

Restating and operationalizing RFC-0000 §16:

- No AI holds constitutional authority, decision authority or veto.
- AI-authored proposals are labeled with their AI author and enter the same RFC process
  as any proposal; they carry no special weight.
- AI workforces operate through task-specific interfaces under Zero Trust (RFC-0000 §15).

## Premortem (mandatory, RFC-0000 §18)

1. **What could fail?** Phase 1 concentrates authority in one person; mitigated by public
   auditability of every decision and the immutable core.
2. **What assumptions are wrong?** The Phase 2 trigger (3 maintainers / 6 months) may be
   miscalibrated; it is amendable by Class 3 without touching the immutable core.
3. **What biases may emerge?** Founder bias in precedence interpretation; mitigated by
   recorded precedent and mandatory reasoning.
4. **How is reversibility guaranteed?** Every section except the Immutable Core is
   amendable via §3; superseded texts remain archived.
5. **How is explainability preserved?** All decisions, interpretations and amendments are
   written, reasoned and historically registered.
