import subprocess
import os
import sys
import re

TARGET_SCRIPT = "system_utilities.py"
REPORT_FILE = "debugging_report.md"

if not os.path.exists(TARGET_SCRIPT):
    print(f"[-] Error: '{TARGET_SCRIPT}' not found.")
    sys.exit(1)

print(f"[+] Multi-Fault Orchestrator active. Debugging '{TARGET_SCRIPT}'...")

traceback_summary = ""
patched_code_display = []

# Loop up to 5 iterations to catch and resolve sequential faults dynamically
for iteration in range(5):
    # Always read a fresh copy of the code from disk at the start of the pass
    with open(TARGET_SCRIPT, "r", encoding="utf-8") as f:
        script_source = f.read()

    run_check = subprocess.run(["python", TARGET_SCRIPT], capture_output=True, text=True)
    
    # If the script executes perfectly with 0 faults, break out of the self-healing loop
    if run_check.returncode == 0:
        print(f"[+] Quality Loop complete: Script executed cleanly on Pass #{iteration+1}.")
        break
        
    error_msg = run_check.stderr
    traceback_summary += f"\n--- Error Trapped on Pass #{iteration+1} ---\n{error_msg}"
    
    # TRIAGE AND ROUTE BASED EXCLUSIVELY ON THE ACTIVE COMPILER ERROR MESSAGE
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

    # Save the current pass updates back to disk immediately
    with open(TARGET_SCRIPT, "w", encoding="utf-8") as f:
        f.write(script_source)

# Generate the artifact report file
diff_summary = "\n".join([f"- {item}" for item in patched_code_display]) if patched_code_display else "- No modifications needed."
with open(REPORT_FILE, "w", encoding="utf-8") as report_file:
    report_file.write(
        f"# SQA Standalone Script Fault Isolation Report\n\n"
        f"## Target File Audited\n`{TARGET_SCRIPT}`\n\n"
        f"## Captured Multi-Fault Execution Tracebacks\n```text\n{traceback_summary.strip()}\n```\n\n"
        f"## Programmatic Self-Healing Diffs Applied\n{diff_summary}\n"
    )
print(f"[+] Telemetry report tracking file '{REPORT_FILE}' written successfully.")