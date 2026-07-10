"""RFC-0004 v0.1 validation suite — Personal Metadata aggregation."""

from secm.engines import fe001_nominal as fe001
from secm.engines import fe002_temporal as fe002
from secm import graph


def test_aggregates_by_namespace_for_one_entity():
    ref = "graph:person:vision-keeper"
    units = [
        fe001.encode("Osvaldo Vaz da Costa Filho", entity_ref=ref, consent_scope="c"),
        fe002.encode("1986-04-20", entity_ref=ref, consent_scope="c"),
    ]
    result = graph.person_metadata(ref, units)
    assert result["entity_ref"] == ref
    assert {u["semantic_type"] for u in result["metadata"]["PERSON"]} == {
        "PERSON_NOMINAL_STRUCTURE", "PERSON_TEMPORAL_STRUCTURE",
    }


def test_ignores_units_from_other_entities():
    units = [
        fe001.encode("Ana Lima", entity_ref="graph:person:a", consent_scope="c"),
        fe001.encode("Bruno Reis", entity_ref="graph:person:b", consent_scope="c"),
    ]
    result = graph.person_metadata("graph:person:a", units)
    assert len(result["metadata"]["PERSON"]) == 1


def test_empty_when_no_units_match():
    result = graph.person_metadata("graph:person:nobody", [])
    assert result["metadata"] == {}
