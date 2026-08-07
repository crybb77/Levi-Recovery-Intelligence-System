import streamlit as st

from components.sidebar_header import show as show_sidebar_header
from styles import colors
from styles import typography
from pathlib import Path
import base64


def _encode_icon(name: str) -> str:
    base = Path(__file__).parent.parent.parent / "assets" / "icons"
    icon_path = base / name
    if not icon_path.exists():
        return ""
    with open(icon_path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"


ICON_SIZE = 36


def show(client_name: str):

    show_sidebar_header()

    # nav items: (label, icon filename)
    nav_items = [
        ("Home", "Home.png"),
        (f"Get to Know {client_name}", "Get_to_Know.png"),
        ("Therapy Library", "Therapy.png"),
        ("Daily Log", "Daily_Log.png"),
        ("Caregiver", "Caregiver.png"),
    ]

    # ensure a session_state page key exists
    if "page" not in st.session_state:
        st.session_state["page"] = "Home"

    st.sidebar.markdown(
        """
        <style>
            [data-testid="stSidebar"] .stButton {
                width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
                display: flex !important;
                justify-content: flex-start !important;
                align-items: center !important;
            }
            [data-testid="stSidebar"] .stButton > button {
                width: 220px !important;
                min-width: 220px !important;
                max-width: 220px !important;
                height: 56px;
                box-sizing: border-box;
                border-radius: 18px;
                border: 1px solid transparent;
                background-color: transparent;
                color: #07191f !important;
                font-size: 17px !important;
                font-weight: 800;
                text-align: left !important;
                padding: 0 16px !important;
                display: flex !important;
                align-items: center !important;
                justify-content: flex-start !important;
                white-space: nowrap !important;
                overflow: hidden !important;
                text-overflow: ellipsis !important;
                margin: 0 !important;
            }
            [data-testid="stSidebar"] .stButton > button > div {
                width: 100% !important;
                padding: 0 !important;
                margin: 0 !important;
                display: flex !important;
                align-items: center !important;
                justify-content: flex-start !important;
            }
            [data-testid="stSidebar"] .stButton > button > div > span {
                width: 100% !important;
                padding: 0 !important;
                margin: 0 !important;
                display: flex !important;
                align-items: center !important;
                justify-content: flex-start !important;
                text-align: left !important;
            }
            [data-testid="stSidebar"] .stButton > button > div > span > span {
                width: 100% !important;
                padding: 0 !important;
                margin: 0 !important;
                display: block !important;
                text-align: left !important;
            }
            [data-testid="stSidebar"] .stButton > button:hover,
            [data-testid="stSidebar"] .stButton > button:focus {
                background-color: rgba(15,118,110,0.08) !important;
                border-color: rgba(15,118,110,0.16) !important;
                color: #0f172a !important;
            }
            [data-testid="stSidebar"] .stButton > button,
            [data-testid="stSidebar"] .stButton > button * {
                color: #07191f !important;
            }
            [data-testid="stSidebar"] .stButton > button > div > span > span {
                font-size: 17px !important;
                font-weight: 800 !important;
                color: #07191f !important;
                text-align: left !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # render navigation with icons using columns so icons can be sized consistently
    for label, icon_file in nav_items:
        icon_data = _encode_icon(icon_file)
        display_label = label
        is_active = st.session_state.get("page") == label
        if is_active and label != "Home":
            display_label = "● " + label

        cols = st.sidebar.columns([0.12, 0.88])
        with cols[0]:
            if icon_data:
                st.markdown(
                    f"""
                    <div style='display:flex; align-items:center; justify-content:center; height:56px;'>
                                <img src='{icon_data}' width='{ICON_SIZE}' style='display:block; height:auto; filter: invert(16%) sepia(66%) saturate(800%) hue-rotate(156deg) brightness(75%) contrast(104%);' />
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                st.write("")
        with cols[1]:
            if st.button(display_label, key=f"nav_{label}"):
                st.session_state["page"] = label

    st.sidebar.divider()

    # bottom welcome card
    st.sidebar.markdown(
        f"""
        <div style="
            margin-top: 18px;
            padding: 16px 16px 16px 16px;
            border-radius: 22px;
            background: rgba(255,255,255,0.96);
            box-shadow: 0 18px 36px rgba(15,118,110,0.08);
        ">
            <div style="display:flex; align-items:center; gap: 14px;">
                <div style="width: 54px; height: 54px; border-radius: 50%; overflow: hidden;">
                    <img src="https://via.placeholder.com/54" style="width:100%; height:100%; object-fit:cover;" />
                </div>
                <div style="flex:1;">
                    <div style="font-family: {typography.PRIMARY_FONT}; font-size: 16px; font-weight: {typography.SEMIBOLD}; color: {colors.TEXT_PRIMARY}; margin-bottom: 4px;">
                        Welcome, {client_name}
                    </div>
                    <div style="font-family: {typography.PRIMARY_FONT}; font-size: 12px; color: {colors.TEXT_SECONDARY}; line-height: 1.4;">
                        Primary Caregiver
                    </div>
                </div>
                <div style="font-size: 18px; color: {colors.TEXT_SECONDARY};">▾</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    return st.session_state.get("page", "Home")