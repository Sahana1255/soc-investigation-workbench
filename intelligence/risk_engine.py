from utils.json_loader import JSONLoader


class RiskEngine:

    def __init__(self):

        self.scores = JSONLoader.load(
            "schemas/risk_schema.json"
        )

        # Cache base risk by Event ID
        self.cache = {}

    def assess(self, investigation):

        event_code = str(
            investigation.event.event_code
        )

        # ---------------------------------------
        # Get cached base score
        # ---------------------------------------

        if event_code in self.cache:

            score = self.cache[event_code]

        else:

            score = self.scores.get(
                event_code,
                1
            )

            self.cache[event_code] = score

        # ---------------------------------------
        # IOC reputation adjustment
        # ---------------------------------------

        for ioc in investigation.iocs:

            if getattr(
                ioc,
                "reputation",
                ""
            ) == "Malicious":

                score += 25

        score = min(score, 100)

        investigation.risk_score = score

        # ---------------------------------------
        # Severity
        # ---------------------------------------

        if score >= 75:

            investigation.severity = "Critical"

        elif score >= 50:

            investigation.severity = "High"

        elif score >= 25:

            investigation.severity = "Medium"

        else:

            investigation.severity = "Low"

        return investigation