# Preservation Architecture

> **"A protocol that intends to survive for decades cannot depend on a single service,
> a single company or a single technology to preserve its existence."**
> — founding decision, recorded in the Architect's Charter (principle 7)

SECM is preserved across four independent layers. Blockchain is deliberately **not**
the birthplace of the protocol — it is excellent for immutability, proof of existence
and consensus, and bad for writing documentation, evolving specifications and
discussing RFCs. Each layer does only what it is best at.

## Layer 1 — GitHub (the living home)

The official development and governance environment: code, RFCs, protocol, discussions,
versioning, issues, pull requests.

- Lives in an **organization** (`github.com/secm-protocol`), never a personal account.
  The protocol has no owner.
- Branch model: `main` → `release` → `develop` → `feature/rfc-XXXX`.
  All work is anchored to RFCs.

## Layer 2 — Zenodo (the permanent citable archive)

GitHub's official Zenodo integration turns every Release into a permanently archived,
**DOI-carrying** version. Every version of the Constitution and the protocol becomes
citable and can never be lost.

- Trigger: each protocol Release (starting at v1.0).
- Result: `Release → Zenodo → DOI` — one DOI per version, forever.

## Layer 3 — Blockchain (proof, not storage)

The chain never stores documents. It registers only:

- content **hash**
- **version**
- **timestamp**
- **DOI**

Anyone can prove a given document existed, unmodified, at a given date — without any
content (including personal data) ever touching the chain. This is required by the
Privacy Architecture: only content-free proofs are permanent.

**Multi-chain by design (Vision Keeper decision, 2026-07-09).** The protocol never
subjects itself to a single blockchain — that would recreate the single point of
failure this layer exists to eliminate (Architect's Charter, principle 7). Each release
proof is anchored on **at least two independent chains** (candidates: Bitcoin,
Ethereum, Solana, Polygon — the exact set, anchoring format and rotation rules are
fixed by the anchoring RFC). A hash is tiny; anchoring it twice costs almost nothing
and survives the death of any one chain.

## Layer 4 — Public Mirrors

- Internet Archive
- Software Heritage (for code)
- Additional public mirrors as they become available

The protocol survives even if any single service disappears.

## The full pipeline

```
GitHub → Release → Zenodo → DOI → Hash → Blockchain → Mirrors
```

## Status

| Layer | Status |
|---|---|
| GitHub organization | Pending — to be created by the Vision Keeper (`secm-protocol`) |
| Zenodo integration | Pending — activated at first Release (v1.0) |
| Blockchain anchoring | Pending — RFC required; **multi-chain (≥2 independent chains) decided 2026-07-09** |
| Mirrors | Pending — after v1.0 |
