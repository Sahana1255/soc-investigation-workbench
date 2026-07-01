import os
import streamlit as st

from reporting.pdf_report import PDFReport


def report(incident, investigations):

    st.subheader("📄 Incident Report")

    if st.button("Generate PDF Report"):

        filename = "SOC_Investigation_Report.pdf"

        PDFReport().generate(
            incident,
            investigations,
            filename
        )

        with open(filename, "rb") as file:

            st.download_button(

                "⬇ Download Report",

                file,

                file_name=filename,

                mime="application/pdf"

            )

        os.remove(filename)
        