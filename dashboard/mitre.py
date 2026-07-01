import pandas as pd
import streamlit as st


def mitre(investigations):

    st.subheader("🎯 MITRE ATT&CK Mapping")

    rows = []

    for investigation in investigations:

        for technique in investigation.techniques:

            rows.append({

                "Framework": technique.framework,

                "Tactic": technique.tactic,

                "Technique": technique.technique

            })

    if not rows:

        st.info("No MITRE techniques mapped.")

        return

    df = pd.DataFrame(rows)

    st.dataframe(
        df,
        use_container_width=True,
        height=300
    )