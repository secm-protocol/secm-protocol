# Contributing to SECM

SECM accepts contributions from humans and AI workforces — under one inviolable rule:

> **No line of code may exist without a corresponding RFC.**
> (Architect's Charter, principle 3 — operationalized by RFC-0001 §5 change classes)

## The flow

Every change follows the founding flow:

```
Vision
  ↓
Chief Architecture Intelligence  (architecture, coherence review)
  ↓
RFC  (specification — approved before any implementation)
  ↓
Engineering Workforce  (implements exactly what the RFC specifies)
  ↓
Code → Tests → Benchmark → Validation
  ↓
Merge
```

Implementation workforces receive **specifications, never ideas**. The instruction is
always *"implement this RFC exactly as specified"* — never *"build what you think is
best"*. Implementation work is scoped **per RFC**: an implementer works on one RFC at a
time, which reduces errors and keeps the architecture consistent.

## Branch model

```
main            – protocol releases only
release         – release preparation
develop         – integration
feature/rfc-XXXX – one branch per RFC
```

All work is anchored to an RFC number.

## How to propose a change

1. Classify it (RFC-0001 §5): Class 1 (trivial — PR directly), Class 2 (substantive —
   RFC required), Class 3 (constitutional — RFC + amendment process).
2. For Class 2/3: copy `rfcs/RFC-TEMPLATE.md` into `rfcs/drafts/draft-<topic>.md`.
   The **premortem section is mandatory** (RFC-0000 §18).
3. AI-authored proposals must be labeled with their AI author (RFC-0001 §7).
4. Drafts receive an RFC number only on acceptance. Rejected/superseded drafts are
   archived, never deleted.

## Authors and Contributors

Every accepted contribution is registered in [AUTHORS.md](AUTHORS.md) — an RFC, an
engine, a benchmark, a validation attack that found a real flaw. The protocol remembers
who built it. The protocol still belongs to no one.

## Validation and Security workforces

Trying to break the protocol is a first-class contribution. Reproducible reports of
architectural incoherence, privacy leaks, calibration failures or hidden transformations
are treated with the same respect as feature work.
