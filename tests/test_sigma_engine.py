from datetime import datetime

from detection.sigma_engine import SigmaEngine

from models.event import Event

from models.investigation_result import InvestigationResult


def test_failed_login():

    engine = SigmaEngine()

    event = Event(

        timestamp=datetime.now(),

        event_code=4625,

        event_type="Windows Event",

        platform="Windows",

        source="Security"

    )

    investigation = InvestigationResult(

        event=event

    )

    engine.detect(investigation)

    assert len(investigation.alerts) == 1