"""FE-002 Temporal Encoding System — RFC-0023 v0.1.

Decomposes birth-date arithmetic into neutral computational
transformations (RFC-0000 §4): a digit-sum reduction of the full date,
and the calendar weekday of birth (a plain deterministic fact). Never
expose mystical terminology; only neutral field names.

Confidence baseline is deliberately very low for date_reduction (same
honesty as FE-001: unvalidated historical transformation). birth_weekday
is a deterministic calendar fact — certain as arithmetic, but its
relevance to anything about the person is equally unvalidated, so it
carries the same honest low confidence as a *signal*.

Privacy: PERSON_BIRTH_DATE is Tier 0 (RFC-0008) — consumed in-memory
only, never stored. Only these irreversible derived values persist.
"""

from __future__ import annotations

import datetime
import hashlib
import json

from ..reduction import reduce_number
from ..units import build_unit

ENGINE = {"id": "FE-002", "version": "0.1.0"}

BASELINE_CONFIDENCE = 0.15

SOURCE_TRADITION = "temporal/calendar encoding, decomposed per RFC-0000 §4"

_WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",
)


def parameters_hash() -> str:
    payload = {"engine": ENGINE, "baseline_confidence": BASELINE_CONFIDENCE}
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()


def encode(birth_date: str, *, entity_ref: str, consent_scope: str) -> dict:
    """Transform a birth date (YYYY-MM-DD) into neutral temporal-structure
    metadata. The date is consumed in-memory only (Tier 0, RFC-0008) — the
    caller must discard the raw date after this call returns."""
    date = datetime.date.fromisoformat(birth_date)
    digits = f"{date.day:02d}{date.month:02d}{date.year:04d}"
    date_sum = sum(int(d) for d in digits)

    return build_unit(
        semantic_type="PERSON_TEMPORAL_STRUCTURE",
        entity_ref=entity_ref,
        engine=ENGINE,
        value={
            "date_reduction": reduce_number(date_sum),
            "birth_weekday": _WEEKDAYS[date.weekday()],
        },
        confidence=BASELINE_CONFIDENCE,
        provenance=["descriptor:rx-intake:v0.1:Q2"],
        transformation_name="temporal-date-reduction",
        transformation_description=(
            "sums all digits of the birth date (DDMMYYYY) and reduces by "
            "repeated digit-sum halting at repdigit multiples of 11; also "
            "computes the calendar weekday of birth (RFC-0023 v0.1)"
        ),
        source_tradition=SOURCE_TRADITION,
        parameters_hash=parameters_hash(),
        consent_scope=consent_scope,
    )
