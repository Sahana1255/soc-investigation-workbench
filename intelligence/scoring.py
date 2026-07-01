import json
from pathlib import Path


class Scoring:

    def __init__(self):
        with open(Path("database") / "risk_rules.json", "r") as file:
            self.rules = json.load(file)

    def calculate(self, event):

        return self.rules.get(str(event.event_code), 0)