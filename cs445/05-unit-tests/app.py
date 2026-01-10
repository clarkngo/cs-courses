from flask import Flask, request, jsonify

app = Flask(__name__)
database = {}

@app.route("/")  
def index():  
 return "Hello World!"

@app.route('/students', methods=['POST'])
def post_students_details():
    try:
        data = request.get_json() 
        
        if not data or "name" not in data or "age" not in data:
            return jsonify({'message': 'Bad Request: Name and Age are required'}), 400
        
        database[data["name"]] = data["age"]
        
        return jsonify({'message': 'Student added successfully'}), 201
        
    except Exception as e:
        return jsonify({'message': f'Error saving object: {str(e)}'}), 500

@app.route('/students/<Student_name>', methods=['GET'])
def get_students_details(Student_name):
    age = database.get(Student_name)
    
    if age is None:
        return jsonify({'message': 'Record Not Found'}), 404
    
    return jsonify({
        'name': Student_name,
        'age': age,
        'message': 'Record Found'
    }), 200

@app.route('/students', methods=['PUT'])
def put_students_details():
    try:
        data = request.get_json()
        
        if not data or "name" not in data or "age" not in data:
            return jsonify({'message': 'Bad Request: Name and Age are required'}), 400

        if data["name"] not in database:
             return jsonify({'message': 'Student not found, cannot update'}), 404

        database[data["name"]] = data["age"]
        return jsonify({'message': 'Student updated successfully'}), 200
        
    except Exception as e:
        return jsonify({'message': f'Error updating object: {str(e)}'}), 500

@app.route('/students/<Student_name>', methods=['DELETE'])
def delete_students_details(Student_name):
    result = database.pop(Student_name, None)
    
    if result is None:
        return jsonify({'message': 'Record Not Found'}), 404
        
    return jsonify({'message': 'Record deleted successfully'}), 200