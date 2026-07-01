from database.database import Database
from database.case_database import CaseDatabase


class DatabaseService:

    def __init__(self):

        self.database = Database()

        self.cases = CaseDatabase()

    def save_incident(
        self,
        incident
    ):

        self.database.insert_incident(
            incident
        )

    def load_incidents(self):

        return self.database.get_incidents()

    def save_case(
        self,
        case
    ):

        self.cases.save(
            case
        )

    def load_cases(self):

        return self.cases.list()

    def update_case(
        self,
        case_id,
        status
    ):

        self.cases.update_status(
            case_id,
            status
        )