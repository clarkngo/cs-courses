import json
import os
import sys
import subprocess

REPORT_FILE = "debugging_report.md"
TARGET_SCRIPT = "system_utilities.py"
OUTPUT_FILE = "eval_results.json"

json_data = {"status": "REJECTED", "score": 0, "raw_ai_critique": "Validation initialization failed."}

if not os.path.exists(REPORT_FILE) or not os.path.exists(TARGET_SCRIPT):
    json_data["raw_ai_critique"] = "Missing required execution metrics."
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)
    sys.exit(1)

print(f"[+] Evaluator Active. Validating standalone execution safety for '{TARGET_SCRIPT}'...")

# Programmatically run the script to confirm the errors are resolved
run_check = subprocess.run(["python", TARGET_SCRIPT], capture_output=True, text=True)

if run_check.returncode == 0:
    with open(REPORT_FILE, "r", encoding="utf-8") as rf:
        report_text = rf.read()
        
    if "## Programmatic Self-Healing Diffs Applied" in report_text:
        json_data = {
            "status": "APPROVED",
            "score": 100,
            "raw_ai_critique": "The structural verification gate confirmed the script executes with 0 faults. Automated self-healing logs match structural standards."
        }
    else:
        json_data = {"status": "REJECTED", "score": 50, "raw_ai_critique": "Code passes execution check, but report layout is missing logs."}
else:
    json_data = {"status": "REJECTED", "score": 0, "raw_ai_critique": f"Script failed execution gate check. Crash traceback:\n{run_check.stderr[:150]}"}

with open(OUTPUT_FILE, "w", encoding="utf-8") as j:
    json.dump(json_data, j, indent=2)
print(f"[+] Evaluation matrix written cleanly to '{OUTPUT_FILE}'.")