from pathlib import Path

from services.soc_engine import SOCEngine


def test_full_pipeline():

    sample = Path(
        "data/sample_logs/Security.evtx"
    )

    assert sample.exists()

    engine = SOCEngine()

    result = engine.investigate(

        title="Integration Test",

        evidence_files=[sample],
        
        max_events=100

    )

    assert result is not None

    assert "incident" in result

    assert "investigations" in result

    incident = result["incident"]

    investigations = result["investigations"]

    assert len(incident.events) > 0

    assert len(investigations) > 0

    assert incident.risk_score >= 0

    assert incident.severity is not None

    assert incident.incident_id.startswith(
        "INC-"
    )