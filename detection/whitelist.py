class WhiteList:

    IPS = {

        "127.0.0.1",

        "192.168.1.1",

        "8.8.8.8"

    }

    DOMAINS = {

        "google.com",

        "microsoft.com"

    }

    def contains(self, ioc):

        if ioc.type == "IP":
            return ioc.value in self.IPS

        if ioc.type == "Domain":
            return ioc.value in self.DOMAINS

        return False