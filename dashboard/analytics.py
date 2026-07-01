from collections import Counter

import pandas as pd
import plotly.express as px
import streamlit as st


def analytics(incident):

    st.subheader("📈 Investigation Analytics")

    if not incident.events:

        st.info("No events available.")

        return

    ids = Counter(
        str(event.event_code)
        for event in incident.events
        if event.event_code
    )

    users = Counter(
        event.username
        for event in incident.events
        if event.username
    )

    processes = Counter(
        event.process
        for event in incident.events
        if event.process
    )

    col1, col2 = st.columns(2)

    if ids:

        df = pd.DataFrame(
            ids.items(),
            columns=[
                "Event ID",
                "Count"
            ]
        )

        fig = px.bar(
            df,
            x="Event ID",
            y="Count",
            title="Top Event IDs"
        )

        col1.plotly_chart(
            fig,
            use_container_width=True
        )

    if users:

        df = pd.DataFrame(
            users.items(),
            columns=[
                "User",
                "Count"
            ]
        )

        fig = px.bar(
            df,
            x="User",
            y="Count",
            title="Top Users"
        )

        col2.plotly_chart(
            fig,
            use_container_width=True
        )

    if processes:

        df = pd.DataFrame(
            processes.items(),
            columns=[
                "Process",
                "Count"
            ]
        )

        fig = px.pie(
            df,
            names="Process",
            values="Count",
            title="Top Processes"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )