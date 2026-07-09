"""RFC-0002 — Protocol Language: canonical metadata unit validation.

Implements the RFC-0002 envelope exactly as specified — nothing beyond it.
Validation returns plain-language errors naming the violated rule, because
outputs must be explainable by construction (RFC-0000 §13, §22).
"""

from __future__ import annotations

import datetime
import re
import uuid

from . import registry

SUPPORTED_SCHEMA_MAJOR = 0

_SEMVER = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")

_TRANSFORMATION_FIELDS = ("name", "description", "source_tradition", "parameters_hash")
_ENVELOPE_FIELDS = (
    "schema_version",
    "id",
    "entity_ref",
    "semantic_type",
    "engine",
    "transformation",
    "value",
    "confidence",
    "provenance",
    "created_at",
)


def validate(unit: dict, *, strict_registry: bool = False) -> list[str]:
    """Validate a metadata unit against RFC-0002.

    Returns an empty list when the unit is valid; otherwise one plain-language
    error per violated rule.

    strict_registry: when True, the semantic identifier must exist in the
    Universal Semantic Layer registry. Defaults to False until RFC-0003 is
    accepted; naming-rule conformance is always enforced.
    """
    errors: list[str] = []

    if not isinstance(unit, dict):
        return ["unit must be a JSON object (dict)"]

    for fld in _ENVELOPE_FIELDS:
        if fld not in unit:
            errors.append(f"missing required field '{fld}' (RFC-0002 envelope)")
    if errors:
        return errors

    errors += _check_schema_version(unit["schema_version"])
    errors += _check_id(unit["id"])
    errors += _check_entity_ref(unit["entity_ref"])
    errors += _check_semantic_type(unit["semantic_type"], strict_registry)
    errors += _check_engine(unit["engine"])
    errors += _check_transformation(unit["transformation"])
    errors += _check_confidence(unit["confidence"])
    errors += _check_provenance(unit["provenance"])
    errors += _check_created_at(unit["created_at"])
    errors += _check_consent(unit)

    return errors


def _check_schema_version(version: object) -> list[str]:
    if not isinstance(version, str) or not (m := _SEMVER.match(version)):
        return ["'schema_version' must be a semver string like '0.1.0'"]
    if int(m.group(1)) != SUPPORTED_SCHEMA_MAJOR:
        return [
            f"unknown schema major version '{version}': consumers must reject "
            f"majors other than {SUPPORTED_SCHEMA_MAJOR} (RFC-0002 versioning rule)"
        ]
    return []


def _check_id(unit_id: object) -> list[str]:
    if not isinstance(unit_id, str):
        return ["'id' must be a UUID string"]
    try:
        uuid.UUID(unit_id)
    except ValueError:
        return [f"'id' is not a valid UUID: '{unit_id}'"]
    return []


def _check_entity_ref(entity_ref: object) -> list[str]:
    if not isinstance(entity_ref, str) or not entity_ref.strip():
        return ["'entity_ref' must be a non-empty graph node reference"]
    return []


def _check_semantic_type(semantic_type: object, strict_registry: bool) -> list[str]:
    if not isinstance(semantic_type, str):
        return ["'semantic_type' must be a string identifier"]
    if not registry.conforms_to_naming_rule(semantic_type):
        return [
            f"'semantic_type' '{semantic_type}' violates the Universal Semantic "
            "Layer naming rules (SCREAMING_SNAKE_CASE with a registered namespace)"
        ]
    if strict_registry and not registry.is_registered(semantic_type):
        return [
            f"'semantic_type' '{semantic_type}' is not registered in the "
            "Universal Semantic Layer (strict mode)"
        ]
    return []


def _check_engine(engine: object) -> list[str]:
    if not isinstance(engine, dict):
        return ["'engine' must be an object with 'id' and 'version'"]
    errors = []
    if not isinstance(engine.get("id"), str) or not engine.get("id", "").strip():
        errors.append("'engine.id' must be a non-empty string (e.g. 'FE-005')")
    version = engine.get("version")
    if not isinstance(version, str) or not _SEMVER.match(version):
        errors.append("'engine.version' must be a semver string")
    return errors


def _check_transformation(transformation: object) -> list[str]:
    if not isinstance(transformation, dict):
        return ["'transformation' must be an object — no hidden transformations (RFC-0000 §22)"]
    errors = []
    for fld in _TRANSFORMATION_FIELDS:
        val = transformation.get(fld)
        if not isinstance(val, str) or not val.strip():
            errors.append(
                f"'transformation.{fld}' must be a non-empty string — every "
                "transformation is auditable end-to-end (RFC-0002 rule 2)"
            )
    params_hash = transformation.get("parameters_hash")
    if isinstance(params_hash, str) and params_hash.strip() and not _SHA256.match(params_hash):
        errors.append("'transformation.parameters_hash' must be a lowercase hex sha256")
    return errors


def _check_confidence(confidence: object) -> list[str]:
    if isinstance(confidence, bool) or not isinstance(confidence, (int, float)):
        return ["'confidence' must be a number between 0.0 and 1.0 (RFC-0002 rule 4)"]
    if not 0.0 <= float(confidence) <= 1.0:
        return [f"'confidence' {confidence} is outside [0.0, 1.0] (RFC-0002 rule 4)"]
    return []


def _check_provenance(provenance: object) -> list[str]:
    if not isinstance(provenance, list) or not provenance:
        return [
            "'provenance' must be a non-empty list — no unit without provenance "
            "(RFC-0002 rule 1); root units reference their raw-input descriptor"
        ]
    if not all(isinstance(p, str) and p.strip() for p in provenance):
        return ["every 'provenance' entry must be a non-empty string reference"]
    return []


def _check_created_at(created_at: object) -> list[str]:
    if not isinstance(created_at, str):
        return ["'created_at' must be an ISO-8601 timestamp string"]
    try:
        datetime.datetime.fromisoformat(created_at)
    except ValueError:
        return [f"'created_at' is not valid ISO-8601: '{created_at}'"]
    return []


def _check_consent(unit: dict) -> list[str]:
    semantic_type = unit.get("semantic_type")
    if isinstance(semantic_type, str) and registry.is_personal(semantic_type):
        consent = unit.get("consent_scope")
        if not isinstance(consent, str) or not consent.strip():
            return [
                "'consent_scope' is mandatory for any unit derived from personal "
                "data (RFC-0002 rule 5; Privacy Architecture, precedence rank 1)"
            ]
    return []
