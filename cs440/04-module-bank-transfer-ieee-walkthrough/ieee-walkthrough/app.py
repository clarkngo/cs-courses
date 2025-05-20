
from flask import Flask, render_template, request, redirect
import json, os
from datetime import datetime, date

app = Flask(__name__)
FEEDBACK_FILE = "data/feedback.json"
MODULE_FILE = "data/module_info.txt"

def load_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        return []
    with open(FEEDBACK_FILE, "r") as f:
        return json.load(f)

def save_feedback(entry):
    data = load_feedback()
    data.append(entry)
    with open(FEEDBACK_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")
def index():
    with open(MODULE_FILE, "r") as f:
        module_info = f.read()
    feedback = load_feedback()
    return render_template("index.html", module_info=module_info, feedback=feedback, today=date.today().isoformat())

@app.route("/feedback", methods=["POST"])
def feedback():
    form = request.form
    comment = f'''
Project: {(form.get("project_name")) or "N/A"}
Module: {(form.get("module_reviewed")) or "N/A"}
Author:{(form.get("author")) or "Unknown"}
Date: {(form.get("walkthrough_date")) or date.today().isoformat()}

Participants:
- Reviewer 1: {(form.get("reviewer1")) or "None"}
- Reviewer 2: {(form.get("reviewer2")) or "None"}

Objectives: {", ".join(form.getlist("objectives")) or "None provided"}

Summary:
{(form.get("summary")) or "No summary provided."}

Reviewer Questions:
- Q1: {(form.get("question1")) or "None"}
- Q2: {(form.get("question2")) or "None"}

Action Items:
- [ ] {(form.get("action1")) or "No next steps specified"}
- [ ] {(form.get("action2")) or "No next steps specified"}

Next Steps: {", ".join(form.getlist("next_steps")) or "No next steps specified"}
'''
    reviewer = form.get("reviewer")
    save_feedback({"reviewer": reviewer, "comment": comment})
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)
