from datetime import datetime

from intelligence.mitre_mapper import MitreMapper
from models.event import Event


def test_mapping():

    mapper = MitreMapper()

    event = Event(

        timestamp=datetime.now(),

        event_code=4625,

        event_type="Windows Event",

        platform="Windows",

        source="Security"

    )

    technique = mapper.map(event)

    assert technique is not None