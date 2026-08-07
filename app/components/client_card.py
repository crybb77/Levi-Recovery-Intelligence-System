import base64
from datetime import datetime
from pathlib import Path

from services.client_service import get_client_profile

from styles import colors
from styles import layout
from styles import typography


def get_client_photo(preferred_name: str) -> str | None:
    photo_path = (
        Path(__file__).parent.parent.parent
        / "client"
        / "photos"
        / f"{preferred_name}_photo.png"
    )

    if not photo_path.exists():
        return None

    with open(photo_path, "rb") as image_file:
        return f"data:image/png;base64,{base64.b64encode(image_file.read()).decode()}"


def show():

    client = get_client_profile()

    current_date = datetime.now().strftime("%b %d, %Y")
    current_day = datetime.now().strftime("%A")
    current_time = datetime.now().strftime("%I:%M %p")

    preferred_name = client["preferred_name"]
    initials = preferred_name[0] if preferred_name else "L"
    photo_src = get_client_photo(preferred_name)

    return f"""

<div class="client-card">

    <div class="client-card-row">
        <div class="client-avatar">{f'<img class="client-photo" src="{photo_src}" alt="{preferred_name} photo" />' if photo_src else initials}</div>
        <div class="client-info">
            <div class="client-field">
                <span class="client-label">Client:</span>
                <span class="client-value">{preferred_name}</span>
            </div>
            <div class="client-field">
                <span class="client-label">Status:</span>
                <span class="client-status-value">{client["status"]}</span>
            </div>
        </div>
    </div>

    <div class="client-divider"></div>

    <div class="meta-details">
        <div class="meta-date">{current_date}</div>
        <div class="meta-time">{current_day} • {current_time}</div>
    </div>
</div>

<style>

.client-card{{
    width: 100%;
    max-width: 280px;
    background: linear-gradient(180deg, rgba(255,255,255,0.92) 0%, rgba(255,255,255,0.6) 28%, rgba(255,255,255,0.28) 60%, rgba(255,255,255,0.12) 100%);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.68);
    border-radius: 0px;
    padding: 18px;
    box-shadow: 0 18px 42px rgba(0,0,0,0.08);
    color: {colors.TEXT_PRIMARY};
}}

.client-card-row{{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    margin-bottom: 14px;
}}

.client-avatar{{
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: linear-gradient(135deg, rgba(34,197,94,0.16), rgba(15,118,110,0.16));
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    font-weight: 700;
    color: {colors.PRIMARY};
    overflow: hidden;
}}

.client-photo{{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}}

.client-info{{
    flex: 0 0 auto;
    min-width: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 4px;
}}

.client-field{{
    display: flex;
    gap: 8px;
    align-items: baseline;
    flex-wrap: wrap;
}}

.client-label{{
    font-size: 12px;
    font-weight: 700;
    color: {colors.TEXT_SECONDARY};
    letter-spacing: 0.08em;
    text-transform: uppercase;
}}

.client-value{{
    font-size: 16px;
    font-weight: {typography.SEMIBOLD};
    color: {colors.TEXT_PRIMARY};
}}

.client-status-value{{
    font-size: 14px;
    font-weight: 700;
    color: #166534;
}}

.client-divider{{
    height: 1px;
    background: rgba(15, 118, 110, 0.16);
    margin: 0 -18px 14px;
}}

.meta-details{{
    text-align: center;
    min-width: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
}}

.meta-date{{
    font-size: 13px;
    font-weight: 700;
    color: {colors.TEXT_PRIMARY};
}}

.meta-time{{
    margin-top: 2px;
    font-size: 12px;
    color: {colors.TEXT_SECONDARY};
}}

</style>

"""