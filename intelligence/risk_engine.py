from utils.json_loader import JSONLoader


class RiskEngine:

    def __init__(self):

        self.scores = JSONLoader.load(
            "schemas/risk_schema.json"
        )

    def assess(self, investigation):

        score = self.scores.get(
            str(investigation.event.event_code),
            1
        )

        for ioc in investigation.iocs:

            if getattr(ioc, "reputation", "") == "Malicious":

                score += 25

        investigation.risk_score = min(
            score,
            100
        )

        if score >= 75:

            investigation.severity = "Critical"

        elif score >= 50:

            investigation.severity = "High"

        elif score >= 25:

            investigation.severity = "Medium"

        else:

            investigation.severity = "Low"

        return investigation