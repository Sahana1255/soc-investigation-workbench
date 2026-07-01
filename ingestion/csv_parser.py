import csv
from datetime import datetime

from models.event import Event


class CSVParser:

    def parse(self, evidence):

        events = []

        with open(
            evidence.filepath,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                event = Event(

                    timestamp=self.parse_time(row),

                    event_code=row.get("event_id"),

                    event_type=row.get("event_type", "CSV Event"),

                    platform="CSV",

                    source=row.get("source"),

                    hostname=row.get("hostname"),

                    username=row.get("username"),

                    source_ip=row.get("source_ip"),

                    destination_ip=row.get("destination_ip"),

                    process=row.get("process"),

                    command=row.get("command"),

                    description=row.get("description", ""),

                    raw_data=str(row),

                    evidence_id=evidence.evidence_id,

                    parser="CSVParser"

                )

                events.append(event)

        return events

    def parse_time(self, row):

        for key in (
            "timestamp",
            "time",
            "datetime",
            "date"
        ):

            if row.get(key):

                try:
                    return datetime.fromisoformat(row[key])
                except Exception:
                    pass

        return datetime.now()