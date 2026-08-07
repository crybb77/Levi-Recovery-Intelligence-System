import streamlit as st

from styles import colors
from styles import typography
from styles import layout


def show(title: str):
    """
    Displays a standardized LRIS card title.

    Example:

        with st.container(border=True):
            card.show("Today's Tasks")
    """

    st.markdown(
        f"""
        <div style="
            font-family:{typography.PRIMARY_FONT};
            font-size:{typography.CARD_TITLE};
            font-weight:{typography.SEMIBOLD};
            color:{colors.TEXT_PRIMARY};
            margin-bottom:{layout.PADDING_MEDIUM};
            line-height:{typography.TIGHT};
        ">
            {title}
        </div>
        """,
        unsafe_allow_html=True,
    )