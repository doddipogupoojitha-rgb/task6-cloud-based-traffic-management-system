# Task 6 - Cloud-Based Traffic Management System 🚦

Real-time traffic analytics system with ingestion, processing, and dashboards.

## Features
- Real-time vehicle count simulation (5 Hyderabad Junctions)
- Congestion Detection: Low/Medium/High
- Signal Control Logic
- Live Dashboard with Total Vehicles, Avg Speed
- REST APIs: /api/traffic, /api/stats
- Auto-refresh every 5 seconds

## Tech Stack
- Python Flask
- Simulated IoT Streams (mock)
- Cloud Ready (Gunicorn)
- HTML/CSS Dashboard

## Run Locally
pip install -r requirements.txt
python app.py

## APIs
- / - Home Live View
- /dashboard - Analytics Dashboard
- /api/traffic - JSON data
