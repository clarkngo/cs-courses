from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import json
import os

app = Flask(__name__)

BUGS_FILE = 'data/bugs.json'

# Load bugs from JSON
def load_bugs():
    if os.path.exists(BUGS_FILE):
        with open(BUGS_FILE, 'r') as f:
            return json.load(f)
    return []

# Save bugs to JSON
def save_bugs(bugs):
    with open(BUGS_FILE, 'w') as f:
        json.dump(bugs, f, indent=4)

@app.route("/")
def index():
    bugs = load_bugs()
    return render_template("index.html", bugs=bugs)

from werkzeug.utils import secure_filename

app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/add", methods=["POST"])
def add_bug():
    bugs = load_bugs()

    # Handle file upload
    file = request.files.get("screenshot")
    filename = None
    if file and file.filename:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    new_bug = {
        "id": len(bugs) + 1,
        "title": request.form.get("title"),
        "description": request.form.get("description"),
        "priority": request.form.get("priority"),
        "type": request.form.get("type"),
        "audit_standard": request.form.get("audit_standard"),
        "corrective_action": request.form.get("corrective_action"),
        "status": "Open",
        "screenshot": f"{app.config['UPLOAD_FOLDER']}/{filename}" if filename else ""
    }

    bugs.append(new_bug)
    save_bugs(bugs)
    return redirect(url_for("index"))

@app.route("/resolve/<int:bug_id>")
def resolve_bug(bug_id):
    bugs = load_bugs()
    for bug in bugs:
        if bug["id"] == bug_id:
            bug["status"] = "Closed"
    save_bugs(bugs)
    return redirect(url_for("index"))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    os.makedirs('data', exist_ok=True)
    if not os.path.exists(BUGS_FILE):
        with open(BUGS_FILE, 'w') as f:
            json.dump([], f)
    app.run(debug=True, port=5001)
