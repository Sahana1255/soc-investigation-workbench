import streamlit as st


def sidebar():

    st.sidebar.title("🛡 SOC Investigation Workbench")

    st.sidebar.divider()

    st.sidebar.info(
        "Upload one or more security evidence files to begin an investigation."
    )

    st.sidebar.divider()

    st.sidebar.subheader("📂 Supported Evidence")

    st.sidebar.success("✔ Windows Security (.evtx)")
    st.sidebar.success("✔ Linux Logs (.log)")
    st.sidebar.success("✔ Firewall Logs (.csv)")

    st.sidebar.subheader("🚧 Coming Soon")

    st.sidebar.info("📧 Email Headers (.eml)")
    st.sidebar.info("📊 Generic CSV Logs")
    st.sidebar.info("🛡 IOC Lists (.json/.ioc)")

    st.sidebar.divider()

    st.sidebar.subheader("📌 Investigation Workflow")

    st.sidebar.markdown("""
1. Upload Evidence
2. Parse Evidence
3. Extract Events
4. Extract IOCs
5. Threat Intelligence
6. MITRE Mapping
7. Risk Assessment
8. Timeline Reconstruction
9. Relationship Analysis
10. Generate Report
""")

    st.sidebar.divider()

    st.sidebar.caption("SOC Investigation Workbench v1.0")