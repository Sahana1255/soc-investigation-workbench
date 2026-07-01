import streamlit as st

from services.search_service import SearchService


def search(
    incident
):

    st.subheader(
        "🔍 Search"
    )

    keyword = st.text_input(
        "Search"
    )

    if not keyword:

        return

    service = SearchService()

    events = service.events(
        incident.events,
        keyword
    )

    st.write(
        f"Events Found: {len(events)}"
    )

    for event in events[:50]:

        st.write(

            event.timestamp,

            event.event_code,

            event.username,

            event.hostname

        )