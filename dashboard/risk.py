import streamlit as st


def risk(investigations):

    st.subheader("⚠ Risk Assessment")

    if not investigations:

        st.info("No investigations available.")

        return

    critical = 0
    high = 0
    medium = 0
    low = 0

    for investigation in investigations:

        severity = getattr(
            investigation,
            "severity",
            "Low"
        )

        if severity == "Critical":
            critical += 1

        elif severity == "High":
            high += 1

        elif severity == "Medium":
            medium += 1

        else:
            low += 1

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Critical", critical)

    c2.metric("High", high)

    c3.metric("Medium", medium)

    c4.metric("Low", low)