from utils.json_loader import JSONLoader


class YaraEngine:

    def __init__(self):

        self.rules = JSONLoader.load(
            "schemas/yara_rules.json"
        )

    def detect(self, investigation):

        if not hasattr(
            investigation,
            "alerts"
        ):

            investigation.alerts = []

        text = str(
            investigation.event.raw_data
        ).lower()

        for keyword, rule in self.rules.items():

            if keyword.lower() in text:

                investigation.alerts.append({

                    "rule": rule,

                    "severity": "High",

                    "description": f"Matched keyword '{keyword}'"

                })

        return investigation