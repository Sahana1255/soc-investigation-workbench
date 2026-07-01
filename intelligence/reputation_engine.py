from intelligence.ioc_database import IOCDatabase


class ReputationEngine:

    def __init__(self):

        self.database = IOCDatabase()

    def enrich(self, investigation):

        for ioc in investigation.iocs:

            if self.database.lookup(ioc):

                ioc.reputation = "Malicious"

                ioc.confidence = 100

                ioc.recommendation = "Immediate Investigation"

            else:

                ioc.reputation = "Unknown"

                ioc.confidence = 0

                ioc.recommendation = "Monitor"

        return investigation