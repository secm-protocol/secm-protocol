"""Personal metadata aggregation — RFC-0004 v0.1 (minimal slice).

Maps the "Personal Metadata Graph" concept onto the existing schema:
every metadata unit already carries entity_ref (RFC-0002). This module
is a read-side aggregation over units already produced by engines — not
new storage, not a new constitutional structure. A full graph database
is future Class 2 work; v0.1 proves the concept cheaply.
"""

from __future__ import annotations


def person_metadata(entity_ref: str, units: list[dict]) -> dict:
    """Aggregate all metadata units for one entity into a namespace-grouped view."""
    by_namespace: dict[str, list[dict]] = {}
    for unit in units:
        if unit.get("entity_ref") != entity_ref:
            continue
        namespace = unit["semantic_type"].split("_", 1)[0]
        by_namespace.setdefault(namespace, []).append(
            {
                "semantic_type": unit["semantic_type"],
                "engine": unit["engine"]["id"],
                "value": unit["value"],
                "confidence": unit["confidence"],
                "created_at": unit["created_at"],
            }
        )
    return {"entity_ref": entity_ref, "metadata": by_namespace}
