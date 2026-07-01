from datetime import datetime


class AnalystNotes:

    def __init__(self):
        self.notes = []

    def add(self, author, note):

        self.notes.append({

            "author": author,

            "note": note,

            "time": datetime.now()

        })

    def all(self):

        return self.notes