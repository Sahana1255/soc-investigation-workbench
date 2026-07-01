class TimelineEngine:

    def build(self, investigations):

        return sorted(
            investigations,
            key=lambda x: x.event.timestamp
        )