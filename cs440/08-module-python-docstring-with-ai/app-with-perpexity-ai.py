"""
Flask API for KPI, Risk, and Feedback Management

This application provides a RESTful API for managing Key Performance Indicators (KPIs), KPI targets, risks, predefined risks, and user feedback. 
It is designed to support a dashboard or management system that needs to store, retrieve, and update these datasets in JSON format.

Endpoints:
----------
- GET /api/kpi
    Returns the list of KPIs from `kpis.json`.

- GET /api/kpi_targets
    Returns the list of KPI targets from `kpi_targets.json`.

- GET /api/risks
    Returns the list of risks from `risks.json`.

- POST /api/risks
    Adds a new risk to `risks.json` and removes it from `predefined_risks.json` if present.
    Expects a JSON object representing the new risk in the request body.

- GET /api/predefined_risks
    Returns the list of predefined risks from `predefined_risks.json`.

- POST /api/feedback-submission
    Submits user feedback related to metrics and appends it to `feedback.json`.
    Expects a JSON object representing the feedback in the request body.

Data Storage:
-------------
All data is stored in the `./data` directory as JSON files:
- kpis.json: List of KPIs
- kpi_targets.json: List of KPI targets
- risks.json: List of risks
- predefined_risks.json: List of predefined risks
- feedback.json: List of user feedback submissions

CORS:
-----
Cross-Origin Resource Sharing (CORS) is enabled for all routes to allow requests from different origins.

Usage:
------
Run the app with:
    python <filename>.py

The app will start a development server on http://localhost:5000.

Dependencies:
-------------
- Flask
- flask_cors
- json
- os

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
