from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# Mock IoT Traffic Data - 4 Hyderabad Junctions
junctions = [
    {"id":"J1", "name":"MG Road - Abids", "area":"Hyderabad Central", "vehicles": 0, "speed": 0, "congestion": "Low", "signal": "Green"},
    {"id":"J2", "name":"Banjara Hills Rd No.1", "area":"Banjara Hills", "vehicles": 0, "speed": 0, "congestion": "Medium", "signal": "Yellow"},
    {"id":"J3", "name":"Gachibowli Main Signal", "area":"Gachibowli", "vehicles": 0, "speed": 0, "congestion": "High", "signal": "Red"},
    {"id":"J4", "name":"Secunderabad Clock Tower", "area":"Secunderabad", "vehicles": 0, "speed": 0, "congestion": "Low", "signal": "Green"},
    {"id":"J5", "name":"Hitech City Junction", "area":"Hitech City", "vehicles": 0, "speed": 0, "congestion": "Medium", "signal": "Green"},
]

def simulate_traffic():
    for j in junctions:
        j["vehicles"] = random.randint(15, 220)
        j["speed"] = random.randint(10, 65)
        j["timestamp"] = datetime.now().strftime("%H:%M:%S")
        # Logic for congestion
        if j["vehicles"] > 160:
            j["congestion"] = "High"
            j["signal"] = "Red"
            j["action"] = "Divert Traffic - Use Alternate Route"
        elif j["vehicles"] > 90:
            j["congestion"] = "Medium"
            j["signal"] = "Yellow"
            j["action"] = "Monitor Closely"
        else:
            j["congestion"] = "Low"
            j["signal"] = "Green"
            j["action"] = "Flow Normal"

@app.route('/')
def home():
    simulate_traffic()
    return render_template('index.html', junctions=junctions)

@app.route('/dashboard')
def dashboard():
    simulate_traffic()
    total_vehicles = sum(j["vehicles"] for j in junctions)
    avg_speed = sum(j["speed"] for j in junctions) // len(junctions)
    high_congestion = len([j for j in junctions if j["congestion"]=="High"])
    return render_template('dashboard.html', junctions=junctions, total=total_vehicles, avg=avg_speed, high=high_congestion)

@app.route('/api/traffic')
def api_traffic():
    simulate_traffic()
    return jsonify(junctions)

@app.route('/api/stats')
def api_stats():
    simulate_traffic()
    return jsonify({
        "total_vehicles": sum(j["vehicles"] for j in junctions),
        "timestamp": datetime.now().isoformat(),
        "junctions": len(junctions)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
