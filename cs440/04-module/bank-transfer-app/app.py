from flask import Flask, render_template, request, redirect
import json, os, random, logging
from datetime import datetime, date
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
TRANSFER_LOG = "data/transfers.json"
ACCOUNTS_FILE = "data/accounts.json"
AUDIT_LOG_JSON = "data/audit_log.json"

# Create a rotating file handler
handler = RotatingFileHandler(
    "data/server.log",     # Log file path
    maxBytes=10 * 1024,    # Max size ~10KB (adjust as needed)
    backupCount=1          # Only keep the latest log file
)

# Set up the root logger to use the rotating handler
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[handler]
)

def load_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        return {}
    with open(ACCOUNTS_FILE, "r") as f:
        return json.load(f)

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(accounts, f, indent=2)

def load_transfers():
    if not os.path.exists(TRANSFER_LOG):
        return []
    with open(TRANSFER_LOG, "r") as f:
        return json.load(f)

def save_transfer(entry):
    data = load_transfers()
    data.append(entry)
    with open(TRANSFER_LOG, "w") as f:
        json.dump(data, f, indent=2)

def append_audit_log(entry, max_entries=20):
    audit_data = []

    if os.path.exists(AUDIT_LOG_JSON):
        with open(AUDIT_LOG_JSON, "r") as f:
            try:
                audit_data = json.load(f)
            except json.JSONDecodeError:
                audit_data = []  # File exists but is empty or corrupt

    audit_data.append(entry)
    audit_data = audit_data[-max_entries:]

    with open(AUDIT_LOG_JSON, "w") as f:
        json.dump(audit_data, f, indent=2)


@app.route("/")
def home():
    accounts = load_accounts()
    logging.info("Visited Home Page")
    return render_template("home.html", transfers=load_transfers(), accounts=accounts, today=date.today().isoformat())

@app.route("/transfer", methods=["GET", "POST"])
def transfer():
    accounts = load_accounts()
    error = None
    if request.method == "POST":
        src = request.form["source"]
        dest = request.form["destination"]
        amount = float(request.form["amount"])
        trans_date = request.form["date"]

        logging.info(f"Transfer request from {src} to {dest} for ${amount} on {trans_date}")

        if random.random() < 0.1:
            error = "Unable to process, please try again"
            logging.warning("Simulated network failure during transfer")
        elif src == dest:
            error = "Source and destination accounts must be different."
            logging.warning("Transfer failed: same source and destination")
        elif src not in accounts:
            error = "Invalid source account."
            logging.error("Invalid source account used")
        elif dest not in accounts:
            error = "Account not found"
            logging.error("Destination account not found")
        elif amount <= 0:
            error = "Amount must be greater than 0."
            logging.warning("Transfer failed: amount <= 0")
        elif accounts[src]["balance"] < amount:
            error = "Insufficient funds"
            logging.warning("Transfer failed: insufficient funds")
        else:
            accounts[src]["balance"] -= amount
            accounts[dest]["balance"] += amount
            save_accounts(accounts)
            entry = {
                "source": src,
                "destination": dest,
                "amount": amount,
                "date": trans_date,
                "submitted": datetime.now().isoformat()
            }
            save_transfer(entry)

            # Log audit to both server.log and audit_log.json (missing IP address)
            audit_entry = {
                "timestamp": entry["submitted"],
                "user_id": src,
                "destination": dest,
                "amount": amount,
                "note": "No IP address recorded"
            }
            append_audit_log(audit_entry)
            logging.info(f"Audit Log Entry: {audit_entry}")
            
            return redirect(f"/confirmation/{src}/{dest}/{amount}/{trans_date}")
    return render_template("transfer.html", accounts=accounts, error=error, today=date.today().isoformat())

@app.route("/confirmation/<source>/<destination>/<amount>/<date>")
def confirmation(source, destination, amount, date):
    accounts = load_accounts()
    transfer = {
        "source": f"{source} - {accounts[source]['name']}",
        "destination": f"{destination} - {accounts[destination]['name']}",
        "amount": float(amount),
        "date": date
    }
    return render_template("confirmation.html", transfer=transfer)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
