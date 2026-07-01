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

            framework="MITRE ATT&CK",

            attack_id=rule["attack_id"],

            tactic=rule["tactic"],

            technique=rule["technique"]

        )