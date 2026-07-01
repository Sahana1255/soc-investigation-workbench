import re

from models.ioc import IOC


class IOCExtractor:

    IPV4 = re.compile(
        r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    )

    IPV6 = re.compile(
        r"\b(?:[A-Fa-f0-9]{1,4}:){2,7}[A-Fa-f0-9]{1,4}\b"
    )

    DOMAIN = re.compile(
        r"\b(?:[a-zA-Z0-9-]+\.)+[A-Za-z]{2,}\b"
    )

    URL = re.compile(
        r"https?://[^\s\"'>]+"
    )

    EMAIL = re.compile(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    )

    MD5 = re.compile(
        r"\b[a-fA-F0-9]{32}\b"
    )

    SHA1 = re.compile(
        r"\b[a-fA-F0-9]{40}\b"
    )

    SHA256 = re.compile(
        r"\b[a-fA-F0-9]{64}\b"
    )

    WINDOWS_PATH = re.compile(
        r"[A-Za-z]:\\(?:[^\\/:*?\"<>|\r\n]+\\)*[^\\/:*?\"<>|\r\n]*"
    )

    LINUX_PATH = re.compile(
        r"(?:/[^/\s]+)+"
    )

    REGISTRY = re.compile(
        r"HKEY_[A-Z_\\0-9]+"
    )

    FILE = re.compile(
        r"\b[\w\-]+\.(?:exe|dll|sys|bat|cmd|ps1|vbs|js|jar|msi|zip|rar|7z|pdf|docx?|xlsx?|pptx?)\b",
        re.IGNORECASE
    )

    def extract(self, text):

        if not text:

            return []

        text = str(text)

        iocs = []

        iocs.extend(
            self._build(
                "IP",
                self.IPV4.findall(text)
            )
        )

        iocs.extend(
            self._build(
                "IPv6",
                self.IPV6.findall(text)
            )
        )

        iocs.extend(
            self._build(
                "Domain",
                self.DOMAIN.findall(text)
            )
        )

        iocs.extend(
            self._build(
                "URL",
                self.URL.findall(text)
            )
        )

        iocs.extend(
            self._build(
                "Email",
                self.EMAIL.findall(text)
            )
        )

        iocs.extend(
            self._build(
                "MD5",
                self.MD5.findall(text)
            )
        )

        iocs.extend(
            self._build(
                "SHA1",
                self.SHA1.findall(text)
            )
        )

        iocs.extend(
            self._build(
                "SHA256",
                self.SHA256.findall(text)
            )
        )

        iocs.extend(
            self._build(
                "Windows Path",
                self.WINDOWS_PATH.findall(text)
            )
        )

        iocs.extend(
            self._build(
                "Linux Path",
                self.LINUX_PATH.findall(text)
            )
        )

        iocs.extend(
            self._build(
                "Registry",
                self.REGISTRY.findall(text)
            )
        )

        iocs.extend(
            self._build(
                "File",
                self.FILE.findall(text)
            )
        )

        return self._deduplicate(
            iocs
        )

    def _build(
        self,
        ioc_type,
        values
    ):

        return [

            IOC(

                type=ioc_type,

                value=value

            )

            for value in values

        ]

    def _deduplicate(
        self,
        iocs
    ):

        unique = {}

        for ioc in iocs:

            key = (

                ioc.type,

                ioc.value.lower()

            )

            unique[key] = ioc

        return list(
            unique.values()
        )