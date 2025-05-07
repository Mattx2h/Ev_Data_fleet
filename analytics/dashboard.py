import streamlit as st
import sqlite3
import pandas as pd

st.title("EV Fleet Data Dashboard")

conn = sqlite3.connect("ev_data.db")
df = pd.read_sql_query("SELECT * FROM ev_data", conn)

if df.empty:
    st.warning("No data available yet.")
else:
    st.metric("Total Records", len(df))
    st.metric("Avg Battery Level", round(df["battery_level"].mean(), 2))
    st.metric("Avg Speed (kph)", round(df["speed_kph"].mean(), 2))

    st.subheader("Battery Level Distribution")
    st.bar_chart(df["battery_level"])

    st.subheader("Speed over Time")
    st.line_chart(df[["timestamp", "speed_kph"]].set_index("timestamp"))
