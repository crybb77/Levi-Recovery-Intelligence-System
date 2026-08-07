import json
from pathlib import Path

import streamlit as st

from components.card import show as card
from components.page_header import show as page_header
from styles import colors
from styles import typography


def show(client_name: str):

    page_header(
        f"Good Morning, {client_name}!",
        "Here's Levi's recovery plan for today."
    )

    st.markdown(
        f"""
        <div style="
            background: {colors.SURFACE};
            border: 1px solid {colors.BORDER};
            border-radius: 24px;
            padding: 26px 28px;
            margin-bottom: 28px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 24px;
            font-family: {typography.PRIMARY_FONT};
        ">
            <div style="flex: 1;">
                <div style="font-size: 18px; font-weight: {typography.SEMIBOLD}; color: {colors.TEXT_PRIMARY}; margin-bottom: 8px;">
                    Small steps today. Big progress tomorrow.
                </div>
                <div style="font-size: 15px; color: {colors.TEXT_SECONDARY}; line-height: 1.75; max-width: 720px;">
                    Keep the family aligned with Levi's daily recovery goals, tasks, and appointments.
                </div>
            </div>
            <div style="font-size: 14px; color: {colors.PRIMARY}; font-weight: {typography.SEMIBOLD};">
                View dashboard overview →
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    activity_library_path = Path("data") / "activity_library.json"
    with activity_library_path.open("r", encoding="utf-8") as file:
        activities = json.load(file)

    columns = st.columns([2.4, 1, 1, 1], gap="large")

    with columns[0]:
        st.markdown(
            f"""
            <div style="background: {colors.SURFACE}; border: 1px solid {colors.BORDER}; border-radius: 24px; padding: 24px; box-shadow: 0 18px 36px rgba(15, 118, 110, 0.08); font-family: {typography.PRIMARY_FONT};">
                <div style="font-size: 18px; font-weight: {typography.SEMIBOLD}; color: {colors.TEXT_PRIMARY}; margin-bottom: 18px;">Today's Tasks</div>
                <div style="display: flex; justify-content: space-between; align-items: center; gap: 16px; margin-bottom: 20px;">
                    <div style="font-size: 15px; font-weight: {typography.SEMIBOLD}; color: {colors.TEXT_PRIMARY};">Task list</div>
                    <div style="font-size: 13px; color: {colors.TEXT_SECONDARY};">{len(activities)} items</div>
                </div>
                <div style="display: grid; gap: 12px;">
                    {''.join([
                        f'''<div style="display:flex; align-items:center; justify-content:space-between; gap: 12px; padding: 12px 0; border-bottom: 1px solid rgba(229,233,237,0.95);">
                                <div style="display:flex; align-items:center; gap: 10px;">
                                    <span style=\"width:18px; height:18px; border:2px solid {colors.BORDER}; border-radius:6px; display:inline-block; background:#fff;\"></span>
                                    <div style=\"font-size:15px; color:{colors.TEXT_PRIMARY};\">{activity['name']}</div>
                                </div>
                                <div style=\"font-size:13px; color:{colors.TEXT_SECONDARY};\">{activity.get('time', 'Time TBD')}</div>
                            </div>'''
                        for activity in activities
                    ])}
                </div>
                <div style="margin-top: 18px; font-size: 13px; color: {colors.PRIMARY}; font-weight: {typography.SEMIBOLD};">View all tasks →</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with columns[1]:
        st.markdown(
            f"""
            <div style="background: {colors.SURFACE}; border: 1px solid {colors.BORDER}; border-radius: 24px; padding: 24px; box-shadow: 0 18px 36px rgba(15, 118, 110, 0.08); font-family: {typography.PRIMARY_FONT};">
                <div style="font-size: 18px; font-weight: {typography.SEMIBOLD}; color: {colors.TEXT_PRIMARY}; margin-bottom: 18px;">Today's Appointment</div>
                <div style="font-size: 16px; font-weight: {typography.SEMIBOLD}; color: {colors.TEXT_PRIMARY}; margin-bottom: 8px;">Occupational Therapy</div>
                <div style="font-size: 14px; color: {colors.TEXT_SECONDARY}; margin-bottom: 6px;">With Sarah Johnson, OT</div>
                <div style="display:flex; align-items:center; gap: 10px; margin-top: 12px; margin-bottom: 14px; color: {colors.PRIMARY}; font-weight: {typography.SEMIBOLD};">
                    <span style="display:inline-flex; align-items:center; justify-content:center; width:24px; height:24px; border-radius:12px; background: rgba(15, 118, 110, 0.08);">⏰</span>
                    11:00 AM – 12:00 PM
                </div>
                <div style="font-size: 14px; color: {colors.TEXT_SECONDARY}; margin-bottom: 14px;">Rehab Center</div>
                <div style="font-size: 14px; color: {colors.TEXT_SECONDARY}; line-height: 1.7;">Focus on balance, mobility, and upper-body coordination during today's session.</div>
                <div style="margin-top: 18px; font-size: 13px; color: {colors.PRIMARY}; font-weight: {typography.SEMIBOLD};">View calendar →</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with columns[2]:
        st.markdown(
            f"""
            <div style="background: {colors.SURFACE}; border: 1px solid {colors.BORDER}; border-radius: 24px; padding: 24px; box-shadow: 0 18px 36px rgba(15, 118, 110, 0.08); font-family: {typography.PRIMARY_FONT};">
                <div style="font-size: 18px; font-weight: {typography.SEMIBOLD}; color: {colors.TEXT_PRIMARY}; margin-bottom: 18px;">Today's Notes</div>
                <div style="font-size: 14px; color: {colors.TEXT_SECONDARY}; line-height: 1.75;">
                    Levi had a great weekend! He enjoyed playing board games and went for a nice walk outside.
                </div>
                <div style="margin-top: 16px; font-size: 14px; color: {colors.PRIMARY}; font-weight: {typography.SEMIBOLD}; line-height: 1.75;">
                    Let's focus on balance exercises today and continue building endurance.
                </div>
                <div style="margin-top: 18px; font-size: 13px; color: {colors.PRIMARY}; font-weight: {typography.SEMIBOLD};">Add note →</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with columns[3]:
        st.markdown(
            f"""
            <div style="background: {colors.SURFACE}; border: 1px solid {colors.BORDER}; border-radius: 24px; padding: 24px; box-shadow: 0 18px 36px rgba(15, 118, 110, 0.08); font-family: {typography.PRIMARY_FONT};">
                <div style="font-size: 18px; font-weight: {typography.SEMIBOLD}; color: {colors.TEXT_PRIMARY}; margin-bottom: 18px;">Progress Snapshot</div>
                <div style="display: flex; justify-content: space-between; gap: 20px; align-items: center; margin-bottom: 18px;">
                    <div>
                        <div style="font-size: 14px; color: {colors.TEXT_SECONDARY}; margin-bottom: 6px;">Steps Today</div>
                        <div style="font-size: 24px; font-weight: {typography.SEMIBOLD}; color: {colors.TEXT_PRIMARY};">2,450</div>
                        <div style="font-size: 14px; color: {colors.TEXT_SECONDARY};">Goal: 5,000</div>
                    </div>
                    <div style="display:grid; place-items:center; width: 94px; height: 94px; border-radius: 50%; background: rgba(15,118,110,0.08); color: {colors.PRIMARY}; font-weight: {typography.SEMIBOLD}; font-size: 22px;">
                        49%
                    </div>
                </div>
                <div style="height: 12px; background: {colors.BORDER}; border-radius: 999px; overflow: hidden; margin-bottom: 22px;">
                    <div style="width: 49%; height: 100%; background: {colors.PRIMARY};"></div>
                </div>
                <div style="display: flex; justify-content: space-between; gap: 14px; align-items: center;">
                    <div>
                        <div style="font-size: 14px; color: {colors.TEXT_SECONDARY}; margin-bottom: 4px;">Exercises Completed</div>
                        <div style="font-size: 20px; font-weight: {typography.SEMIBOLD}; color: {colors.TEXT_PRIMARY};">2 / 5</div>
                    </div>
                    <div style="font-size: 14px; font-weight: 700; color: {colors.SUCCESS};">40%</div>
                </div>
                <div style="margin-top: 18px; font-size: 13px; color: {colors.PRIMARY}; font-weight: {typography.SEMIBOLD};">View full progress →</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div style="
            background: #F2FCF7;
            border-radius: 24px;
            padding: 22px 24px;
            margin-top: 22px;
            font-family: {typography.PRIMARY_FONT};
            color: {colors.TEXT_SECONDARY};
            display: flex;
            align-items: center;
            gap: 14px;
        ">
            <div style="font-size: 18px; color: {colors.PRIMARY};">“</div>
            <div>
                <div style="font-size: 15px; line-height: 1.75; color: {colors.TEXT_PRIMARY};">
                    Every day is a new opportunity for progress and connection.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
