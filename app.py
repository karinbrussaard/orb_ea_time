import streamlit as st
from datetime import datetime, time
import pytz

st.set_page_config(page_title="ORB EA Time", page_icon="⏰")

st.title("ORB EA Time Calculator")

server_time_input = st.time_input("Wat is de server tijd nu (linksboven MT5)?")

if server_time_input:

    local_now = datetime.now()

    server_now = datetime.combine(local_now.date(), server_time_input)
    offset = server_now - local_now

    ny_tz = pytz.timezone("America/New_York")
    ny_now = datetime.now(ny_tz)
    ny_open = ny_tz.localize(datetime.combine(ny_now.date(), time(9, 30)))

    ny_open_local = ny_open.astimezone()

    ea_time = ny_open_local + offset

    st.success(f"Zet je EA op: {ea_time.strftime('%H:%M')}")
