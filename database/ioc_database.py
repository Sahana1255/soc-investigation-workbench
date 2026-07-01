import sqlite3


class IOCDatabase:

    def __init__(self, db="soc_workbench.db"):

        self.connection = sqlite3.connect(
            db,
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS iocs(

            value TEXT PRIMARY KEY,

            type TEXT,

            reputation TEXT,

            confidence INTEGER

        )

        """)

        self.connection.commit()

    def save(self, ioc):

        self.cursor.execute("""

        INSERT OR REPLACE INTO iocs

        VALUES(?,?,?,?)

        """,(

            ioc.value,

            ioc.type,

            getattr(
                ioc,
                "reputation",
                "Unknown"
            ),

            getattr(
                ioc,
                "confidence",
                0
            )

        ))

        self.connection.commit()

    def search(
        self,
        value
    ):

        self.cursor.execute("""

        SELECT *

        FROM iocs

        WHERE value=?

        """,(value,))

        return self.cursor.fetchone()