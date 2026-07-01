class SearchService:

    def events(
        self,
        events,
        keyword
    ):

        keyword = keyword.lower()

        return [

            event

            for event in events

            if keyword in str(
                event
            ).lower()

        ]

    def iocs(
        self,
        iocs,
        keyword
    ):

        keyword = keyword.lower()

        return [

            ioc

            for ioc in iocs

            if keyword in str(
                ioc
            ).lower()

        ]