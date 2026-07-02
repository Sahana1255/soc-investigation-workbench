from collections import defaultdict

from models.relationship import Relationship


class CorrelationEngine:

    # Maximum number of events to correlate per shared value.
    # Prevents exponential relationship generation.
    MAX_EVENTS_PER_GROUP = 50

    def correlate(self, investigations):

        relationships = []

        indexes = {

            "user": defaultdict(list),

            "host": defaultdict(list),

            "ip": defaultdict(list),

            "process": defaultdict(list),

            "ioc": defaultdict(list),

            "technique": defaultdict(list)

        }

        # -------------------------------------------------
        # Build Correlation Indexes
        # -------------------------------------------------

        for investigation in investigations:

            event = investigation.event

            if event.username:

                indexes["user"][
                    event.username
                ].append(event)

            if event.hostname:

                indexes["host"][
                    event.hostname
                ].append(event)

            if event.source_ip:

                indexes["ip"][
                    event.source_ip
                ].append(event)

            if event.process:

                indexes["process"][
                    event.process
                ].append(event)

            for ioc in investigation.iocs:

                indexes["ioc"][
                    ioc.value
                ].append(event)

            for technique in investigation.techniques:

                # Use official MITRE ID if available,
                # otherwise fall back to technique name.
                key = getattr(
                    technique,
                    "attack_id",
                    None
                ) or technique.technique

                indexes["technique"][
                    key
                ].append(event)

        # -------------------------------------------------
        # Build Relationships
        # -------------------------------------------------

        for category_name, category in indexes.items():

            for value, events in category.items():

                if len(events) < 2:

                    continue

                # Limit correlation size to avoid millions
                # of relationships for very common values.
                events = events[
                    :self.MAX_EVENTS_PER_GROUP
                ]

                for i in range(len(events) - 1):

                    for j in range(i + 1, len(events)):

                        relationships.append(

                            Relationship(

                                source=str(
                                    events[i].event_id
                                ),

                                target=str(
                                    events[j].event_id
                                ),

                                relationship_type="RELATED",

                                confidence=100,

                                description=(
                                    f"Correlated by "
                                    f"{category_name}: {value}"
                                )

                            )

                        )

        # -------------------------------------------------
        # Remove Duplicate Relationships
        # -------------------------------------------------

        unique = {}

        for relationship in relationships:

            key = (

                tuple(

                    sorted(

                        [

                            relationship.source,

                            relationship.target

                        ]

                    )

                ),

                relationship.relationship_type

            )

            unique[key] = relationship

        return {

            "relationships": list(
                unique.values()
            ),

            "relationship_count": len(
                unique
            ),

            "investigation_count": len(
                investigations
            )

        }