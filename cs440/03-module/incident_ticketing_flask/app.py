
from flask import Flask, render_template, request, redirect
from src.incident import Incident

app = Flask(__name__)
tickets = [
    Incident("Email not syncing", "Alice"),
    Incident("VPN connection fails", "Bob"),
    Incident("Printer not working", "Charlie"),
]
tickets[0].assign("IT Support 1")
tickets[0].resolve()
tickets[1].assign("IT Support 2")

@app.route("/")
def index():
    return render_template("index.html", tickets=tickets)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        reporter = request.form["reporter"]
        ticket = Incident(title, reporter)
        tickets.append(ticket)
        return redirect("/")
    return render_template("create.html")

@app.route("/resolve/<ticket_id>")
def resolve(ticket_id):
    for ticket in tickets:
        if ticket.id == ticket_id:
            ticket.resolve()
            break
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
