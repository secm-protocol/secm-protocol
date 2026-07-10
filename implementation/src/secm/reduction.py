"""Shared digit-sum reduction algorithm (FE-001, FE-002 — RFC-0022/0023).

Classical technique: repeatedly sum digits until a single digit 1-9,
halting early at repdigit multiples of 11 (11, 22, 33) — a defining
property of the classical algorithm being decomposed (RFC-0000 §4). No
mystical significance is attached to these values internally or
externally; this is pure, deterministic arithmetic.
"""

from __future__ import annotations

_HALT_VALUES = (11, 22, 33)


def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))


def reduce_number(n: int) -> int:
    """Reduce n to a single digit 1-9, or halt at a repdigit multiple of 11."""
    n = abs(n)
    while n > 9 and n not in _HALT_VALUES:
        n = digit_sum(n)
    return n
