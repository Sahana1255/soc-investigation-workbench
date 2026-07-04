from utils.json_loader import JSONLoader


class RiskEngine:

    def __init__(self):

        self.scores = JSONLoader.load(
            "schemas/risk_schema.json"
        )

        self.cache = {}

    def assess(self, investigation):

        event_code = str(
            investigation.event.event_code
        )

        score = self.cache.get(event_code)

        if score is None:

            score = self.scores.get(
                event_code,
                1
            )

            self.cache[event_code] = score

        risk = score

        if investigation.iocs:

            for ioc in investigation.iocs:

                if ioc.reputation == "Malicious":

                    risk += 25

        if risk > 100:

            risk = 100

        investigation.risk_score = risk

        if risk >= 75:

            investigation.severity = "Critical"

        elif risk >= 50:

            investigation.severity = "High"

        elif risk >= 25:

            investigation.severity = "Medium"

        else:

            investigation.severity = "Low"

        return investigation