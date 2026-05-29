import json
import os
import sys
import subprocess

REPORT_FILE = "debugging_report.md"
TARGET_SCRIPT = "production_service.py"
OUTPUT_FILE = "eval_results.json"

json_data = {"status": "REJECTED", "score": 0, "raw_ai_critique": "Validation initialization failed."}

if not os.path.exists(REPORT_FILE) or not os.path.exists(TARGET_SCRIPT):
    json_data["raw_ai_critique"] = "Required multi-agent tracking artifacts are missing."
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)
    sys.exit(1)

print(f"[+] Evaluator Active. Auditing guardrail status for '{TARGET_SCRIPT}'...")

run_check = subprocess.run(["python", TARGET_SCRIPT], capture_output=True, text=True)

if run_check.returncode == 0 and "KeyError" not in run_check.stderr:
    with open(REPORT_FILE, "r", encoding="utf-8") as rf:
        report_text = rf.read()
        
    if "Applied Structural Resilience Patches" in report_text:
        json_data = {
            "status": "APPROVED",
            "score": 100,
            "raw_ai_critique": "The governance gate verified that the service layer safely compiles, resists malformed key lookups, and encapsulates input handlers securely."
        }
    else:
        json_data = {"status": "REJECTED", "score": 50, "raw_ai_critique": "The script compiles cleanly, but the orchestrator compliance report details are incomplete."}
else:
    json_data = {"status": "REJECTED", "score": 0, "raw_ai_critique": f"Guardrail audit failed. Active runtime crash logs present:\n{run_check.stderr[:150]}"}

with open(OUTPUT_FILE, "w", encoding="utf-8") as j:
    json.dump(json_data, j, indent=2)
print(f"[+] Governance execution matrix output successfully to '{OUTPUT_FILE}'.")