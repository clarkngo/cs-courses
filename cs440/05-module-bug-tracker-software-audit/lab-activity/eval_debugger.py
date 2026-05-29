import json
import os
import sys
import subprocess
import glob

REPORT_FILE = "debugging_report.md"
OUTPUT_FILE = "eval_results.json"

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

# Execution evaluation gate run
run_check = subprocess.run(["python", target_script], capture_output=True, text=True)

# Broad validation check for clean execution (Exit 0) and zero active runtime error traces
has_runtime_crash = (
    run_check.returncode != 0 or 
    "Traceback" in run_check.stderr or 
    "AuditViolation" in run_check.stderr or
    "ValueError" in run_check.stderr or
    "TypeError" in run_check.stderr
)

if not has_runtime_crash:
    with open(REPORT_FILE, "r", encoding="utf-8") as rf:
        report_text = rf.read()
        
    is_report_valid = "Report" in report_text and "Audited" in report_text

    if is_report_valid:
        json_data = {
            "status": "APPROVED",
            "score": 100,
            "raw_ai_critique": f"The verification gate successfully certified '{target_script}'. The script compiled cleanly (Exit 0) and the orchestration report passed structural process compliance."
        }
    else:
        json_data = {
            "status": "REJECTED",
            "score": 50,
            "raw_ai_critique": "The healed staging script executes cleanly, but the companion markdown report layout failed structural auditing criteria."
        }
else:
    clipped_error = run_check.stderr.strip()[:150] if run_check.stderr else "Runtime compilation verification check failed."
    json_data = {
        "status": "REJECTED",
        "score": 0,
        "raw_ai_critique": f"Staging artifact execution gate check failed. Live crash log output:\n{clipped_error}"
    }

with open(OUTPUT_FILE, "w", encoding="utf-8") as j: json.dump(json_data, j, indent=2)
print(f"[+] Governance evaluation complete. Results written cleanly to '{OUTPUT_FILE}'.")