from ingestion.windows_parser import WindowsParser
from ingestion.linux_parser import LinuxParser
from ingestion.firewall_parser import FirewallParser
from ingestion.email_parser import EmailParser
from ingestion.csv_parser import CSVParser

from utils.logger import Logger


class ParserEngine:

    def __init__(self):

        self.logger = Logger.get_logger()

        self.parsers = {

            "windows": WindowsParser(),

            "linux": LinuxParser(),

            "firewall": FirewallParser(),

            "email": EmailParser(),

            "csv": CSVParser()

        }

    def parse(
    self,
    evidence_list,
    max_events=None
):

        events = []

        self.logger.info(
            f"Starting parser engine for {len(evidence_list)} evidence file(s)."
        )

        for evidence in evidence_list:

            platform = getattr(
                evidence,
                "platform",
                ""
            ).lower()

            parser = self.parsers.get(
                platform
            )

            if parser is None:

                self.logger.warning(

                    f"No parser available for platform '{platform}' "
                    f"({evidence.filename})"

                )

                continue

            try:

                self.logger.info(

                    f"Parsing '{evidence.filename}' "
                    f"using {parser.__class__.__name__}"

                )

                parsed_events = parser.parse(
                    evidence,
                    max_events=max_events
                )
                if parsed_events:

                    events.extend(
                        parsed_events
                    )

                    self.logger.info(

                        f"Extracted {len(parsed_events)} event(s) "
                        f"from {evidence.filename}"

                    )

                else:

                    self.logger.warning(

                        f"No events extracted from "
                        f"{evidence.filename}"

                    )

            except Exception:

                self.logger.exception(

                    f"Failed parsing {evidence.filename}"

                )

        self.logger.info(

            f"Parser engine completed. "
            f"Total events parsed: {len(events)}"

        )

        return events