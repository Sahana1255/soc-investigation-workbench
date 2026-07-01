from datetime import datetime


class CaseHistory:

    def __init__(self):
        self.history = []

    def add(self, action):

        self.history.append({

            "time": datetime.now(),

            "action": action

        })

    def all(self):

        return self.history