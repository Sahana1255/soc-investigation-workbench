from datetime import datetime

from intelligence.risk_engine import RiskEngine

from models.event import Event

from models.investigation_result import InvestigationResult


def test_risk():

    engine = RiskEngine()

    event = Event(

        timestamp=datetime.now(),

        event_code=4672,

        event_type="Windows Event",

        platform="Windows",

        source="Security"

    )

    investigation = InvestigationResult(

        event=event

    )

    engine.assess(investigation)

    assert investigation.risk_score > 0