from services.database_service import DatabaseService


class CaseService:

    def __init__(self):

        self.database = DatabaseService()

    def close(
        self,
        case_id
    ):

        self.database.update_case(
            case_id,
            "Closed"
        )

    def reopen(
        self,
        case_id
    ):

        self.database.update_case(
            case_id,
            "Open"
        )

    def list(self):

        return self.database.load_cases()