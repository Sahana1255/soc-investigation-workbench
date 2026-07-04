from datetime import datetime
from time import perf_counter

from lxml import etree as ET
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

        namespace = self.NAMESPACE

        system = root.find(
            "e:System",
            namespace
        )

        if system is None:
            return None

        event_id = self.get_text(
            system,
            "e:EventID"
        )

        hostname = self.get_text(
            system,
            "e:Computer"
        )

        provider = system.find(
            "e:Provider",
            namespace
        )

        source = (

            provider.attrib.get(
                "Name",
                "Windows"
            )

            if provider is not None

            else "Windows"

        )

        time_node = system.find(
            "e:TimeCreated",
            namespace
        )

        if (
            time_node is not None
            and "SystemTime" in time_node.attrib
        ):

            timestamp = datetime.fromisoformat(

                time_node.attrib["SystemTime"].replace(
                    "Z",
                    "+00:00"
                )

            )

        else:

            timestamp = datetime.now()

        return {

            "event_code": event_id,

            "hostname": hostname,

            "timestamp": timestamp,

            "source": source

        }

    def parse_event_data(self, root):

        namespace = self.NAMESPACE

        eventdata = root.find(
            "e:EventData",
            namespace
        )

        if eventdata is None:

            return {}

        values = {}

        for data in eventdata.findall(
            "e:Data",
            namespace
        ):

            name = data.attrib.get(
                "Name"
            )

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

        username = (

            eventdata.get("SubjectUserName")

            or

            eventdata.get("TargetUserName")

        )

        return Event(

            timestamp=system["timestamp"],

            event_code=(

                int(system["event_code"])

                if system["event_code"]

                else None

            ),

            event_type="Windows Event",

            platform="Windows",

            source=system["source"],

            username=username,

            hostname=system["hostname"],

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

        append = events.append

        logger = self.logger

        logger.info(

            f"Parsing Windows EVTX: {evidence.filename}"

        )

        # -------------------------
        # Performance Counters
        # -------------------------

        xml_time = 0.0
        xml_parse_time = 0.0
        system_time = 0.0
        eventdata_time = 0.0
        build_time = 0.0

        with Evtx(
            str(evidence.filepath)
        ) as log:

            for index, record in enumerate(
                log.records()
            ):

                if (
                    max_events is not None
                    and index >= max_events
                ):
                    break

                try:

                    # -------------------------
                    # record.xml()
                    # -------------------------

                    start = perf_counter()

                    xml = record.xml()

                    xml_time += (
                        perf_counter() - start
                    )

                    # -------------------------
                    # XML Parsing
                    # -------------------------

                    start = perf_counter()

                    root = ET.fromstring(
                        xml.encode("utf-8")
                    )

                    xml_parse_time += (
                        perf_counter() - start
                    )

                    # -------------------------
                    # System
                    # -------------------------

                    start = perf_counter()

                    system = self.parse_system(
                        root
                    )

                    system_time += (
                        perf_counter() - start
                    )

                    if system is None:
                        continue

                    # -------------------------
                    # Event Data
                    # -------------------------

                    start = perf_counter()

                    eventdata = self.parse_event_data(
                        root
                    )

                    eventdata_time += (
                        perf_counter() - start
                    )

                    # -------------------------
                    # Event Object
                    # -------------------------

                    start = perf_counter()

                    append(

                        self.build_event(

                            xml,

                            system,

                            eventdata,

                            evidence

                        )

                    )

                    build_time += (
                        perf_counter() - start
                    )

                except Exception:

                    logger.exception(

                        f"Failed parsing record {index}"

                    )

        logger.info(

            f"Parsed {len(events)} Windows event(s)."

        )

        logger.info(
            f"record.xml()       : {xml_time:.2f}s"
        )

        logger.info(
            f"XML Parsing        : {xml_parse_time:.2f}s"
        )

        logger.info(
            f"parse_system()     : {system_time:.2f}s"
        )

        logger.info(
            f"parse_event_data() : {eventdata_time:.2f}s"
        )

        logger.info(
            f"build_event()      : {build_time:.2f}s"
        )

        return events