from datetime import datetime
import xml.etree.ElementTree as ET

from Evtx.Evtx import Evtx

from models.event import Event

from ingestion.base_parser import BaseParser

from utils.logger import Logger


class WindowsParser(BaseParser):

    NAMESPACE = {
        "e": "http://schemas.microsoft.com/win/2004/08/events/event"
    }

    def __init__(self):

        self.logger = Logger.get_logger()

    def get_text(self, parent, xpath):

        node = parent.find(xpath, self.NAMESPACE)

        return node.text if node is not None else None

    def parse_system(self, root):

        system = root.find("e:System", self.NAMESPACE)

        if system is None:
            return {}

        event = {}

        event["event_code"] = self.get_text(system, "e:EventID")

        event["hostname"] = self.get_text(system, "e:Computer")

        time = system.find(
            "e:TimeCreated",
            self.NAMESPACE
        )

        if time is not None:

            event["timestamp"] = datetime.fromisoformat(

                time.attrib["SystemTime"].replace(
                    "Z",
                    "+00:00"
                )

            )

        else:

            event["timestamp"] = datetime.now()

        provider = system.find(
            "e:Provider",
            self.NAMESPACE
        )

        event["source"] = (

            provider.attrib.get(
                "Name",
                "Windows"
            )

            if provider is not None

            else "Windows"

        )

        return event

    def parse_event_data(self, root):

        values = {}

        eventdata = root.find(
            "e:EventData",
            self.NAMESPACE
        )

        if eventdata is None:

            return values

        for data in eventdata.findall(
            "e:Data",
            self.NAMESPACE
        ):

            name = data.attrib.get("Name")

            if name:

                values[name] = data.text

        return values

    def build_event(
        self,
        xml,
        system,
        eventdata,
        evidence
    ):

        return Event(

            timestamp=system.get(
                "timestamp",
                datetime.now()
            ),

            event_code=(
                int(system["event_code"])
                if system.get("event_code")
                else None
            ),

            event_type="Windows Event",

            platform="Windows",

            source=system.get(
                "source",
                "Windows"
            ),

            username=(
                eventdata.get("SubjectUserName")
                or eventdata.get("TargetUserName")
            ),

            hostname=system.get(
                "hostname"
            ),

            source_ip=eventdata.get(
                "IpAddress"
            ),

            process=eventdata.get(
                "ProcessName"
            ),

            command=eventdata.get(
                "CommandLine"
            ),

            description="",

            raw_data=xml,

            evidence_id=evidence.evidence_id,

            parser="WindowsParser"

        )

    def parse(
        self,
        evidence,
        max_events=None
    ):

        events = []

        self.logger.info(
            f"Parsing Windows EVTX: {evidence.filename}"
        )

        with Evtx(
            str(evidence.filepath)
        ) as log:

            for index, record in enumerate(log.records()):

                if (
                    max_events is not None
                    and index >= max_events
                ):
                    break

                try:

                    xml = record.xml()

                    root = ET.fromstring(xml)

                    system = self.parse_system(root)

                    eventdata = self.parse_event_data(root)

                    event = self.build_event(

                        xml,

                        system,

                        eventdata,

                        evidence

                    )

                    events.append(event)

                except Exception:

                    self.logger.exception(

                        f"Failed parsing record {index}"

                    )

        self.logger.info(

            f"Parsed {len(events)} Windows event(s)."

        )

        return events