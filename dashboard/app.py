import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="Smart Agriculture Dashboard",
    page_icon="🌱",
    layout="wide"
)

# Auto refresh every 3 seconds
st_autorefresh(interval=3000, key="refresh")

st.title("🌱 IoT Smart Agriculture Monitoring Dashboard")

BASE_DIR = Path(__file__).resolve().parent.parent
csv_file = BASE_DIR / "data" / "sensor_log.csv"

if not csv_file.exists():
    st.error("sensor_log.csv not found")
    st.stop()

try:
    df = pd.read_csv(csv_file)
except Exception as e:
    st.error(f"CSV Error: {e}")
    st.stop()

if df.empty:
    st.warning("Waiting for sensor data...")
    st.stop()

latest = df.iloc[-1]

# ---------------- KPI CARDS ----------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "🌡 Temperature",
    f"{latest['temperature']} °C"
)

col2.metric(
    "💧 Humidity",
    f"{latest['humidity']} %"
)

col3.metric(
    "🌱 Soil Moisture",
    f"{latest['soil_moisture']} %"
)

col4.metric(
    "🚰 Water Level",
    f"{latest['water_level']} %"
)

st.divider()

# ---------------- ALERTS ----------------

st.subheader("⚠ Alerts")

if latest["temperature"] > 35:
    st.error("High Temperature Detected")

if latest["soil_moisture"] < 30:
    st.warning("Low Soil Moisture")

if latest["water_level"] < 20:
    st.error("Low Water Level")

if latest["pump_status"] == "ON":
    st.success("Pump Status: ON")
else:
    st.info("Pump Status: OFF")

st.divider()

# ---------------- CHARTS ----------------

st.subheader("📈 Sensor Trends")

chart1 = px.line(
    df.tail(50),
    x="timestamp",
    y="temperature",
    title="Temperature Trend"
)

st.plotly_chart(
    chart1,
    use_container_width=True
)

chart2 = px.line(
    df.tail(50),
    x="timestamp",
    y="soil_moisture",
    title="Soil Moisture Trend"
)

st.plotly_chart(
    chart2,
    use_container_width=True
)

chart3 = px.line(
    df.tail(50),
    x="timestamp",
    y="water_level",
    title="Water Level Trend"
)

st.plotly_chart(
    chart3,
    use_container_width=True
)

# ---------------- DATA TABLE ----------------

st.subheader("📋 Latest Sensor Records")

st.dataframe(
    df.tail(20),
    use_container_width=True
)

# ---------------- DOWNLOAD ----------------

csv = df.to_csv(index=False)

st.download_button(
    label="⬇ Download CSV Report",
    data=csv,
    file_name="agriculture_report.csv",
    mime="text/csv"
)