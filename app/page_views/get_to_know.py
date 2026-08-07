import streamlit as st

from components.page_header import show as page_header
from services.client_service import get_preferred_name


def show():

    client_name = get_preferred_name()

    page_header(
        f"Get to Know {client_name}",
        f"Learn about {client_name}'s personality, communication style, interests, routines, and rehabilitation journey."
    )

    st.info("This page is under development.")