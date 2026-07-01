import pandas as pd
import streamlit as st


def timeline(events):

    st.subheader("🕒 Investigation Timeline")

    rows = []

    for event in sorted(events, key=lambda e: e.timestamp):

        rows.append({

            "Time": event.timestamp,

            "Event ID": event.event_code,

            "User": event.username,

            "Host": event.hostname,

            "Process": event.process,

            "Source IP": event.source_ip

        })

    st.dataframe(
        pd.DataFrame(rows),
        use_container_width=True,
        height=400
    )