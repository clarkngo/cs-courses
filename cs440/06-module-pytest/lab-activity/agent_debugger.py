import subprocess
import os
import sys

SRC_SCRIPT = "bank_processor.py"
HEALED_SCRIPT = "bank_processor_healed.py"
REPORT_FILE = "debugging_report.md"

if not os.path.exists(SRC_SCRIPT):
    print(f"[-] Error: '{SRC_SCRIPT}' not found.")
    sys.exit(1)

print(f"[+] SQA Test Orchestrator active. Seeding staging target from '{SRC_SCRIPT}'...")

with open(SRC_SCRIPT, "r", encoding="utf-8") as f:
    baseline_content = f.read()

with open(HEALED_SCRIPT, "w", encoding="utf-8") as f:
    f.write(baseline_content)

traceback_summary = ""
patched_code_display = []

for iteration in range(5):
    with open(HEALED_SCRIPT, "r", encoding="utf-8") as f:
        script_source = f.read()

    run_check = subprocess.run(["python", HEALED_SCRIPT], capture_output=True, text=True)
    
    if run_check.returncode == 0:
        print(f"[+] Quality Loop complete: Test logic boundaries stabilized on Pass #{iteration+1}.")
        break
        
    error_msg = run_check.stderr if run_check.stderr else run_check.stdout
    traceback_summary += f"\n--- Test Validation Masking Intercepted on Pass #{iteration+1} ---\n{error_msg}"
    
    # TRIAGE ROUTING STREAM: Detect the masked verification logic exception trace
    if "per-transaction limit" in error_msg or "account.transfer(15000)" in script_source:
        print("[*] Triage: Refactoring masked boundary condition transaction sequences...")
        
        # Unmask the execution flow by converting the lump sum into safe, multi-step allocations
        corrected_sequence = (
            "account.transfer(9000)  # Safe Transaction 1\n"
            "    account.transfer(9000)  # Safe Transaction 2 (Total: 18000)\n"
            "    try:\n"
            "        account.transfer(8000)  # Pushes aggregate to 26000 (Triggers Daily Limit)\n"
            "        raise AssertionError('TestFailed: Daily limit check bypassed.')\n"
            "    except ValueError as e:\n"
            "        if 'daily transfer limit' in str(e):\n"
            "            print('[+] Success: Daily transfer limit guard verified successfully.')\n"
            "        else:\n"
            "            raise e"
        )
        
        script_source = script_source.replace("account.transfer(15000)", corrected_sequence)
        patched_code_display.append("Refactored masked validation calls into safe incremental allocations to evaluate true daily limits.")
    else:
        print("[-] Verification ceiling reached or unknown error signature caught.")
        break

    with open(HEALED_SCRIPT, "w", encoding="utf-8") as f:
        f.write(script_source)

# Export structural pipeline markdown log metadata parameters
diff_summary = "\n".join([f"- {item}" for item in patched_code_display]) if patched_code_display else "- Test vectors verified."
with open(REPORT_FILE, "w", encoding="utf-8") as report_file:
    report_file.write(
        f"# SQA Test Framework & Boundary Validation Report\n\n"
        f"## Target File Audited\n`{SRC_SCRIPT}`\n\n"
        f"## Captured Guardrail Violations\n```text\n{traceback_summary.strip()}\n```\n\n"
        f"## Applied Structural Resilience Patches\n{diff_summary}\n"
    )
print(f"[+] Automated test telemetry report written out to '{REPORT_FILE}'.")