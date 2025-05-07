from fastapi import FastAPI, Request
import sqlite3
import time
from analytics.summarize import summarize_ev_data

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running!"}

conn = sqlite3.connect("ev_data.db", check_same_thread=False)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS ev_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id TEXT,
    timestamp REAL,
    battery_level REAL,
    speed_kph REAL,
    temperature_c REAL,
    latitude REAL,
    longitude REAL
)
""")
conn.commit()

@app.post("/ingest")
async def ingest_data(request: Request):
    data = await request.json()
    c.execute("INSERT INTO ev_data (vehicle_id, timestamp, battery_level, speed_kph, temperature_c, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (data["vehicle_id"], data["timestamp"], data["battery_level"],
               data["speed_kph"], data["temperature_c"], data["latitude"], data["longitude"]))
    conn.commit()
    return {"status": "success", "data": data}

@app.get("/summary")
async def get_summary():
    return summarize_ev_data()
