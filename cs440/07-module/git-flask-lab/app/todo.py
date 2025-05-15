from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version="1.0", title="To-Do API", description="Manage simple tasks", doc="/docs")

ns = api.namespace("tasks", description="Task operations")

tasks = {}

task_model = api.model("Task", {
    "id": fields.String(required=True, description="Task ID"),
    "description": fields.String(required=True, description="Task description"),
    "due_date": fields.String(require d=False, description="Due date (YYYY-MM-DD)")
})

@ns.route("/")
class TaskList(Resource):
    @ns.doc("list_tasks")
    def get(self):
        """List all tasks"""
        return tasks

    @ns.doc("add_task")
    @ns.expect(task_model)
    def post(self):
        """Add a new task"""
        data = api.payload
        task_id = data["id"]
        tasks[task_id] = {
            "description": data["description"],
            "due_date": data.get("due_date")
        }
        return {"message": "Task added"}, 201

@ns.route("/<string:id>")
@ns.response(404, "Task not found")
@ns.param("id", "The task ID")
class Task(Resource):
    @ns.doc("delete_task")
    def delete(self, id):
        """Delete a task by ID"""
        if id in tasks:
            del tasks[id]
            return {"message": "Task deleted"}
        api.abort(404, "Task not found")
