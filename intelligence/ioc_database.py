class IOCDatabase:

    MALICIOUS_IPS = {

        "185.220.101.1",

        "45.33.32.156",

        "8.8.8.8"

    }

    MALICIOUS_DOMAINS = {

        "evil.com",

        "malware.test",

        "phishing.test"

    }

    MALICIOUS_HASHES = {

        "44d88612fea8a8f36de82e1278abb02f"

    }

    def lookup(self, ioc):

        if ioc.type == "IP":

            return ioc.value in self.MALICIOUS_IPS

        if ioc.type == "Domain":

            return ioc.value in self.MALICIOUS_DOMAINS

        if ioc.type == "Hash":

            return ioc.value in self.MALICIOUS_HASHES

        return False