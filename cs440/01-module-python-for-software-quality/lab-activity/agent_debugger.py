import subprocess
import os
import sys
import re

SRC_SCRIPT = "system_utilities.py"
HEALED_SCRIPT = "system_utilities_healed.py"
REPORT_FILE = "debugging_report.md"

if not os.path.exists(SRC_SCRIPT):
    print(f"[-] Error: '{SRC_SCRIPT}' not found.")
    sys.exit(1)

print(f"[+] Multi-Fault Orchestrator active. Seeding staging target from '{SRC_SCRIPT}'...")

# Step 1: Read the immutable baseline and initialize the staging file
with open(SRC_SCRIPT, "r", encoding="utf-8") as f:
    baseline_source = f.read()

with open(HEALED_SCRIPT, "w", encoding="utf-8") as f:
    f.write(baseline_source)

traceback_summary = ""
patched_code_display = []

# Step 2: Loop up to 5 iterations executing and refining the STAGING file
for iteration in range(5):
    with open(HEALED_SCRIPT, "r", encoding="utf-8") as f:
        script_source = f.read()

    # Execute the staging build asset
    run_check = subprocess.run(["python", HEALED_SCRIPT], capture_output=True, text=True)
    
    # Break early if the staging file runs flawlessly
    if run_check.returncode == 0:
        print(f"[+] Quality Loop complete: Staging script executed cleanly on Pass #{iteration+1}.")
        break
        
    error_msg = run_check.stderr
    traceback_summary += f"\n--- Error Trapped on Pass #{iteration+1} ---\n{error_msg}"
    
    # Triage and route based on the staging execution error stream
    if "print(items[i" in error_msg or "line 4" in error_msg:
        print("[*] Triage: Fixing print statement syntax cutoff signature...")
        script_source = script_source.replace("print(items[i", "print(items[i])")
        patched_code_display.append("Fixed print statement bracket cutoff error.")
        
    elif "radus" in error_msg or "NameError" in error_msg:
        print("[*] Triage: Resolving variable NameError typo...")
        script_source = script_source.replace("radus", "radius")
        patched_code_display.append("Corrected 'radus' variable name typo to 'radius'.")
        
    elif "ZeroDivisionError" in error_msg:
        print("[*] Triage: Injecting mathematical zero-division guard...")
        defensive_fix = "if b == 0:\n        return 0.0\n    return a / b"
        script_source = script_source.replace("return a / b", defensive_fix)
        patched_code_display.append("Injected runtime safety check guard for zero-division risk.")
        
    elif "if name =" in error_msg or "check_name" in error_msg:
        print("[*] Triage: Correcting comparison token assignment mismatch...")
        script_source = re.sub(r"if\s+name\s*=\s*(['\"]{2})", r"if name == \1", script_source)
        patched_code_display.append("Swapped variable assignment token '=' with equality operator '=='.")
        
    else:
        print("[-] Unmapped error signature encountered. Exiting self-healing loop.")
        break

    # Save modifications back into the staging file buffer
    with open(HEALED_SCRIPT, "w", encoding="utf-8") as f:
        f.write(script_source)

# Step 3: Write out the pipeline telemetry report
diff_summary = "\n".join([f"- {item}" for item in patched_code_display]) if patched_code_display else "- No modifications needed."
with open(REPORT_FILE, "w", encoding="utf-8") as report_file:
    report_file.write(
        f"# SQA Standalone Script Fault Isolation Report\n\n"
        f"## Target File Audited\n`{SRC_SCRIPT}`\n\n"
        f"## Captured Multi-Fault Execution Tracebacks\n```text\n{traceback_summary.strip()}\n```\n\n"
        f"## Programmatic Self-Healing Diffs Applied\n{diff_summary}\n"
    )
print(f"[+] Telemetry report tracking file '{REPORT_FILE}' written successfully.")