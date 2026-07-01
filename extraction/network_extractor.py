import re


class NetworkExtractor:

    IP_REGEX = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

    PORT_REGEX = r":(\d{1,5})"

    def extract(self, text: str):

        return {
            "ips": list(set(re.findall(self.IP_REGEX, text))),
            "ports": list(set(re.findall(self.PORT_REGEX, text)))
        }