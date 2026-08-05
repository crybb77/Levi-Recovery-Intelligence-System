import streamlit as st
import json

from pages import home

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="Levi Recovery Intelligence System",
    page_icon="🧠",
    layout="wide"
)

# ----------------------------------------------------
# Session State
# ----------------------------------------------------

if "selected_activity" not in st.session_state:
    st.session_state.selected_activity = None

if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.title("🧠 Levi Recovery Intelligence System")

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "📚 Therapy Library",
        "📝 Daily Log",
        "👥 Caregiver"
    ]
)

# ====================================================
# HOME
# ====================================================

if page == "🏠 Home":

    # Display the Home page header from pages/home.py
    home.show()

    # ------------------------------------------------
    # The remaining sections will be moved into modules
    # one at a time.
    # ------------------------------------------------

    left_column, right_column = st.columns([2, 1])

    with left_column:

        with open("data/activity_library.json", "r") as file:
            activities = json.load(file)

        st.subheader("Today's Tasks")

        for activity in activities:
            st.checkbox(
                activity["name"],
                key=activity["id"]
            )

    with right_column:

        st.subheader("Today's Notes")
        st.info("No notes for today.")

        st.subheader("Today's Appointment")
        st.success("No appointments scheduled.")

    st.write("🚧 Version 1 is currently under development.")

# ====================================================
# THERAPY LIBRARY
# ====================================================

if page == "📚 Therapy Library":

    st.title("📚 Therapy Library")

    if st.session_state.selected_category == "Vision Therapy":

        if st.button("⬅ Back to Therapy Library"):
            st.session_state.selected_category = None
            st.rerun()

        st.header("👁️ Vision Therapy")

        if st.button("👁️ Brock String"):
            with open("therapies/vision/brock_string/brock_string.md", "r") as file:
                st.markdown(file.read())

    else:

        st.write("Select a therapy category:")

        if st.button("👁️ Vision Therapy"):
            st.session_state.selected_category = "Vision Therapy"
            st.rerun()

        if st.button("⚖️ Balance & Mobility"):
            st.success("Coming Soon")

        if st.button("👂 Vestibular Therapy"):
            st.success("Coming Soon")

        if st.button("🗣️ Speech & Communication"):
            st.success("Coming Soon")

        if st.button("🏡 Daily Living Skills"):
            st.success("Coming Soon")

        if st.button("❤️ Wellness"):
            st.success("Coming Soon")

# ====================================================
# DAILY LOG
# ====================================================

if page == "📝 Daily Log":

    st.title("📝 Daily Log")
    st.info("Daily Log coming soon.")

# ====================================================
# CAREGIVER
# ====================================================

if page == "👥 Caregiver":

    st.title("👥 Caregiver")
    st.info("Caregiver tools coming soon.")