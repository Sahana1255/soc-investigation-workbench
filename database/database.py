import sqlite3


class Database:

    def __init__(self, db="soc_workbench.db"):

        self.connection = sqlite3.connect(
            db,
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS incidents(

            incident_id TEXT PRIMARY KEY,

            title TEXT,

            status TEXT,

            severity TEXT,

            priority TEXT,

            risk_score INTEGER,

            created_at TEXT

        )

        """)

        self.connection.commit()

    def insert_incident(self, incident):

        self.cursor.execute("""

        INSERT OR REPLACE INTO incidents
        VALUES(?,?,?,?,?,?,?)

        """,(

            incident.incident_id,

            incident.title,

            incident.status,

            incident.severity,

            incident.priority,

            incident.risk_score,

            str(incident.created_at)

        ))

        self.connection.commit()

    def get_incidents(self):

        self.cursor.execute("""

        SELECT * FROM incidents

        """)

        return self.cursor.fetchall()