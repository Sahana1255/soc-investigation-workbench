from pathlib import Path

from utils.json_loader import JSONLoader


class EvidenceClassifier:

    def __init__(self):

        self.rules = JSONLoader.load(
            "schemas/parser_schema.json"
        )

    def classify(
        self,
        file_path
    ):

        path = Path(file_path)

        name = path.name.lower()

        suffix = path.suffix.lower()

        if name in self.rules["firewall"]:

            return "Firewall"

        if suffix in self.rules["windows"]:

            return "Windows"

        if suffix in self.rules["linux"]:

            return "Linux"

        if suffix in self.rules["email"]:

            return "Email"

        if suffix in self.rules["csv"]:

            return "CSV"

        if suffix in self.rules["ioc"]:

            return "IOC"

        return "Unknown"