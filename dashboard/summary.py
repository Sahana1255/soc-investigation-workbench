import streamlit as st


def summary(incident):

    st.subheader("📊 Incident Overview")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Events", len(incident.events))
    c2.metric("IOCs", len(incident.iocs))
    c3.metric("Evidence", len(incident.evidence))
    c4.metric("Relationships", len(incident.relationships))
    c5.metric("Risk Score", incident.risk_score)