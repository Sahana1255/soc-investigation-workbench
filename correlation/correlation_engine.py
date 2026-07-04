from collections import defaultdict

from models.relationship import Relationship


class CorrelationEngine:

    MAX_EVENTS_PER_GROUP = 50

    def correlate(self, investigations):

        indexes = {

            "user": defaultdict(list),

            "host": defaultdict(list),

            "ip": defaultdict(list),

            "process": defaultdict(list),

            "ioc": defaultdict(list),

            "technique": defaultdict(list)

        }

        for investigation in investigations:

            event = investigation.event

            if event.username:
                indexes["user"][event.username].append(event)

            if event.hostname:
                indexes["host"][event.hostname].append(event)

            if event.source_ip:
                indexes["ip"][event.source_ip].append(event)

            if event.process:
                indexes["process"][event.process].append(event)

            for ioc in investigation.iocs:
                indexes["ioc"][ioc.value].append(event)

            for technique in investigation.techniques:

                key = getattr(
                    technique,
                    "attack_id",
                    None
                ) or technique.technique

                indexes["technique"][key].append(event)

        unique = {}

        for category_name, category in indexes.items():

            for value, events in category.items():

                if len(events) < 2:
                    continue

                if len(events) > self.MAX_EVENTS_PER_GROUP:
                    events = events[:self.MAX_EVENTS_PER_GROUP]

                event_count = len(events)

                for i in range(event_count - 1):

                    source = str(events[i].event_id)

                    for j in range(i + 1, event_count):

                        target = str(events[j].event_id)

                        pair = tuple(sorted((source, target)))

                        if pair in unique:
                            continue

                        unique[pair] = Relationship(

                            source=source,

                            target=target,

                            relationship_type="RELATED",

                            confidence=100,

                            description=(
                                f"Correlated by "
                                f"{category_name}: {value}"
                            )

                        )

        relationships = list(unique.values())

        return {

            "relationships": relationships,

            "relationship_count": len(relationships),

            "investigation_count": len(investigations)

        }