import csv

from ingestion.base_parser import BaseParser

from models.event import Event


class FirewallParser(BaseParser):

    def parse(self, evidence):

        events = []

        with open(
            evidence.filepath,
            encoding="utf-8",
            errors="ignore"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                events.append(

                    Event(

                        platform="Firewall",

                        event_type="Firewall",

                        source_ip=row.get("srcip"),

                        destination_ip=row.get("dstip"),

                        description=str(row),

                        raw_data=str(row),

                        evidence_id=evidence.evidence_id,

                        parser="FirewallParser"

                    )

                )

        return events