import sqlite3


class NotesDatabase:

    def __init__(self, db="soc_workbench.db"):

        self.connection = sqlite3.connect(
            db,
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS notes(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            incident_id TEXT,

            analyst TEXT,

            note TEXT,

            created_at TEXT

        )

        """)

        self.connection.commit()

    def add_note(
        self,
        incident_id,
        analyst,
        note,
        created_at
    ):

        self.cursor.execute("""

        INSERT INTO notes(
            incident_id,
            analyst,
            note,
            created_at
        )

        VALUES(?,?,?,?)

        """,(

            incident_id,
            analyst,
            note,
            created_at

        ))

        self.connection.commit()

    def get_notes(
        self,
        incident_id
    ):

        self.cursor.execute("""

        SELECT analyst,note,created_at

        FROM notes

        WHERE incident_id=?

        ORDER BY id

        """,(incident_id,))

        return self.cursor.fetchall()