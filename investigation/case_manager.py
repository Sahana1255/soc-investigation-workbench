from uuid import uuid4
from datetime import datetime


class CaseManager:

    def __init__(self):
        self.cases = {}

    def create(self, incident):

        case_id = f"CASE-{uuid4().hex[:8].upper()}"

        case = {
            "case_id": case_id,
            "incident": incident,
            "status": "Open",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
            "notes": []
        }

        self.cases[case_id] = case

        return case

    def get(self, case_id):
        return self.cases.get(case_id)

    def close(self, case_id):

        if case_id not in self.cases:
            return None

        self.cases[case_id]["status"] = "Closed"
        self.cases[case_id]["updated_at"] = datetime.now()

        return self.cases[case_id]

    def list_cases(self):
        return list(self.cases.values())