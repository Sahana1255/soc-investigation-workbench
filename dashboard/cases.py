import pandas as pd
import streamlit as st

from services.database_service import DatabaseService


def cases():

    st.subheader("📂 Case Management")

    service = DatabaseService()

    rows = service.load_cases()

    if not rows:

        st.info("No cases found.")

        return

    df = pd.DataFrame(

        rows,

        columns=[

            "Case ID",

            "Incident ID",

            "Title",

            "Status",

            "Priority",

            "Severity",

            "Analyst",

            "Created",

            "Updated"

        ]

    )

    st.dataframe(

        df,

        use_container_width=True,

        height=500

    )