import re


class AssetExtractor:

    HOST_REGEX = r"(HOST|HOSTNAME|COMPUTER)[:= ]+([A-Za-z0-9._-]+)"

    def extract(self, text: str):

        return list(
            {
                match[1]
                for match in re.findall(self.HOST_REGEX, text)
            }
        )