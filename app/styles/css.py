import base64
from pathlib import Path

import streamlit as st

from styles import colors
from styles import layout
from styles import typography


def _icon_base64(filename: str) -> str:
    icon_path = Path(__file__).parent.parent.parent / "assets" / "icons" / filename
    with open(icon_path, "rb") as icon_file:
        return base64.b64encode(icon_file.read()).decode()


def load_css():

    home_icon = _icon_base64("Home.png")
    get_to_know_icon = _icon_base64("Get_to_Know.png")
    therapy_icon = _icon_base64("Therapy.png")
    daily_log_icon = _icon_base64("Daily_Log.png")
    caregiver_icon = _icon_base64("Caregiver.png")

    st.markdown(
        f"""
<style>

/* ---------- Page ---------- */

.stApp {{
    background: {colors.BACKGROUND};
    color: {colors.TEXT_PRIMARY};
}}

.block-container {{

    padding-top: {layout.PAGE_TOP_PADDING};
    padding-bottom: {layout.PAGE_BOTTOM_PADDING};

    padding-left: 0px;
    padding-right: 0px;

    max-width: 100%;

}}

.stMarkdown {{
    font-family: {typography.PRIMARY_FONT};
}}

/* ---------- Sidebar ---------- */

section[data-testid="stSidebar"] {{
    background: rgba(248, 250, 252, 0.98);
    border-right: 1px solid {colors.DIVIDER};
}}

section[data-testid="stSidebar"] .css-1d391kg {{
    padding-top: 28px;
    padding-left: 22px;
    padding-right: 22px;
    padding-bottom: 26px;
    background: {colors.SURFACE};
    border-radius: 28px;
    box-shadow: 0 22px 44px rgba(15, 118, 110, 0.08);
    border: 1px solid rgba(209, 213, 219, 0.5);
}}

section[data-testid="stSidebar"] .stRadio > div {{
    margin-top: 20px;
}}

section[data-testid="stSidebar"] input[type="radio"] {{
    position: absolute !important;
    opacity: 0 !important;
    width: 1px !important;
    height: 1px !important;
    margin: 0 !important;
    padding: 0 !important;
    border: 0 !important;
    clip: rect(0 0 0 0) !important;
    overflow: hidden !important;
}}

section[data-testid="stSidebar"] .stRadio label {{
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 14px 18px;
    border-radius: 20px;
    margin-bottom: 12px;
    cursor: pointer;
    transition: background 0.25s ease, color 0.25s ease, border-color 0.25s ease, transform 0.25s ease;
    border: 1px solid rgba(209,213,219,0.26);
    font-weight: 600;
    color: {colors.TEXT_PRIMARY};
    background: rgba(255,255,255,0.98);
    box-shadow: 0 14px 30px rgba(15, 118, 110, 0.06);
}}

section[data-testid="stSidebar"] .stRadio label:hover {{
    background: rgba(15, 118, 110, 0.08);
    transform: translateX(1px);
}}

section[data-testid="stSidebar"] .stRadio input[type="radio"]:checked + div label,
section[data-testid="stSidebar"] .stRadio input[type="radio"]:checked + div div,
section[data-testid="stSidebar"] .stRadio input[type="radio"]:checked + label,
section[data-testid="stSidebar"] .stRadio input[type="radio"]:checked ~ label,
section[data-testid="stSidebar"] .stRadio input[type="radio"]:checked ~ div label,
section[data-testid="stSidebar"] .stRadio input[type="radio"]:checked ~ div div {{
    background: {colors.PRIMARY};
    color: white !important;
    border-color: {colors.PRIMARY};
    box-shadow: 0 18px 40px rgba(15, 118, 110, 0.18);
    font-weight: 700;
}}

section[data-testid="stSidebar"] .stRadio input[type="radio"]:checked + div label::before,
section[data-testid="stSidebar"] .stRadio input[type="radio"]:checked + div div::before,
section[data-testid="stSidebar"] .stRadio input[type="radio"]:checked + label::before,
section[data-testid="stSidebar"] .stRadio input[type="radio"]:checked ~ label::before,
section[data-testid="stSidebar"] .stRadio input[type="radio"]:checked ~ div label::before,
section[data-testid="stSidebar"] .stRadio input[type="radio"]:checked ~ div div::before {{
    background-color: rgba(255, 255, 255, 0.18);
    border-radius: 999px;
    width: 28px;
    height: 28px;
}}

section[data-testid="stSidebar"] .stRadio label:has(input:checked) {{
    background: {colors.PRIMARY};
    color: white !important;
}}

section[data-testid="stSidebar"] .stRadio label::before {{
    content: "";
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    transition: background-color 0.2s ease, transform 0.2s ease;
}}

section[data-testid="stSidebar"] .stRadio label:nth-of-type(1)::before {{
    background-image: url("data:image/png;base64,{home_icon}");
}}

section[data-testid="stSidebar"] .stRadio label:nth-of-type(2)::before {{
    background-image: url("data:image/png;base64,{get_to_know_icon}");
}}

section[data-testid="stSidebar"] .stRadio label:nth-of-type(3)::before {{
    background-image: url("data:image/png;base64,{therapy_icon}");
}}

section[data-testid="stSidebar"] .stRadio label:nth-of-type(4)::before {{
    background-image: url("data:image/png;base64,{daily_log_icon}");
}}

section[data-testid="stSidebar"] .stRadio label:nth-of-type(5)::before {{
    background-image: url("data:image/png;base64,{caregiver_icon}");
}}

section[data-testid="stSidebar"] .stButton > button {{
    border-radius: 16px;
    margin-top: 16px;
}}

/* ---------- Dashboard Cards ---------- */

div[data-testid="stVerticalBlockBorderWrapper"] {{
    border-radius: {layout.CARD_RADIUS} !important;
    border: 1px solid {colors.BORDER} !important;
    box-shadow: 0 14px 32px rgba(15, 118, 110, 0.08);
    background: {colors.SURFACE} !important;
}}

div[data-testid="stVerticalBlockBorderWrapper"] .stMarkdown {{
    font-family: {typography.PRIMARY_FONT};
}}

</style>
""",
        unsafe_allow_html=True,
    )
