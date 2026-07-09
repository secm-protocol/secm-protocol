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
| Blockchain anchoring | Pending — RFC required (chain choice, anchoring format) |
| Mirrors | Pending — after v1.0 |
