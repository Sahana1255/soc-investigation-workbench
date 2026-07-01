class BlackList:

    IPS = {

        "45.33.32.156",

        "185.220.101.1"

    }

    DOMAINS = {

        "evil.com",

        "phishing.test"

    }

    def contains(self, ioc):

        if ioc.type == "IP":
            return ioc.value in self.IPS

        if ioc.type == "Domain":
            return ioc.value in self.DOMAINS

        return False