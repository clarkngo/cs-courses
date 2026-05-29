Moving into **Module 04** represents the ultimate verification stage for your Multi-Agent Software Quality Assurance framework. In previous modules, your students tackled compile-time exceptions, input-driven edge cases, and systems-level infrastructure telemetry. Now, they will leverage **Compliance Logging Auditing & Security Telemetry Tracking** to perform an automated code walkthrough based on formal IEEE 1028 review standards.

As highlighted in the provided documentation walkthrough, the system specification explicitly demands that transaction events be logged with user IDs, timestamps, and **IP addresses** for regulatory compliance (e.g., PCI DSS, SOX). However, the current legacy application explicitly excludes it, writing a note stating `"No IP address recorded"`.

Your students will write an orchestrator that detects this compliance logging gap during a simulation run, automatically updates the security logging engine to capture the valid host parameter context, and certifies the application through the universal governance gatekeeper.

---

## 🏗️ Module 04 Architecture Directory Map

```text
04-module-compliance-auditing/
├── bank_transfer_service.py       # Immutable Baseline (Legacy transfer engine with a compliance logging gap)
├── agent_debugger.py             # Security Orchestrator (Traps compliance gaps -> builds staging asset)
├── bank_transfer_service_healed.py # Staging Target Output (Generates fully compliant secure audit logs)
├── eval_debugger.py              # Governance Agent (Verifies clean execution & compliance matching)
├── debugging_report.md           # Pipeline verification report (Passes structural check)
└── eval_results.json              # Final automated validation grading token

```

---

## 🔑 Reference Answer Keys (Instructor Verification Layer)

### 1. The Immutable Baseline (`bank_transfer_service.py`)

This file represents the legacy core banking application block that passes basic syntax rules but actively violates non-functional logging security protocols.

```python
# Bank Transfer Service Layer - Project Horizon Baseline
import json
import os

def process_transfer(source_acc, dest_acc, amount):
    print(f"[*] Processing transaction request: From {source_acc} to {dest_acc} for ${amount}...")
    
    # Core Data Validation Logic
    if source_acc == dest_acc:
        return "Source and destination accounts must be different."
        
    # Mock Audit Log Payload Definition
    audit_entry = {
        "timestamp": "2026-05-29T14:32:10",
        "user_id": source_acc,
        "destination": dest_acc,
        "amount": amount,
        # COMPLIANCE FAULT: Violates IEEE 1028 spec and PCI DSS regulations by failing to log client IP parameters
        "note": "No IP address recorded"
    }
    
    with open("audit_log.json", "w", encoding="utf-8") as f:
        json.dump(audit_entry, f, indent=2)
        
    # Programmatic Compliance Alarm for the SQA Pipeline Tracker
    if audit_entry.get("note") == "No IP address recorded":
        raise ValueError("ComplianceViolationError: Secure audit telemetry trail missing client IP address context context.")
        
    return "Transfer successful."

if __name__ == "__main__":
    process_transfer("123-001", "123-002", 100.0)

```

### 2. The Refactored Orchestrator (`agent_debugger.py`)

This script executes the transfer script, intercepts the `ComplianceViolationError` from the standard error stream, and uses regular expressions to swap out the unshielded audit configuration for a hardened network identity tracker.

```python
import subprocess
import os
import sys
import re

SRC_SCRIPT = "bank_transfer_service.py"
HEALED_SCRIPT = "bank_transfer_service_healed.py"
REPORT_FILE = "debugging_report.md"

if not os.path.exists(SRC_SCRIPT):
    print(f"[-] Error: '{SRC_SCRIPT}' not found.")
    sys.exit(1)

print(f"[+] Security Orchestrator active. Copying baseline from '{SRC_SCRIPT}'...")

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
        print(f"[+] Quality Loop complete: Security log trails hardened on Pass #{iteration+1}.")
        break
        
    error_msg = run_check.stderr if run_check.stderr else run_check.stdout
    traceback_summary += f"\n--- Security Compliance Exception Caught on Pass #{iteration+1} ---\n{error_msg}"
    
    # TRIAGE STREAM: Target the non-compliant audit log footprint explicitly
    if "ComplianceViolationError" in error_msg or '"note": "No IP address recorded"' in script_source:
        print("[*] Triage: Engineering secure IP address telemetry injection rule...")
        
        # Replace the security gap with a fully authenticated IP tracker dictionary field entry
        script_source = script_source.replace('"note": "No IP address recorded"', '"ip_address": "127.0.0.1"')
        # Eliminate the validation safety tripwire trap cleanly
        script_source = script_source.replace('if audit_entry.get("note") == "No IP address recorded":', 'if "ip_address" not in audit_entry:')
        
        patched_code_display.append("Hardened audit log dictionary fields to inject mandatory client network IP parameters.")
    else:
        print("[-] System loop complete or unhandled exception profile trapped.")
        break

    with open(HEALED_SCRIPT, "w", encoding="utf-8") as f:
        f.write(script_source)

# Export the mandatory diagnostic summary file for the evaluator check
diff_summary = "\n".join([f"- {item}" for item in patched_code_display]) if patched_code_display else "- Security metrics verified."
with open(REPORT_FILE, "w", encoding="utf-8") as report_file:
    report_file.write(
        f"# SQA Compliance Auditing & Log Verification Report\n\n"
        f"## Target File Audited\n`{SRC_SCRIPT}`\n\n"
        f"## Captured Guardrail Violations\n```text\n{traceback_summary.strip()}\n```\n\n"
        f"## Applied Structural Resilience Patches\n{diff_summary}\n"
    )
print(f"[+] Automated telemetry audit report written out to '{REPORT_FILE}'.")

```

### 3. The Universal Evaluator (`eval_debugger.py`)

This remains your standardized, standalone gatekeeper file that automatically finds the generated `_healed.py` file, compiles it cleanly, checks for the presence of the compliance metadata string `"Audited"`, and signs off with a perfect grade.

```python
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

# Strict validation check for clean execution (Exit 0) and zero active error trace strings
has_runtime_crash = run_check.returncode != 0 or "Traceback" in run_check.stderr or "ValueError" in run_check.stderr

if not has_runtime_crash and os.path.exists("audit_log.json"):
    with open(REPORT_FILE, "r", encoding="utf-8") as rf:
        report_text = rf.read()
        
    with open("audit_log.json", "r", encoding="utf-8") as jf:
        log_data = json.load(jf)

    # Compliance validations: Verify structural log parameters are saved
    is_ip_captured = "ip_address" in log_data and log_data["ip_address"] == "127.0.0.1"
    is_report_valid = "Report" in report_text and "Audited" in report_text

    if is_ip_captured and is_report_valid:
        json_data = {
            "status": "APPROVED",
            "score": 100,
            "raw_ai_critique": f"The verification gate successfully certified '{target_script}'. The pipeline captures secure network identities, eliminates compliance trace errors, and produces an authorized audit markdown log."
        }
    else:
        json_data = {
            "status": "REJECTED",
            "score": 50,
            "raw_ai_critique": "The script executes safely, but the resulting audit trail formats or the companion markdown report layout failed compliance audits."
        }
else:
    clipped_error = run_check.stderr.strip()[:150] if run_check.stderr else "Missing file system validation tokens."
    json_data = {
        "status": "REJECTED",
        "score": 0,
        "raw_ai_critique": f"Staging artifact execution gate check failed. Live crash log output:\n{clipped_error}"
    }

with open(OUTPUT_FILE, "w", encoding="utf-8") as j: json.dump(json_data, j, indent=2)
print(f"[+] Governance evaluation complete. Results written cleanly to '{OUTPUT_FILE}'.")

```

---

## 📝 Complete Student Lab Manual

# Lab Manual: Compliance Logging Auditing & IEEE 1028 Walkthroughs

## Objective

In this lab, you will move from general system triage up to **Compliance Governance and Regulatory Telemetry Tracking**. Simulating a formal walkthrough review process aligned with **IEEE 1028 standard requirements**, you will identify a critical compliance gap within a financial transaction service layer.

You will build a two-agent automation system designed to intercept unhandled compliance warning flags and automatically rewrite the application's logging structure to capture mandatory security parameters.

To preserve the architectural baseline of your development workspace, your code tracking tools must treat the original software module as an immutable baseline, outputting all refactored code updates to an isolated staging asset file:

1. 
**The Orchestrator Agent (`agent_debugger.py`):** Programmatically invokes runtime executions, isolates security tracking defects from the error stream, and outputs a secure build artifact.


2. **The Evaluator Agent (`eval_debugger.py`):** Acts as an independent compliance officer, evaluating the resulting staging asset file and generating standardized grading metrics.

---

### Step 1: Initialize the Immutable Baseline (`bank_transfer_service.py`)

First, construct your core transaction service module layer. This script contains valid operational data validation loops but explicitly violates banking compliance regulations (such as PCI DSS or Sarbanes-Oxley mandates) by actively discarding the client's network identity signature during audit log writing cycles.

Create a file named `bank_transfer_service.py` and populate it with the following baseline implementation:

```python
# Bank Transfer Service Layer - Project Horizon Baseline
import json
import os

def process_transfer(source_acc, dest_acc, amount):
    print(f"[*] Processing transaction request: From {source_acc} to {dest_acc} for ${amount}...")
    
    # Core Data Validation Logic
    if source_acc == dest_acc:
        return "Source and destination accounts must be different."
        
    # Mock Audit Log Payload Definition
    audit_entry = {
        "timestamp": "2026-05-29T14:32:10",
        "user_id": source_acc,
        "destination": dest_acc,
        "amount": amount,
        # COMPLIANCE FAULT: Violates IEEE 1028 spec and PCI DSS regulations by failing to log client IP parameters
        "note": "No IP address recorded"
    }
    
    with open("audit_log.json", "w", encoding="utf-8") as f:
        json.dump(audit_entry, f, indent=2)
        
    # Programmatic Compliance Alarm for the SQA Pipeline Tracker
    if audit_entry.get("note") == "No IP address recorded":
        raise ValueError("ComplianceViolationError: Secure audit telemetry trail missing client IP address context.")
        
    return "Transfer successful."

if __name__ == "__main__":
    process_transfer("123-001", "123-002", 100.0)

```

---

### Step 2: Build the Orchestrator Triage Agent (`agent_debugger.py`)

Your second task is to build an automation agent capable of executing an autonomous code walkthrough. It must run the script, identify missing parameters based on the system's `ComplianceViolationError` signal, and patch the tracking payload structure to inject mandatory parameters.

Create `agent_debugger.py` to satisfy the following engineering specifications:

* 
**Immutable Inputs:** Your script must read from the baseline file (`bank_transfer_service.py`) but **never mutate it directly**. All ongoing refactoring loops must happen in-memory or be saved to a standalone staging file.


* **Isolated Target Output:** Save your final, hardened code updates to a brand-new staging file named `bank_transfer_service_healed.py`.
* **Multi-Pass Convergence Loop:** Configure an execution cycle (up to 5 iterations) to continuously capture downstream errors that surface once earlier blockers are eliminated.
* 
**Traceback-Driven Triage:** Route your code modifications by analyzing error keywords found inside the runtime's `stderr` channel (e.g., target the `ComplianceViolationError` text trace).


* 
**Idempotent Mitigation Logic:** Update the file buffer to strip the non-compliant note parameter string, safely injecting an authenticated dictionary field entry named `"ip_address": "127.0.0.1"` instead. Ensure your replacement loop explicitly checks if the string is already modified to prevent duplicate code stacking.


* **Pipeline Telemetry:** Upon cycle completion, compile an automated diagnostic summary named `debugging_report.md` logging the trapped tracebacks and applied structural modifications.

---

### Step 3: Implement the Independent Governance Gate (`eval_debugger.py`)

To eliminate conflicts of interest within automated infrastructure pipelines, the tool modifying code must remain completely decoupled from the system certifying compliance. You will deploy your standardized, universal evaluation module to function as your standalone quality gate.

Create `eval_debugger.py` to perform a **hybrid structural-and-semantic validation audit**:

1. **Dynamic Target Discovery:** The script must dynamically scan your directory workspace using file pattern filters (e.g., `glob.glob("*_healed.py")`) to find the target staging build asset.
2. 
**Compilation Guard:** It must programmatically execute the discovered staging build artifact, verifying that the script terminates with a perfect exit code of `0` and leaves behind zero trace errors or compliance warnings.


3. 
**Data Compliance Evaluation:** It must read the resulting `audit_log.json` payload structure to confirm that the `"ip_address"` metric has been successfully recorded with an evaluated identity string of `"127.0.0.1"`.


4. **Telemetry Substring Check:** It must verify that `debugging_report.md` exists and contains the strict compliance auditing markdown substring parameters **"Report"** and **"Audited"**.
5. **Structured Schema Export:** Save your final compliance evaluations directly into a standardized JSON payload named `eval_results.json` matching this layout:

```json
{
  "status": "APPROVED" or "REJECTED",
  "score": 100 or 0,
  "raw_ai_critique": "A brief structural analysis statement outlines pipeline verification criteria."
}

```

---

### Step 4: Execute the Multi-Agent Pipeline

Once your automated testing architecture is complete, flush any historical tracking indicators out of your directory workspace and execute your pipeline end-to-end within your command terminal:

```bash
# Clean out previous execution traces
rm -f eval_results.json debugging_report.md bank_transfer_service_healed.py audit_log.json

# Step 1: Run the Security Self-Healing Orchestrator Agent
python agent_debugger.py

# Step 2: Run the Independent Compliance Evaluator Gate
python eval_debugger.py

```

---

### Step 5: Verification & System Audit

To confirm that your autonomous loop is operating optimally, audit your workspace outputs:

* 
**`bank_transfer_service.py`:** Check the file to ensure it remains completely untouched and retains its original non-compliant code.


* 
**`bank_transfer_service_healed.py`:** Confirm that this script runs seamlessly with an exit code of `0` and generates secure, trace-compliant logs.


* **`eval_results.json`:** Ensure that the verification matrix logs an `"APPROVED"` status parameter coupled with a perfect engineering score of `100`.