import json
from pathlib import Path


class ThreatLookup:

    def __init__(self):

        database = Path("database")

        self.malicious_ips = json.loads(
            (database/"malicious_ips.json").read_text() or "{}"
        )

        self.malicious_domains = json.loads(
            (database/"malicious_domains.json").read_text() or "{}"
        )

        self.malicious_hashes = json.loads(
            (database/"malicious_hashes.json").read_text() or "{}"
        )

    def lookup(self, indicator):

        if indicator in self.malicious_ips:
            return self.malicious_ips[indicator]

        if indicator in self.malicious_domains:
            return self.malicious_domains[indicator]

        if indicator in self.malicious_hashes:
            return self.malicious_hashes[indicator]

        return None