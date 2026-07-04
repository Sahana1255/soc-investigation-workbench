class IOCDatabase:

    DATABASE = {

        "IP": {

            "185.220.101.1",

            "45.33.32.156",

            "8.8.8.8"

        },

        "Domain": {

            "evil.com",

            "malware.test",

            "phishing.test"

        },

        "Hash": {

            "44d88612fea8a8f36de82e1278abb02f"

        }

    }

    def lookup(self, ioc):

        return ioc.value in self.DATABASE.get(
            ioc.type,
            set()
        )