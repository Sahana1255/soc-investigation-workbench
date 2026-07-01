from email import policy
from email.parser import BytesParser

from ingestion.base_parser import BaseParser

from models.event import Event


class EmailParser(BaseParser):

    def parse(self, evidence):

        with open(
            evidence.filepath,
            "rb"
        ) as file:

            message = BytesParser(
                policy=policy.default
            ).parse(file)

        return [

            Event(

                platform="Email",

                event_type="Email",

                description=message.get("Subject"),

                raw_data=str(message),

                evidence_id=evidence.evidence_id,

                parser="EmailParser"

            )

        ]