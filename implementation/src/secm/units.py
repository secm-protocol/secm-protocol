"""Canonical metadata unit builder — RFC-0002 envelopes.

Internal plumbing shared by engines: builds units that pass the RFC-0007
validator. Engines decide semantics; this module only assembles envelopes.
"""

from __future__ import annotations

import datetime
import uuid


def build_unit(
    *,
    semantic_type: str,
    entity_ref: str,
    engine: dict,
    value: dict,
    confidence: float,
    provenance: list[str],
    transformation_name: str,
    transformation_description: str,
    source_tradition: str,
    parameters_hash: str,
    consent_scope: str | None = None,
) -> dict:
    unit = {
        "schema_version": "0.1.0",
        "id": str(uuid.uuid4()),
        "entity_ref": entity_ref,
        "semantic_type": semantic_type,
        "engine": dict(engine),
        "transformation": {
            "name": transformation_name,
            "description": transformation_description,
            "source_tradition": source_tradition,
            "parameters_hash": parameters_hash,
        },
        "value": value,
        "confidence": round(float(confidence), 4),
        "provenance": list(provenance),
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    if consent_scope is not None:
        unit["consent_scope"] = consent_scope
    return unit
