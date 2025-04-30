from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    # BUG: allows blank entries
    tasks.append({"task": task, "status": "1"})  # BUG: "1" instead of "Pending"
    return redirect("/")

# TODO: No delete functionality
# TODO: No validation
# TODO: No status toggle

if __name__ == "__main__":
    app.run(debug=True, port=5001)
