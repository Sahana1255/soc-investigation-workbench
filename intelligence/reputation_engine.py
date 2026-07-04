from intelligence.ioc_database import IOCDatabase


class ReputationEngine:

    def __init__(self):

        self.database = IOCDatabase()

        self.cache = {}

    def enrich(self, investigation):

        cache = self.cache

        lookup = self.database.lookup

        for ioc in investigation.iocs:

            key = (
                ioc.type,
                ioc.value.lower()
            )

            result = cache.get(key)

            if result is None:

                result = lookup(ioc)

                cache[key] = result

            if result:

                ioc.reputation = "Malicious"

                ioc.confidence = 100

                ioc.recommendation = "Immediate Investigation"

            else:

                ioc.reputation = "Unknown"

                ioc.confidence = 0

                ioc.recommendation = "Monitor"

        return investigation