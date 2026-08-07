import streamlit as st

from components.logo import show as show_logo
from styles import colors
from styles import typography


def show():
    """
    Displays the LRIS logo and brand headline at the top of the sidebar.
    """

    with st.sidebar:

        show_logo(width=170)

        st.markdown(
            f"""
            <div style="
                margin-top: 0;
                margin-bottom: 0;
                padding: 18px 0 0 0;
                font-family: {typography.PRIMARY_FONT};
            ">
                <div style="
                    font-size: 22px;
                    font-weight: {typography.SEMIBOLD};
                    color: {colors.TEXT_PRIMARY};
                    margin-bottom: 8px;
                    letter-spacing: -0.03em;
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()