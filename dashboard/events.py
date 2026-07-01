import pandas as pd
import streamlit as st


def events(events):

    st.subheader("📋 Event Explorer")

    if not events:

        st.info("No events.")

        return

    search = st.text_input(
        "Search"
    ).lower()

    rows = []

    for event in events:

        text = " ".join([

            str(event.event_code),

            str(event.username),

            str(event.hostname),

            str(event.process),

            str(event.source_ip)

        ]).lower()

        if search and search not in text:

            continue

        rows.append({

            "Time": event.timestamp,

            "Event ID": event.event_code,

            "User": event.username,

            "Host": event.hostname,

            "IP": event.source_ip,

            "Process": event.process

        })

    st.dataframe(

        pd.DataFrame(rows),

        use_container_width=True,

        height=600

    )