import random
import time
import json
import requests

def generate_ev_data(vehicle_id):
    return {
        "vehicle_id": vehicle_id,
        "timestamp": time.time(),
        "battery_level": round(random.uniform(20.0, 100.0), 2),
        "speed_kph": round(random.uniform(0, 120), 1),
        "temperature_c": round(random.uniform(15, 40), 1),
        "latitude": round(random.uniform(34.0, 38.0), 6),
        "longitude": round(random.uniform(-122.0, -118.0), 6)
    }

URL = "http://localhost:8000/ingest"

if __name__ == "__main__":
    while True:
        data = generate_ev_data("EV-001")
        print("Sending:", data)
        try:
            res = requests.post(URL, json=data)
            print("Status:", res.status_code)
        except Exception as e:
            print("Error:", e)
        time.sleep(3)
