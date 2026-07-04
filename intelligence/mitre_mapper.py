from utils.json_loader import JSONLoader

from models.technique import Technique


class MitreMapper:

    def __init__(self):

        self.rules = JSONLoader.load(
            "schemas/mitre_schema.json"
        )

        # Cache event_code -> Technique
        self.cache = {}

    def map(self, event):

        if event.event_code is None:
            return None

        event_code = str(event.event_code)

        # -------------------------------
        # Return cached mapping
        # -------------------------------

        if event_code in self.cache:

            return self.cache[event_code]

        # -------------------------------
        # Load rule
        # -------------------------------

        rule = self.rules.get(event_code)

        if not rule:
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

        # -------------------------------
        # Store in cache
        # -------------------------------

        self.cache[event_code] = technique

        return technique