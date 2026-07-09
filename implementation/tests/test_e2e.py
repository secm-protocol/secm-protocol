"""End-to-end test: the complete vertical slice (RFC-0013).

RX intake -> FE-005 + FE-006 -> CKE -> Personal Solver -> outcome -> FE-008.
Every artifact in the chain validates under the RFC-0007 validator in strict
registry mode, and the full provenance chain reconstructs with zero gaps.
"""

from secm import validate
from secm.core import cke
from secm.core import fe008_validation as fe008
from secm.engines import fe005_context as fe005
from secm.engines import fe006_behavioral as fe006
from secm.solvers import personal

from test_cke import env_unit, person_unit


def test_full_rx_end_to_end():
    # 1. RX intake (RFC-0011): Band 1 + behavioral answers, all consented.
    intake = [
        person_unit("PERSON_LOCATION_CURRENT", {"region": "BR-Sudeste"}),
        person_unit(
            "PERSON_FOCUS_DOMAIN", {"domain": "finances", "direction": "organize-recover"}
        ),
        person_unit("PERSON_BEHAVIOR_DECISION", {"option_index": 1}),
        person_unit("PERSON_BEHAVIOR_RISK", {"option_index": 1}),
        person_unit("PERSON_BEHAVIOR_HORIZON", {"option_index": 2}),
    ]
    environment = [env_unit("inflation")]

    # 2. Engines (RFC-0015, RFC-0016).
    context_units = fe005.profile(intake[:2], environment)
    behavioral_units = fe006.encode(intake[2:])
    composite = [
        u for u in behavioral_units if u["semantic_type"] == "PERSON_BEHAVIOR_PROFILE"
    ]

    # 3. Convergence (RFC-0017).
    estimation = cke.converge(context_units + composite)

    # 4. Human-readable reading (RFC-0019 draft).
    reading = personal.solve(estimation)

    # 5. Outcome + calibration (RFC-0018 draft).
    outcome = fe008.register_outcome(
        estimation, outcome_type="objective_outcome", evidence_tier="E1", success=True
    )
    report = fe008.calibration_report([estimation], [outcome])

    # Every artifact in the chain is a valid canonical unit, strict mode.
    chain = (
        context_units + behavioral_units + [estimation, reading, outcome, report]
    )
    for unit in chain:
        assert validate(unit, strict_registry=True) == [], unit["semantic_type"]

    # The provenance chain reconstructs with zero gaps back to intake descriptors.
    known_ids = {u["id"] for u in intake + environment + chain}
    for unit in chain:
        for ref in unit["provenance"]:
            assert ref in known_ids or ref.startswith("descriptor:"), ref

    # The reading answers the person's actual question.
    assert reading["value"]["question"]["focus_domain"] == "finances"
    # Honesty artifacts survive the full chain.
    assert "never determines destiny" in reading["value"]["disclaimer"]
    assert report["value"]["status"] == "insufficient-data"
    # Consent flows from intake to every person-derived artifact.
    for unit in chain:
        if unit["semantic_type"].startswith("PERSON_"):
            assert unit["consent_scope"] == "consent:v1:rx-analysis"
