# DRAFT — Contribution Weight System (CWS): Pseudonymous, Work-Earned Governance

| Field | Value |
|---|---|
| **Status** | Draft — awaiting Vision Keeper review |
| **Class** | 3 (Constitutional — defines voting weight) |
| **Authors** | **Vision Keeper (Osvaldo)** — requirements; Implementation Workforce (Claude — AI, design and drafting) |
| **Requires** | RFC-0000, RFC-0001 |
| **Created** | 2026-07-08 |

## Summary

Decision weight in SECM is **earned through accepted work and bound to a cryptographic
key — never to an identity**. Contributors gain real voting power proportional to
validated contributions; the founder holds significant but not sole weight; and no one —
including the protocol and the Vision Keeper — can learn who a contributor is unless
that person voluntarily discloses it. This is proof-of-accepted-work governance.

## Motivation

Direction set by the Vision Keeper: the protocol must survive without depending on him;
contributors who feed the protocol must gain decision force; his weight is greater as
founder and first developer, but never the only one; and contributor identity must be
protected **even from the protocol itself**.

Identity-based solutions available in this era — biometric proof-of-personhood,
state-ID KYC, social-graph verification — all violate that requirement and precedence
rank 1 (human protection, RFC-0001 §4). They are **explicitly rejected**. The honest
remaining model ties weight to work the community accepted, exactly as pseudonymous
authorship has always worked: the work carries the weight, not the name.

## Specification

### 1. Contributor identity = a signing key

- A contributor is an asymmetric keypair (Ed25519 or equivalent). The public key
  fingerprint is the contributor's permanent pseudonymous ID.
- Registration is implicit: the first accepted contribution records the fingerprint in
  the ledger. No name, e-mail verification or identity document is ever required.
- Voluntary self-disclosure is allowed but **grants zero additional weight**. This
  invariant is constitutional: if disclosure gave advantage, social pressure to
  de-anonymize would follow.

### 2. Contribution Points (CP)

Points are granted **only when a contribution is accepted** through the normal pipeline
(RFC-0000 §14) — never by automatic metrics. Commits, lines of code and activity volume
are worth nothing by themselves (anti-Goodhart rule).

| Accepted contribution | Points |
|---|---|
| Class 3 RFC (constitutional) | 50 |
| Class 2 RFC (substantive) | 20 |
| Implementation of an RFC (merged + validated) | 15 |
| Validated security/validation finding | 10–30 by severity |
| Benchmarks, test suites, substantial documentation | 5 |
| Class 1 (trivial) | 1 — capped at 10 per quarter per key |

The point award is part of the acceptance decision itself and is recorded in a public,
append-only, signed ledger (`governance/contribution-ledger.md`): date, key
fingerprint, contribution reference, class, points, decided-by. Anyone can recompute
every weight from the ledger (RFC-0000 §22 — auditable).

### 3. Active weight and decay

Voting weight uses **exponential decay with a 24-month half-life** (parameter):
`weight = Σ points × 2^(−months_since_award / 24)`.

Power stays with those who sustain the protocol; abandoned keys fade automatically.
Nothing is ever deleted — only decayed.

### 4. Maintainer threshold

A key with active weight **≥ 100** (parameter) is a **maintainer**: a voting member of
the Phase 2 Council. This makes the RFC-0001 §2 phase trigger objective: Phase 2 becomes
possible when 3+ keys hold maintainer status.

### 5. Voting weight function

**Linear in active weight**, with one optional cap: no single non-founder key may
exceed **25%** (parameter) of total non-founder voting weight in a given vote.

Linear weighting is chosen deliberately: concave functions (square root, logarithm)
reward splitting one person's work across several pseudonyms; superlinear functions
create oligarchy. Linear is split-neutral — the only Sybil-neutral choice available
without identity verification.

### 6. Founder weight

While active, the founding Vision Keeper holds a **fixed 25% share** (parameter) of
total voting weight in any weighted vote, plus the Class 3 assent right of RFC-0001 §2.
Founder privileges are personal and non-inheritable (RFC-0001, Continuity and
Succession). The founder may also earn CP like any contributor, recorded in the same
public ledger under the same rules.

### 7. Privacy boundaries — stated honestly

- The protocol never requires identity, never records identity, and never conditions
  weight on identity.
- Platform-level metadata (e.g., the Git host sees IP addresses and account data) is
  **outside the protocol's control**. Contributors who need strong anonymity must use
  their own operational security; the protocol's guarantee is that it will never demand
  more than a key.

## Honest limits of this design

Stated openly, because hiding them would violate §22:

1. **Sybil:** one human can hold several keys — undetectable by design, since detection
   would require identity. Defense: weight tracks *accepted work*, which costs real
   effort and passes human review either way; linear weighting makes splitting
   pointless. The per-key cap slightly rewards splitting for very large contributors —
   that is the price of the cap, and the cap is a parameter.
2. **Key sale or transfer:** cryptographically undetectable. Mitigations: decay makes
   dormant purchased keys lose value, and the founder assent right guards the
   constitutional layer during the founding era.
3. **Humanity is unverifiable.** A pseudonymous key could be operated by an AI. The
   constitutional rule "no AI decision authority" (RFC-0001 §7) therefore operates on
   accountability: every key is presumed to act under a human's responsibility, and
   declared AI workforces remain advisory. This is the maximum honesty possible without
   identity verification.
4. **Meritocracy of available time:** those with more free time accumulate weight
   faster. Inherent to every open-source governance model; decay softens it, nothing
   eliminates it.

## Validation Criteria

- **Reproducibility:** any third party recomputes all weights from the public ledger
  and obtains identical results, bit for bit.
- **Decay correctness:** property tests on the weight function (monotonic decay, no
  negative weights, split-neutrality of linear weighting).
- **Dry run:** one full simulated Class 2 vote executed end-to-end from ledger data
  before the system governs anything real.

## Parameters for Vision Keeper decision

| Parameter | Proposed | Notes |
|---|---|---|
| Decay half-life | 24 months | shorter = power more current, harsher to veterans |
| Maintainer threshold | 100 CP active | ~2 substantive RFCs + implementations |
| Founder share | 25% | fixed while active; lapses per succession rules |
| Per-key cap | 25% of non-founder weight | optional; removable |
| Point schedule | table above | amendable by Class 3 |

## Premortem (mandatory — RFC-0000 §18)

1. **What could fail?** Point farming via low-value RFCs → mitigated: acceptance goes
   through consensus + Class 1 caps; schedule amendable if gamed.
2. **Wrong assumptions?** That accepted-work cost deters Sybil sufficiently; if proven
   wrong, parameters (threshold, cap) are tunable without constitutional change.
3. **Biases?** Early contributors accumulate compounding influence → decay bounds it;
   founder share is explicit rather than hidden.
4. **Reversibility?** The ledger is append-only and public: any weight rule change
   recomputes cleanly over the same history.
5. **Explainability?** Every unit of power in the system traces to a dated, signed,
   public ledger entry. No hidden weight exists.

## Status History

| Date | Status | Decided by |
|---|---|---|
| 2026-07-08 | Draft | — |
