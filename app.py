import streamlit as st
from datetime import datetime, time, timedelta
import pytz

st.set_page_config(page_title="ORB EA Time", page_icon="⏰")
st.title("ORB EA Time Calculator")

server_time_input = st.time_input("Wat is de server tijd nu (linksboven MT5)?")

if server_time_input:

    # Huidige lokale datum + tijd
    local_now = datetime.now()

    # Maak datetime van ingevoerde server tijd (vandaag)
    server_now = datetime.combine(local_now.date(), server_time_input)

    # Bereken exact verschil in minuten
    offset = server_now - local_now

    # New York timezone
    ny_tz = pytz.timezone("America/New_York")

    # Vandaag 09:30 NY tijd
    ny_today = datetime.now(ny_tz).date()
    ny_open = ny_tz.localize(datetime.combine(ny_today, time(9, 30)))

    # Zet NY open om naar lokale tijd
    ny_open_local = ny_open.astimezone()

    # Voeg exact server offset toe
    ea_time = ny_open_local + offset

    st.success(f"Zet je EA op: {ea_time.strftime('%H:%M')}")
