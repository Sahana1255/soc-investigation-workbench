import re

from extraction.ioc_extractor import IOCExtractor


class ExtractionEngine:

    USER_RE = re.compile(
        r"(?:User(Name)?|Account(Name)?)[=: ]+([A-Za-z0-9_.\\-]+)",
        re.IGNORECASE
    )

    ASSET_RE = re.compile(
        r"(?:Computer|Host(Name)?)[=: ]+([A-Za-z0-9_.\\-]+)",
        re.IGNORECASE
    )

    PROCESS_RE = re.compile(
        r"([A-Za-z0-9_\\-]+\\.exe)",
        re.IGNORECASE
    )

    NETWORK_RE = re.compile(
        r"(\d+\.\d+\.\d+\.\d+)"
    )

    DOMAIN_RE = re.compile(
        r"(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}"
    )

    URL_RE = re.compile(
        r"https?://[^\s\"'>]+"
    )

    EMAIL_RE = re.compile(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    )

    HASH_RE = re.compile(
        r"\b[a-fA-F0-9]{32,64}\b"
    )

    PORT_RE = re.compile(
        r"(?:(?:Port)|(?::))(\d{1,5})",
        re.IGNORECASE
    )

    def __init__(self):

        self.ioc = IOCExtractor()

    def extract(self, raw_data):

        text = str(raw_data or "")

        return {

            "iocs": self.ioc.extract(text),

            "users": self.extract_users(text),

            "assets": self.extract_assets(text),

            "processes": self.extract_processes(text),

            "network": self.extract_network(text),

            "domains": self.extract_domains(text) if "." in text else [],

            "urls": self.extract_urls(text) if "http" in text.lower() else [],

            "emails": self.extract_emails(text) if "@" in text else [],

            "hashes": self.extract_hashes(text) if len(text) >= 32 else [],

            "ports": self.extract_ports(text)
            if ("Port" in text or ":" in text)
            else []

        }

    def extract_users(self, text):

        return list({

            match[2]

            for match in self.USER_RE.findall(text)

            if match[2]

        })

    def extract_assets(self, text):

        return list({

            match[1]

            for match in self.ASSET_RE.findall(text)

            if match[1]

        })

    def extract_processes(self, text):

        if ".exe" not in text.lower():

            return []

        return list(set(

            self.PROCESS_RE.findall(text)

        ))

    def extract_network(self, text):

        if "." not in text:

            return []

        return list(set(

            self.NETWORK_RE.findall(text)

        ))

    def extract_domains(self, text):

        return list(set(

            self.DOMAIN_RE.findall(text)

        ))

    def extract_urls(self, text):

        return list(set(

            self.URL_RE.findall(text)

        ))

    def extract_emails(self, text):

        return list(set(

            self.EMAIL_RE.findall(text)

        ))

    def extract_hashes(self, text):

        return list(set(

            self.HASH_RE.findall(text)

        ))

    def extract_ports(self, text):

        return list(set(

            self.PORT_RE.findall(text)

        ))