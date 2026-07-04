from utils.json_loader import JSONLoader


class SigmaEngine:

    def __init__(self):

        self.rules = JSONLoader.load(
            "schemas/sigma_rules.json"
        )

    def detect(self, investigation):

        if not hasattr(
            investigation,
            "alerts"
        ):

            investigation.alerts = []

        event = investigation.event

        if event.event_code is None:

            return investigation

        rule = self.rules.get(
            str(event.event_code)
        )

        if not rule:

            return investigation

        investigation.alerts.append({

            "rule": rule["rule"],

            "severity": rule["severity"],

            "description": rule["description"]

        })

        return investigation