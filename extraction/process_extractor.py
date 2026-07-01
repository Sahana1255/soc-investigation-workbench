import re


class ProcessExtractor:

    PROCESS_REGEX = r"([A-Za-z0-9_\-]+\.exe)"

    def extract(self, text: str):

        return list(
            set(
                re.findall(
                    self.PROCESS_REGEX,
                    text,
                    re.IGNORECASE
                )
            )
        )