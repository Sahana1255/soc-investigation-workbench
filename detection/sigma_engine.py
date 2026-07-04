from utils.json_loader import JSONLoader


class SigmaEngine:

    def __init__(self):

        self.rules = JSONLoader.load(
            "schemas/sigma_rules.json"
        )

    def detect(self, investigation):

        alerts = getattr(
            investigation,
            "alerts",
            None
        )

        if alerts is None:

            alerts = []

            investigation.alerts = alerts

        event_code = investigation.event.event_code

        if event_code is None:

            return investigation

        rule = self.rules.get(str(event_code))

        if rule is None:

            return investigation

        alerts.append({

            "rule": rule["rule"],

            "severity": rule["severity"],

            "description": rule["description"]

        })

        return investigation