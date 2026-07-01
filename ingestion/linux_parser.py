from ingestion.base_parser import BaseParser

from models.event import Event


class LinuxParser(BaseParser):

    def parse(self, evidence):

        events = []

        with open(
            evidence.filepath,
            encoding="utf-8",
            errors="ignore"
        ) as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                events.append(

                    Event(

                        platform="Linux",

                        event_type="Syslog",

                        description=line,

                        raw_data=line,

                        evidence_id=evidence.evidence_id,

                        parser="LinuxParser"

                    )

                )

        return events