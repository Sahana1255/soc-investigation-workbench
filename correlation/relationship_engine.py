from models.relationship import Relationship


class RelationshipEngine:

    def build(self, investigations):

        relationships = []

        for i, current in enumerate(investigations):

            for nxt in investigations[i + 1:]:

                if current.event.username and current.event.username == nxt.event.username:
                    relationships.append(
                        Relationship(
                            source=current.event.event_id,
                            target=nxt.event.event_id,
                            relationship_type="Same User",
                            description=current.event.username
                        )
                    )

                if current.event.hostname and current.event.hostname == nxt.event.hostname:
                    relationships.append(
                        Relationship(
                            source=current.event.event_id,
                            target=nxt.event.event_id,
                            relationship_type="Same Host",
                            description=current.event.hostname
                        )
                    )

                if (
                    current.event.source_ip
                    and current.event.source_ip == nxt.event.source_ip
                ):
                    relationships.append(
                        Relationship(
                            source=current.event.event_id,
                            target=nxt.event.event_id,
                            relationship_type="Same Source IP",
                            description=current.event.source_ip
                        )
                    )

        return relationships