"""FE-001 Nominal Encoding System — RFC-0022 v0.1.

Decomposes the historical Pythagorean letter-value table into a neutral
computational transformation (RFC-0000 §4): only the arithmetic is
extracted, never the mystical interpretation. Never expose mystical
terminology (Life Path, Soul Number, Expression Number) — internally or
externally; only neutral field names.

Confidence baseline is deliberately very low: this is an unvalidated
historical transformation with zero established evidence connecting it
to real-world outcomes. FE-008 (RFC-0018) is the only path to a higher
weight, and only through real calibration data.

Privacy: PERSON_NAME is Tier 0 (RFC-0008) — consumed in-memory only,
never stored. Output values are irreversible by construction: a name
collapses to one of ~12 possible single values, which cannot recover
the original name — a stronger guarantee than hashing (RFC-0008 warns
that hashing low-entropy personal data like names is not anonymization).
"""

from __future__ import annotations

import hashlib
import json

from ..reduction import reduce_number
from ..units import build_unit

ENGINE = {"id": "FE-001", "version": "0.1.0"}

BASELINE_CONFIDENCE = 0.15

SOURCE_TRADITION = "Pythagorean numerical encoding, decomposed per RFC-0000 §4"

# Classical Pythagorean letter-value table (A-Z, repeating 1-9). Decomposed
# as pure arithmetic per RFC-0000 §4 — the mystical interpretation is not
# adopted, only this deterministic mapping.
_LETTER_VALUES = {
    letter: (i % 9) + 1 for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
}
_VOWELS = frozenset("AEIOU")


def parameters_hash() -> str:
    payload = {
        "engine": ENGINE,
        "letter_values": _LETTER_VALUES,
        "vowels": sorted(_VOWELS),
        "baseline_confidence": BASELINE_CONFIDENCE,
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()


def _letters_only(name: str) -> str:
    return "".join(ch for ch in name.upper() if ch in _LETTER_VALUES)


def encode(name: str, *, entity_ref: str, consent_scope: str) -> dict:
    """Transform a full birth name into neutral nominal-structure metadata.

    The name is consumed in-memory only (Tier 0, RFC-0008) — the caller
    must discard the raw name after this call returns; it is never stored.
    """
    letters = _letters_only(name)
    if not letters:
        raise ValueError("name must contain at least one A-Z letter after normalization")

    total = sum(_LETTER_VALUES[c] for c in letters)
    vowels = sum(_LETTER_VALUES[c] for c in letters if c in _VOWELS)
    consonants = sum(_LETTER_VALUES[c] for c in letters if c not in _VOWELS)

    return build_unit(
        semantic_type="PERSON_NOMINAL_STRUCTURE",
        entity_ref=entity_ref,
        engine=ENGINE,
        value={
            "total_reduction": reduce_number(total),
            "vowel_reduction": reduce_number(vowels) if vowels else None,
            "consonant_reduction": reduce_number(consonants) if consonants else None,
        },
        confidence=BASELINE_CONFIDENCE,
        provenance=["descriptor:rx-intake:v0.1:Q1"],
        transformation_name="nominal-letter-value-reduction",
        transformation_description=(
            "sums Pythagorean letter-values over all letters / vowels / "
            "consonants of the birth name and reduces each sum by repeated "
            "digit-sum, halting at repdigit multiples of 11 (RFC-0022 v0.1)"
        ),
        source_tradition=SOURCE_TRADITION,
        parameters_hash=parameters_hash(),
        consent_scope=consent_scope,
    )
