"""Student management Flask application."""
import json

from flask import Flask
from flask import request

database = {}
app = Flask(__name__)


@app.route("/")
def index():
    """Return hello world message."""
    return "Hello World!"


@app.route('/students', methods=['POST'])
def post_students_details():
    """Create a new student record."""
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))
        database[dict_json["name"]] = dict_json["age"]
        return 'Success', 200
    except Exception as e:
        print("Error during saving object ", e)
        return 'Failed', 400


@app.route('/students', methods=['PUT'])
def put_students_details():
    """Update an existing student record."""
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))
        database[dict_json["name"]] = dict_json["age"]
        return 'Success', 200
    except Exception as e:
        print("Error during saving object ", e)
        return 'Failed', 400


@app.route('/students/<student_name>', methods=['GET'])
def get_students_details(student_name):
    """Get a student record by name."""
    try:
        name = database[student_name]
        if name is None:
            return 'Record Not Found', 404
        return 'Record Found ' + student_name + ' age is ' + str(name), 200
    except KeyError:
        return 'Record Not Found', 404


@app.route('/students/<student_name>', methods=['DELETE'])
def delete_students_details(student_name):
    """Delete a student record by name."""
    try:
        database.pop(student_name)
        return 'Record deleted successfully', 200
    except KeyError:
        return 'Record Not Found', 404
    except Exception as e:
        print("Error while removing record ", e)
        return 'Error while removing record', 400 
