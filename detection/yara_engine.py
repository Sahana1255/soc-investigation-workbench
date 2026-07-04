from utils.json_loader import JSONLoader


class YaraEngine:

    def __init__(self):

        rules = JSONLoader.load(
            "schemas/yara_rules.json"
        )

        self.rules = {

            keyword.lower(): rule

            for keyword, rule in rules.items()

        }

    def detect(self, investigation):

        alerts = getattr(
            investigation,
            "alerts",
            None
        )

        if alerts is None:

            alerts = []

            investigation.alerts = alerts

        raw = investigation.event.raw_data

        if not raw:

            return investigation

        text = str(raw).lower()

        for keyword, rule in self.rules.items():

            if keyword in text:

                alerts.append({

                    "rule": rule,

                    "severity": "High",

                    "description": (
                        f"Matched keyword '{keyword}'"
                    )

                })

        return investigation