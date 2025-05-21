"""
Flask KPI and Risk Management API

This application provides API endpoints for retrieving, adding, and managing KPIs (Key Performance Indicators), KPI targets, and risk-related data in JSON format. It is designed to support dashboards or feedback platforms for performance monitoring in an organizational or project setting.

Modules:
- Flask: Web framework for API routing
- flask_cors: Handles Cross-Origin Resource Sharing
- json, os: File handling for reading/writing JSON data

Routes:
-------

GET /api/kpi
    Returns the current KPI data from `kpis.json`.

GET /api/kpi_targets
    Returns the KPI target values from `kpi_targets.json`.

GET /api/risks
    Retrieves the list of submitted risks from `risks.json`.

POST /api/risks
    Adds a new risk entry to `risks.json` and removes the matching item (by ID) from `predefined_risks.json`.

GET /api/predefined_risks
    Returns predefined risks from `predefined_risks.json`, or an empty list if the file doesn't exist.

POST /api/feedback-submission
    Accepts metric feedback and appends it to `feedback.json`.

Helper Functions:
-----------------

read_json(file: str) -> dict | list
    Reads and parses JSON data from the specified file.

write_json(file: str, data: dict | list)
    Writes JSON data to the specified file with pretty formatting.

Usage:
------
Run the app using:

    python app.py

Make sure the `./data` directory exists and contains the necessary JSON files:

    - kpis.json
    - kpi_targets.json
    - risks.json
    - predefined_risks.json
    - feedback.json (optional; will be created on first POST)

"""


from flask import Flask, jsonify, request
from flask_cors import CORS
import json, os

app = Flask(__name__)
CORS(app)

DATA_DIR = './data'
KPI_FILE = os.path.join(DATA_DIR, 'kpis.json')
KPI_TARGETS_FILE = os.path.join(DATA_DIR, 'kpi_targets.json')
RISK_FILE = os.path.join(DATA_DIR, 'risks.json')

def read_json(file):
    with open(file, 'r') as f:
        return json.load(f)

def write_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/api/kpi')
def get_kpis():
    return jsonify(read_json(KPI_FILE))

@app.route('/api/kpi_targets')
def get_targets():
    return jsonify(read_json(KPI_TARGETS_FILE))

@app.route('/api/risks')
def get_risks():
    return jsonify(read_json(RISK_FILE))

@app.route('/api/risks', methods=['POST'])
def add_risk():
    new_risk = request.get_json()
    risk_file = './data/risks.json'
    predefined_file = './data/predefined_risks.json'

    # Append to risks.json
    risks = []
    if os.path.exists(risk_file):
        with open(risk_file) as f:
            risks = json.load(f)
    risks.append(new_risk)
    with open(risk_file, 'w') as f:
        json.dump(risks, f, indent=2)

    # Remove from predefined_risks.json
    if os.path.exists(predefined_file):
        with open(predefined_file) as f:
            predefined = json.load(f)
        predefined = [r for r in predefined if r.get('id') != new_risk.get('id')]
        with open(predefined_file, 'w') as f:
            json.dump(predefined, f, indent=2)

    return jsonify(new_risk), 201


@app.route('/api/feedback-submission', methods=['POST'])
def save_metric_feedback():
    feedback = request.get_json()
    filepath = './data/feedback.json'
    if os.path.exists(filepath):
        with open(filepath) as f:
            all_feedback = json.load(f)
    else:
        all_feedback = []

    all_feedback.append(feedback)
    with open(filepath, 'w') as f:
        json.dump(all_feedback, f, indent=2)
    return jsonify({"status": "saved"}), 201


@app.route('/api/predefined_risks', methods=['GET'])
def get_predefined_risks():
    filepath = './data/predefined_risks.json'
    if not os.path.exists(filepath):
        return jsonify([])  # Return empty list if the file doesn't exist
    with open(filepath) as f:
        risks = json.load(f)
    return jsonify(risks)

if __name__ == '__main__':
    app.run(debug=True)
