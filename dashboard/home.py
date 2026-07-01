import os
import tempfile

import streamlit as st

from services.soc_engine import SOCEngine

from dashboard.cases import cases
from dashboard.summary import summary
from dashboard.analytics import analytics
from dashboard.events import events
from dashboard.iocs import iocs
from dashboard.timeline import timeline
from dashboard.mitre import mitre
from dashboard.risk import risk
from dashboard.graph import relationship_graph
from dashboard.reports import report
from dashboard.alerts import alerts


def home():

    st.title("🛡 SOC Investigation Workbench")

    st.write(
        "Upload one or more evidence files to begin an investigation."
    )

    uploaded = st.file_uploader(
        "Upload Evidence",
        type=[
            "evtx",
            "log",
            "csv",
            "txt",
            "eml",
            "msg",
            "json",
            "ioc"
        ],
        accept_multiple_files=True
    )

    if not uploaded:

        tab = st.tabs([
            "📂 Cases"
        ])[0]

        with tab:
            cases()

        return

    temp_files = []

    for file in uploaded:

        suffix = os.path.splitext(
            file.name
        )[1]

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp:

            temp.write(
                file.read()
            )

            temp_files.append(
                temp.name
            )

    engine = SOCEngine()

    with st.spinner(
        "Investigating evidence..."
    ):

        result = engine.investigate(
            title="Interactive Investigation",
            evidence_files=temp_files
        )

    case = result["case"]

    incident = result["incident"]

    investigations = result["investigations"]

    st.success(
        f"✅ Investigation Completed | {case['case_id']}"
    )

    (
        tab1,
        tab2,
        tab3,
        tab4,
        tab5,
        tab6,
        tab7,
        tab8,
        tab9,
        tab10,
        tab11
    ) = st.tabs([

        "📂 Cases",

        "📊 Summary",

        "📈 Analytics",

        "📋 Events",

        "🌐 IOCs",

        "🕒 Timeline",

        "🎯 MITRE ATT&CK",

        "⚠ Risk",

        "🔗 Relationships",

        "📄 Report",

        "🚨 Alerts"

    ])

    with tab1:
        cases()

    with tab2:
        summary(
            incident
        )

    with tab3:
        analytics(
            incident
        )

    with tab4:
        events(
            incident.events
        )

    with tab5:
        iocs(
            incident.iocs
        )

    with tab6:
        timeline(
            incident.events
        )

    with tab7:
        mitre(
            investigations
        )

    with tab8:
        risk(
            investigations
        )

    with tab9:
        relationship_graph(
            incident.events
        )

    with tab10:
        report(
            incident,
            investigations
        )

    with tab11:
        alerts(
            investigations
        )

    for file in temp_files:

        if os.path.exists(
            file
        ):

            os.remove(
                file
            )