import streamlit as st

from styles import colors
from styles import typography
from styles import layout


def show(title: str, subtitle: str = ""):
    """
    Displays a standardized LRIS page header.

    Every application page should use this component directly beneath
    the global banner.
    """

    # --------------------------------------------------
    # Page Title
    # --------------------------------------------------

    st.markdown(
        f"""
        <div style="
            font-family:{typography.PRIMARY_FONT};
            font-size:{typography.TITLE};
            font-weight:{typography.BOLD};
            color:{colors.TEXT_PRIMARY};
            margin-bottom:8px;
            line-height:{typography.TIGHT};
        ">
            {title}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Page Subtitle
    # --------------------------------------------------

    if subtitle:

        st.markdown(
            f"""
            <div style="
                font-family:{typography.PRIMARY_FONT};
                font-size:{typography.SUBTITLE};
                font-weight:{typography.MEDIUM};
                color:{colors.TEXT_SECONDARY};
                margin-bottom:{layout.PADDING_LARGE};
                line-height:{typography.NORMAL_LINE};
            ">
                {subtitle}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()