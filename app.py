import streamlit as st
from datetime import datetime, time
import pytz

st.set_page_config(page_title="ORB EA Time", page_icon="⏰")
st.title("ORB EA Time Calculator")

server_time_str = st.text_input(
    "Wat is de server tijd nu? (bijv 15:30)"
)

if server_time_str:

    try:
        server_hour = int(server_time_str.split(":")[0])

        # Lokale tijd
        local_now = datetime.now()
        local_hour = local_now.hour

        # Alleen uurverschil
        offset_hours = server_hour - local_hour

        # New York timezone
        ny_tz = pytz.timezone("America/New_York")
        ny_now = datetime.now(ny_tz)

        # Vandaag 09:30 NY
        ny_open = ny_tz.localize(
            datetime.combine(ny_now.date(), time(9, 30))
        )

        # Zet om naar lokale tijd
        ny_open_local = ny_open.astimezone()

        # Voeg alleen uur-offset toe
        final_hour = (ny_open_local.hour + offset_hours) % 24

        st.success(f"Zet je EA op: {final_hour:02d}:30")

    except:
        st.error("Gebruik formaat HH:MM")
