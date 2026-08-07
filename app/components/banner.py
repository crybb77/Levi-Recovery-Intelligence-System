import base64
from datetime import datetime
from pathlib import Path

import streamlit as st

from services.client_service import get_client_profile
from components.client_card import show as show_client_card

from styles import colors
from styles import typography
from styles import layout


def get_banner_image():

    image_path = (
        Path(__file__).parent.parent.parent
        / "assets"
        / "images"
        / "hero_banner.png"
    )

    with open(image_path, "rb") as image:
        return base64.b64encode(image.read()).decode()


def get_logo_image():

    image_path = (
        Path(__file__).parent.parent.parent
        / "assets"
        / "images"
        / "lris_logo.png"
    )

    with open(image_path, "rb") as image:
        return base64.b64encode(image.read()).decode()


def show():

    client = get_client_profile()

    banner_image = get_banner_image()
    logo_image = get_logo_image()

    local_time = datetime.now().strftime("%I:%M %p")
    current_date = datetime.now().strftime("%b %d, %Y")
    initials = client["preferred_name"][0] if client["preferred_name"] else "L"

    st.html(
        f"""
<style>

.lris-banner {{
    width: calc(100% + ({layout.PAGE_CONTENT_PADDING} * 2));
    margin-left: -{layout.PAGE_CONTENT_PADDING};
    margin-right: -{layout.PAGE_CONTENT_PADDING};
    margin-top: -{layout.PAGE_TOP_PADDING};
    margin-bottom: {layout.SECTION_GAP};
    background-image: url("data:image/png;base64,{banner_image}");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    padding:0 {layout.BANNER_PADDING_X};
    min-height: {layout.BANNER_HEIGHT};
    display: flex;
    align-items: center;
    box-sizing: border-box;    position: relative;    color: {colors.TEXT_LIGHT};
    border-radius: {layout.BANNER_RADIUS};
    box-shadow: 0 30px 68px rgba(15, 118, 110, 0.18);
}}

.banner-row {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 18px;
    flex-wrap: wrap;
}}

.banner-left{{

    flex:1;

    display:flex;

    align-items:center;

    justify-content:flex-start;

    padding-left:48px;
}}

.branding-text{{

    display:flex;

    flex-direction:column;

    justify-content:center;

}}

.branding-text h1{{

    margin:0;

    color:#16324F;

    font-size:42px;

    font-weight:700;

    letter-spacing:-0.02em;

    line-height:1.15;

}}

.branding-text p{{

    margin-top:12px;

    margin-bottom:0;

    color:#0F766E;

    font-size:22px;

    font-style:italic;

    font-weight:500;

}}

.hero-subtitle {{
    margin: 0;
    font-size: 30px;
    font-weight: {typography.MEDIUM};
    color: rgba(255,255,255,0.92);
    line-height: 1.4;
    max-width: 620px;
}}

.banner-logo{{
    width:300px;
    height:auto;
    margin-right:24px;
    display:inline-block;
}}

.banner-right {{

    position: absolute;
    right: 56px;
    bottom: 0;
    width: 280px;
    max-width: 280px;
    flex-shrink: 0;
    z-index: 2;

}}

.client-card {{
    background: rgba(255,255,255,.72);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.45);
    border-radius: 0px;
    padding: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,.10);
    color: {colors.TEXT_PRIMARY};
}}

.client-top {{
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 12px;
}}

.client-avatar {{
    width: 58px;
    height: 58px;
    border-radius: 50%;
    background: linear-gradient(135deg, rgba(34,197,94,0.18), rgba(15,118,110,0.16));
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    font-weight: 700;
    color: {colors.PRIMARY};
}}

.client-summary {{
    display: flex;
    flex-direction: column;
    gap: 4px;
}}

.client-title {{
    margin: 0;
    font-size: 11px;
    font-weight: 700;
    color: {colors.TEXT_SECONDARY};
    text-transform: uppercase;
    letter-spacing: 0.18em;
}}

.client-name {{
    margin: 0;
    font-size: 24px;
    font-weight: {typography.SEMIBOLD};
    color: {colors.TEXT_PRIMARY};
}}

.client-program {{
    margin: 0;
    font-size: 14px;
    color: {colors.TEXT_SECONDARY};
    line-height: 1.6;
}}

.client-divider {{
    height: 1px;
    background: rgba(15, 118, 110, 0.12);
    margin: 10px 0;
}}

.client-info-grid {{
    display: grid;
    gap: 8px;
}}

.client-info-card {{
    background: rgba(244, 251, 248, 0.95);
    border-radius: 20px;
    padding: 10px 12px;
}}

.client-info-label {{
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    color: {colors.TEXT_SECONDARY};
    margin-bottom: 6px;
}}

.client-info-value {{
    font-size: 18px;
    font-weight: 700;
    color: {colors.TEXT_PRIMARY};
    margin-bottom: 6px;
}}

.client-info-note {{
    font-size: 13px;
    color: {colors.TEXT_SECONDARY};
}}

.status-pill {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 10px 14px;
    border-radius: 999px;
    background: rgba(34, 197, 94, 0.14);
    color: {colors.SUCCESS};
    font-size: 13px;
    font-weight: 700;
}}

</style>

<div class="lris-banner">
    <div class="banner-row">
        <div class="banner-left">
            <img class="banner-logo" src="data:image/png;base64,{logo_image}" alt="LRIS logo" />

            <div class="branding-text">

                <h1>
                    Levi Recovery Intelligence System
                </h1>

                <p>
                    Organizing care. Supporting recovery.
                </p>

            </div>

        </div>
        <div class="banner-right">
            {show_client_card()}
        </div>

    </div>
</div>
"""
    )