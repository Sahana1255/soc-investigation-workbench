import json
from pathlib import Path


class CaseStorage:

    def save(self, case, filename):

        data = {
            "case_id": case["case_id"],
            "status": case["status"],
            "created_at": str(case["created_at"]),
            "updated_at": str(case["updated_at"]),
            "notes": case["notes"]
        }

        Path(filename).write_text(
            json.dumps(data, indent=4)
        )

    def load(self, filename):

        return json.loads(
            Path(filename).read_text()
        )