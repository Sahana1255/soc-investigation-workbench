import json


class JSONLoader:

    @staticmethod
    def load(file):

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)