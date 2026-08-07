import streamlit as st
import json

from components.banner import show as show_banner
from components.card import show as card
from components.page_header import show as page_header
from components.sidebar import show as show_sidebar

from services.client_service import get_preferred_name

from page_views import home
from page_views import get_to_know

from styles.css import load_css

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="Levi Recovery Intelligence System",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

# ----------------------------------------------------
# Session State
# ----------------------------------------------------

if "selected_activity" not in st.session_state:
    st.session_state.selected_activity = None

if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

# ----------------------------------------------------
# Global Banner
# ----------------------------------------------------

client_name = get_preferred_name()

show_banner()

# ----------------------------------------------------
# Sidebar Navigation
# ----------------------------------------------------

page = show_sidebar(client_name)

# ====================================================
# HOME
# ====================================================

if page == "Home":

    home.show(client_name)

# ====================================================
# GET TO KNOW LEVI
# ====================================================

elif page == f"Get to Know {client_name}":

    get_to_know.show()

# ====================================================
# THERAPY LIBRARY
# ====================================================

elif page == "Therapy Library":

    page_header(
        "Therapy Library",
        "Browse therapies and treatment resources."
    )

    if st.session_state.selected_category == "Vision Therapy":

        if st.button("Back to Therapy Library"):
            st.session_state.selected_category = None
            st.rerun()

        card("Vision Therapy")

        if st.button("Brock String"):

            with open(
                "therapies/vision/brock_string/brock_string.md",
                "r",
                encoding="utf-8"
            ) as file:

                st.markdown(file.read())

    else:

        st.write("Select a therapy category:")

        if st.button("Vision Therapy"):
            st.session_state.selected_category = "Vision Therapy"
            st.rerun()

        if st.button("Balance & Mobility"):
            st.info("Coming Soon")

        if st.button("Vestibular Therapy"):
            st.info("Coming Soon")

        if st.button("Speech & Communication"):
            st.info("Coming Soon")

        if st.button("Daily Living Skills"):
            st.info("Coming Soon")

        if st.button("Wellness"):
            st.info("Coming Soon")

# ====================================================
# DAILY LOG
# ====================================================

elif page == "Daily Log":

    page_header(
        "Daily Log",
        "Record daily observations, activities, and progress."
    )

    st.info("Daily Log coming soon.")

# ====================================================
# CAREGIVER
# ====================================================

elif page == "Caregiver":

    page_header(
        "Caregiver",
        "Resources and tools for the care team."
    )

    st.info("Caregiver tools coming soon.")