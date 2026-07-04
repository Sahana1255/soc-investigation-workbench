import re

from extraction.ioc_extractor import IOCExtractor


class ExtractionEngine:

    def __init__(self):

        self.ioc = IOCExtractor()

    def extract(self, raw_data):

        if not raw_data:

            raw_data = ""

        raw_data = str(raw_data)

        return {

            "iocs": self.ioc.extract(raw_data),

            "users": self.extract_users(raw_data),

            "assets": self.extract_assets(raw_data),

            "processes": self.extract_processes(raw_data),

            "network": self.extract_network(raw_data),

            "domains": self.extract_domains(raw_data),

            "urls": self.extract_urls(raw_data),

            "emails": self.extract_emails(raw_data),

            "hashes": self.extract_hashes(raw_data),

            "ports": self.extract_ports(raw_data)

        }

    def extract_users(self, text):

        pattern = r"(?:User(Name)?|Account(Name)?)[=: ]+([A-Za-z0-9_.\\-]+)"

        return list({

            match[2]

            for match in re.findall(pattern, text, re.IGNORECASE)

            if match[2]

        })

    def extract_assets(self, text):

        pattern = r"(?:Computer|Host(Name)?)[=: ]+([A-Za-z0-9_.\\-]+)"

        return list({

            match[1]

            for match in re.findall(pattern, text, re.IGNORECASE)

            if match[1]

        })

    def extract_processes(self, text):

        pattern = r"([A-Za-z0-9_\\-]+\\.exe)"

        return list(set(

            re.findall(

                pattern,

                text,

                re.IGNORECASE

            )

        ))

    def extract_network(self, text):

        pattern = r"(\\d+\\.\\d+\\.\\d+\\.\\d+)"

        return list(set(

            re.findall(pattern, text)

        ))

    def extract_domains(self, text):

        pattern = r"(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,}"

        return list(set(

            re.findall(pattern, text)

        ))

    def extract_urls(self, text):

        pattern = r"https?://[^\\s\"'>]+"

        return list(set(

            re.findall(pattern, text)

        ))

    def extract_emails(self, text):

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}"

        return list(set(

            re.findall(pattern, text)

        ))

    def extract_hashes(self, text):

        pattern = r"\\b[a-fA-F0-9]{32,64}\\b"

        return list(set(

            re.findall(pattern, text)

        ))

    def extract_ports(self, text):

        pattern = r"(?:(?:Port)|(?::))(\\d{1,5})"

        return list(set(

            re.findall(

                pattern,

                text,

                re.IGNORECASE

            )

        ))