from collections import Counter

import streamlit as st


def statistics(
    incident
):

    st.subheader(
        "📊 Statistics"
    )

    st.metric(
        "Events",
        len(
            incident.events
        )
    )

    st.metric(
        "IOCs",
        len(
            incident.iocs
        )
    )

    counter = Counter(

        event.event_code

        for event in incident.events

    )

    st.write(
        "Top Event IDs"
    )

    st.write(
        dict(
            counter.most_common(10)
        )
    )