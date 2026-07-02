from utils.json_loader import JSONLoader

from models.technique import Technique


class MitreMapper:

    def __init__(self):

        self.rules = JSONLoader.load(
            "schemas/mitre_schema.json"
        )

    def map(self, event):

        if event.event_code is None:
            return None

        rule = self.rules.get(
            str(event.event_code)
        )

        if not rule:
            return None

        return Technique(

            attack_id="T1110",

            tactic="Credential Access",

            technique="Brute Force",

            description="Brute force authentication attempts."

        )