import streamlit as st

from dashboard.sidebar import sidebar
from dashboard.home import home


st.set_page_config(
    page_title="SOC Investigation Workbench",
    page_icon="🛡️",
    layout="wide"
)

sidebar()

home()