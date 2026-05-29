import json
import os
import sys
import subprocess
import glob

REPORT_FILE = "debugging_report.md"
OUTPUT_FILE = "eval_results.json"
INCIDENTS_JSON = "incidents.json"
TRIAGE_MD = "triage_summary.md"

json_data = {"status": "REJECTED", "score": 0, "raw_ai_critique": "Validation initialization failed."}

print("[+] Independent Governance Gate active. Scanning for staging artifacts...")
healed_files = glob.glob("*_healed.py")

if not healed_files:
    json_data["raw_ai_critique"] = "Missing required staging artifact: No '*_healed.py' file found."
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f: json.dump(json_data, f, indent=2)
    sys.exit(1)

target_script = healed_files[0]

if not os.path.exists(REPORT_FILE):
    json_data["raw_ai_critique"] = f"Missing compliance telemetry: '{REPORT_FILE}' not found."
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f: json.dump(json_data, f, indent=2)
    sys.exit(1)

# Step 1: Execution validation gate run
run_check = subprocess.run(["python", target_script], capture_output=True, text=True)

if run_check.returncode == 0 and os.path.exists(INCIDENTS_JSON) and os.path.exists(TRIAGE_MD):
    # Step 2: Validate generated ITIL downstream data compliance tokens
    with open(INCIDENTS_JSON, "r", encoding="utf-8") as jf:
        incident_metrics = json.load(jf)
        
    with open(TRIAGE_MD, "r", encoding="utf-8") as mf:
        triage_text = mf.read()
        
    with open(REPORT_FILE, "r", encoding="utf-8") as rf:
        report_text = rf.read()

    # ITIL Governance Constraints Verification
    is_database_category = incident_metrics.get("category") == "Database"
    is_critical_severity = incident_metrics.get("severity") == "CRITICAL"
    is_assigned_correctly = "Data Engineering" in triage_text
    is_report_valid = "Report" in report_text and "Audited" in report_text

    if is_database_category and is_critical_severity and is_assigned_correctly and is_report_valid:
        json_data = {
            "status": "APPROVED",
            "score": 100,
            "raw_ai_critique": f"Governance check passed. The script compiled cleanly, mapped the database exception to 'CRITICAL' severity, and routed the ticket to the Data Engineering domain under ITIL parameters."
        }
    else:
        json_data = {
            "status": "REJECTED",
            "score": 50,
            "raw_ai_critique": "The pipeline runs, but the generated incident artifacts failed ITIL compliance classification standards."
        }
else:
    json_data = {
        "status": "REJECTED",
        "score": 0,
        "raw_ai_critique": f"Artifact validation gate execution failed. System traceback:\n{run_check.stderr[:150]}"
    }

with open(OUTPUT_FILE, "w", encoding="utf-8") as j: json.dump(json_data, j, indent=2)
print(f"[+] Governance execution matrix output successfully to '{OUTPUT_FILE}'.")