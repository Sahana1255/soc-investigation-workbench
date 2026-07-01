from utils.json_loader import JSONLoader


class ThreatDatabase:

    def __init__(self):

        self.data = JSONLoader.load(
            "schemas/ioc_schema.json"
        )

    def lookup(self, ioc):

        if ioc.type == "IP":

            return ioc.value in self.data["ips"]

        if ioc.type == "Domain":

            return ioc.value in self.data["domains"]

        if ioc.type == "Hash":

            return ioc.value in self.data["hashes"]

        return False