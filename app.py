import streamlit as st
from datetime import datetime, time, timedelta
import pytz

st.set_page_config(page_title="ORB EA Time", page_icon="⏰")
st.title("ORB EA Time Calculator")

server_time_str = st.text_input(
    "Wat is de server tijd nu (bijv 15:30 of 15:30:12)?"
)

if server_time_str:

    try:
        # Parse ingevoerde tijd
        if len(server_time_str.split(":")) == 2:
            server_time = datetime.strptime(server_time_str, "%H:%M").time()
        else:
            server_time = datetime.strptime(server_time_str, "%H:%M:%S").time()

        local_now = datetime.now()

        server_now = datetime.combine(local_now.date(), server_time)

        # Exact verschil in seconden
        offset = server_now - local_now

        ny_tz = pytz.timezone("America/New_York")

        ny_today = datetime.now(ny_tz).date()
        ny_open = ny_tz.localize(datetime.combine(ny_today, time(9, 30)))

        ny_open_local = ny_open.astimezone()

        ea_time = ny_open_local + offset

        st.success(f"Zet je EA op: {ea_time.strftime('%H:%M:%S')}")

    except:
        st.error("Gebruik formaat HH:MM of HH:MM:SS")
