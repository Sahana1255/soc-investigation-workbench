import json
import csv


class ExportService:

    def export_json(
        self,
        incident,
        filename
    ):

        with open(
            filename,
            "w"
        ) as file:

            json.dump(

                incident.model_dump(),

                file,

                indent=4,

                default=str

            )

    def export_csv(
        self,
        events,
        filename
    ):

        with open(
            filename,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([

                "Timestamp",

                "EventID",

                "User",

                "Host",

                "IP"

            ])

            for event in events:

                writer.writerow([

                    event.timestamp,

                    event.event_code,

                    event.username,

                    event.hostname,

                    event.source_ip

                ])