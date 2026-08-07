from pathlib import Path

import streamlit as st


# --------------------------------------------------
# Logo Component
# --------------------------------------------------

LOGO_PATH = (
    Path(__file__).parent.parent.parent
    / "assets"
    / "images"
    / "lris_logo.png"
)


def show(width=220):
    """
    Displays the LRIS logo.

    Example:

        from components.logo import show

        show()

        show(width=160)
    """

    st.image(str(LOGO_PATH), width=width)