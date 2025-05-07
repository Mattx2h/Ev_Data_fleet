# EV Fleet Data Analyzer

This project simulates an electric vehicle (EV) fleet data ingestion and analytics pipeline, inspired by real-world IoT systems like Tesla’s.

## 🚗 Features:
- Real-time data simulation (battery %, speed, location)
- RESTful API using FastAPI for data ingestion and summary
- SQLite database for storage
- Streamlit dashboard to visualize metrics (battery trends, speed over time)

## 🛠 Tech Stack:
- Python, FastAPI, Streamlit, SQLite, Pandas, NumPy

## 🧪 How to Run:

1. Start the API server:
```
uvicorn api.main:app --reload
```

2. Start the data simulator:
```
python data_generator/simulate_ev_data.py
```

3. Run the dashboard:
```
streamlit run analytics/dashboard.py
```
