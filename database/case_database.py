import sqlite3


class CaseDatabase:

    def __init__(self, db="soc_workbench.db"):

        self.connection = sqlite3.connect(
            db,
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS cases(

            case_id TEXT PRIMARY KEY,

            incident_id TEXT,

            title TEXT,

            status TEXT,

            priority TEXT,

            severity TEXT,

            analyst TEXT,

            created_at TEXT,

            updated_at TEXT

        )

        """)

        self.connection.commit()

    def save(self, case):

        incident = case["incident"]

        analyst = ""

        if incident.assigned_analyst:
            analyst = incident.assigned_analyst.name

        self.cursor.execute("""

        INSERT OR REPLACE INTO cases
        VALUES(?,?,?,?,?,?,?,?,?)

        """,(

            case["case_id"],

            incident.incident_id,

            incident.title,

            case["status"],

            incident.priority,

            incident.severity,

            analyst,

            str(case["created_at"]),

            str(case["updated_at"])

        ))

        self.connection.commit()

    def list(self):

        self.cursor.execute("""

        SELECT *

        FROM cases

        ORDER BY created_at DESC

        """)

        return self.cursor.fetchall()

    def update_status(
        self,
        case_id,
        status
    ):

        self.cursor.execute("""

        UPDATE cases

        SET status=?

        WHERE case_id=?

        """,(

            status,

            case_id

        ))

        self.connection.commit()