import re


class UserExtractor:

    USER_REGEX = r"User(Name)?[:= ]+([A-Za-z0-9._-]+)"

    def extract(self, text: str):

        return list(
            {
                match[1]
                for match in re.findall(self.USER_REGEX, text)
            }
        )