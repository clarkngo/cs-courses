"""
Risk and KPI Management API

This Flask application provides a RESTful API for managing key performance indicators (KPIs), 
KPI targets, and risk data for a business management dashboard system. It allows retrieving 
KPI data, managing risks, and submitting feedback on metrics.

The API interacts with JSON files stored in a data directory to persist information.
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
    """
    Reads and parses a JSON file.
    
    Args:
        file (str): Path to the JSON file to read.
        
    Returns:
        dict or list: The parsed JSON data.
    """
    with open(file, 'r') as f:
        return json.load(f)

def write_json(file, data):
    """
    Writes data to a JSON file with proper formatting.
    
    Args:
        file (str): Path to the JSON file to write.
        data (dict or list): Data to write to the file.
    """
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/api/kpi')
def get_kpis():
    """
    Retrieves all KPI data.
    
    Returns:
        JSON: A JSON response containing all KPI data.
    """
    return jsonify(read_json(KPI_FILE))

@app.route('/api/kpi_targets')
def get_targets():
    """
    Retrieves all KPI target data.
    
    Returns:
        JSON: A JSON response containing all KPI target data.
    """
    return jsonify(read_json(KPI_TARGETS_FILE))

@app.route('/api/risks')
def get_risks():
    """
    Retrieves all risk data.
    
    Returns:
        JSON: A JSON response containing all risk entries.
    """
    return jsonify(read_json(RISK_FILE))

@app.route('/api/risks', methods=['POST'])
def add_risk():
    """
    Adds a new risk to the risk register and removes it from predefined risks if present.
    
    The function expects a JSON payload representing the risk to be added.
    
    Returns:
        tuple: A JSON response containing the added risk and HTTP status code 201 (Created).
    """
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
    """
    Saves feedback on metrics submitted by users.
    
    The function expects a JSON payload containing the feedback data.
    
    Returns:
        tuple: A JSON response with status "saved" and HTTP status code 201 (Created).
    """
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
    """
    Retrieves all predefined risk templates.
    
    Returns:
        JSON: A JSON response containing all predefined risk templates or an empty list
             if the file doesn't exist.
    """
    filepath = './data/predefined_risks.json'
    if not os.path.exists(filepath):
        return jsonify([])  # Return empty list if the file doesn't exist
    with open(filepath) as f:
        risks = json.load(f)
    return jsonify(risks)

if __name__ == '__main__':
    """
    Run the Flask application in debug mode if this script is executed directly.
    """
    app.run(debug=True)