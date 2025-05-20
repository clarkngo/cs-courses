from flask import Flask, render_template, request, redirect, url_for
import os, json

app = Flask(__name__)
TASKS_FILE = 'data/tasks.json'

os.makedirs('data', exist_ok=True)
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as f:
        json.dump([], f)

def load_tasks():
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("task", "").strip()
    if not title:
        return redirect(url_for("index"))

    tasks = load_tasks()
    tasks.append({
        "id": len(tasks) + 1,
        "task": title,
        "status": "Pending"
    })
    save_tasks(tasks)
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Done"
    save_tasks(tasks)
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=5002)
