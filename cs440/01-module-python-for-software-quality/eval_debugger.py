import json
import os
import sys
import subprocess
import glob

REPORT_FILE = "debugging_report.md"
OUTPUT_FILE = "eval_results.json"

# Default fallback failure state
json_data = {
    "status": "REJECTED",
    "score": 0,
    "raw_ai_critique": "Validation initialization failed."
}

print("[+] Independent Governance Gate active. Scanning for staging artifacts...")

# 1. Dynamic Discovery: Find any file ending in '_healed.py'
healed_files = glob.glob("*_healed.py")

if not healed_files:
    json_data["raw_ai_critique"] = "Missing required staging artifact: No '*_healed.py' file found."
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)
    print("[-] Evaluation aborted: No staging target found.")
    sys.exit(1)

# Select the discovered healed script target
target_script = healed_files[0]
print(f"[+] Target artifact identified: '{target_script}'")

# 2. Verify existence of the companion compliance markdown report
if not os.path.exists(REPORT_FILE):
    json_data["raw_ai_critique"] = f"Missing compliance telemetry: '{REPORT_FILE}' not found."
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)
    print("[-] Evaluation aborted: Missing report file.")
    sys.exit(1)

# 3. Execution Gate: Run the staging artifact programmatically
run_check = subprocess.run(["python", target_script], capture_output=True, text=True)

# Define common crash signatures to ensure true runtime safety
has_runtime_crash = (
    run_check.returncode != 0 or 
    "Traceback" in run_check.stderr or 
    "KeyError" in run_check.stderr or 
    "NameError" in run_check.stderr
)

if not has_runtime_crash:
    # 4. Semantic Report Audit
    with open(REPORT_FILE, "r", encoding="utf-8") as rf:
        report_text = rf.read()
        
    # Check for general compliance headers present in both lab manual specs
    if "Report" in report_text and "Audited" in report_text:
        json_data = {
            "status": "APPROVED",
            "score": 100,
            "raw_ai_critique": f"The verification gate successfully validated '{target_script}'. The script compiled cleanly (Exit 0) and the orchestration report passed structural compliance."
        }
    else:
        json_data = {
            "status": "REJECTED",
            "score": 50,
            "raw_ai_critique": "The healed script executes cleanly, but the companion markdown report layout failed structural auditing criteria."
        }
else:
    # Capture the first 150 characters of the stderr crash buffer for student feedback
    clipped_error = run_check.stderr.strip()[:150] if run_check.stderr else "Unknown runtime exception encountered."
    json_data = {
        "status": "REJECTED",
        "score": 0,
        "raw_ai_critique": f"Staging artifact execution gate check failed. Live crash exception captured:\n{clipped_error}"
    }

# 5. Output standardized JSON metrics
with open(OUTPUT_FILE, "w", encoding="utf-8") as j:
    json.dump(json_data, j, indent=2)

print(f"[+] Governance evaluation complete. Results written cleanly to '{OUTPUT_FILE}'.")