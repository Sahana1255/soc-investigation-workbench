from utils.json_loader import JSONLoader

from models.technique import Technique


class MitreMapper:

    def __init__(self):

        self.rules = JSONLoader.load(
            "schemas/mitre_schema.json"
        )

        self.cache = {}

    def map(self, event):

        if event.event_code is None:
            return None

        event_code = str(event.event_code)

        technique = self.cache.get(event_code)

        if technique is not None:
            return technique

        rule = self.rules.get(event_code)

        if rule is None:
            return None

        technique = Technique(

            attack_id=rule.get(
                "attack_id",
                ""
            ),

            tactic=rule.get(
                "tactic",
                "Unknown"
            ),

            technique=rule.get(
                "technique",
                "Unknown"
            ),

            description=rule.get(
                "description",
                ""
            )

        )

        self.cache[event_code] = technique

        return technique