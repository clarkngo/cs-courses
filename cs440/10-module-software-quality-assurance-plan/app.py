from flask import Flask, render_template, request, redirect
import json
from pathlib import Path

app = Flask(__name__)
DATA_FILE = Path("submissions.json")
SCENARIO_FILE = Path("scenario.json")

@app.route("/")
def index():
    with open(SCENARIO_FILE) as f:
        scenario = json.load(f)
    return render_template("index.html", scenario=scenario)

@app.route("/submit", methods=["POST"])
def submit():
    submission = {
        "title": request.form["title"],
        "description": request.form["description"],
        "objectives": request.form["objectives"],
        "roles": request.form["roles"],
        "standards": request.form["standards"],
        "test_plan": request.form["test_plan"]
    }

    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(submission)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
