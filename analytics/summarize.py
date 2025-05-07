import sqlite3
import pandas as pd

def summarize_ev_data():
    conn = sqlite3.connect("ev_data.db")
    df = pd.read_sql_query("SELECT * FROM ev_data", conn)

    if df.empty:
        return {"message": "No data yet"}

    summary = {
        "total_records": len(df),
        "average_battery_level": round(df["battery_level"].mean(), 2),
        "average_speed_kph": round(df["speed_kph"].mean(), 2),
        "lowest_battery_vehicle": df.loc[df["battery_level"].idxmin()]["vehicle_id"],
        "highest_speed": df["speed_kph"].max()
    }
    return summary
