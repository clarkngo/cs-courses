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
    filepath = './data/risks.json'
    if os.path.exists(filepath):
        with open(filepath) as f:
            risks = json.load(f)
    else:
        risks = []
    risks.append(new_risk)
    with open(filepath, 'w') as f:
        json.dump(risks, f, indent=2)
    return jsonify(new_risk), 201


@app.route('/api/metric-submission', methods=['POST'])
def save_metric_feedback():
    feedback = request.get_json()
    filepath = './data/metric_feedback.json'
    if os.path.exists(filepath):
        with open(filepath) as f:
            all_feedback = json.load(f)
    else:
        all_feedback = []

    all_feedback.append(feedback)
    with open(filepath, 'w') as f:
        json.dump(all_feedback, f, indent=2)
    return jsonify({"status": "saved"}), 201

if __name__ == '__main__':
    app.run(debug=True)
