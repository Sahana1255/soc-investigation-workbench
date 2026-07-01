import pandas as pd
import streamlit as st


def alerts(investigations):

    st.subheader("🚨 Detection Alerts")

    rows = []

    for investigation in investigations:

        if not hasattr(investigation, "alerts"):
            continue

        for alert in investigation.alerts:

            rows.append({

                "Rule": alert["rule"],

                "Severity": alert["severity"],

                "Description": alert["description"],

                "Event ID": investigation.event.event_code,

                "User": investigation.event.username,

                "Host": investigation.event.hostname,

                "Time": investigation.event.timestamp

            })

    if not rows:

        st.success("No alerts detected.")

        return

    df = pd.DataFrame(rows)

    severity = st.selectbox(

        "Severity Filter",

        ["All", "Critical", "High", "Medium", "Low"]

    )

    if severity != "All":

        df = df[
            df["Severity"] == severity
        ]

    st.metric(

        "Total Alerts",

        len(df)

    )

    st.dataframe(

        df,

        use_container_width=True,

        height=600

    )