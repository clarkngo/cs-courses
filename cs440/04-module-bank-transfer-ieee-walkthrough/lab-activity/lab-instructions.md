Yes, we should update the Module 04 lab manual to make it completely bulletproof. This ensures students understand exactly where the baseline code belongs and prevents them from accidentally overwriting their orchestrator script.

Here is the finalized, production-ready version of the **Module 04 Lab Manual** reflecting our decoupled staging-build architecture, completely aligned with the IEEE 1028 walkthrough parameters.

---

# Lab Manual: Compliance Logging Auditing & IEEE 1028 Walkthroughs

## Objective

In this lab, you will advance from general system triage up to **Compliance Governance and Regulatory Telemetry Tracking**. Simulating a formal walkthrough review process aligned with **IEEE 1028 software review standards**, you will identify a critical compliance gap within a financial transaction service layer.

You will build a two-agent automation system designed to intercept unhandled compliance warning flags and automatically rewrite the application's logging structure to capture mandatory security parameters.

To preserve the architectural baseline of your development workspace, your code tracking tools must treat the original software module as an immutable baseline, outputting all refactored code updates to an isolated staging asset file:

1. **The Orchestrator Agent (`agent_debugger.py`):** Programmatically invokes runtime executions, isolates security tracking defects from the error stream, and outputs a secure build artifact.
2. **The Evaluator Agent (`eval_debugger.py`):** Acts as an independent compliance officer, evaluating the resulting staging asset file and generating standardized grading metrics.

---

### Step 1: Initialize the Immutable Baseline (`bank_transfer_service.py`)

First, construct your core transaction service module layer. This script contains valid operational data validation loops but explicitly violates banking compliance regulations (such as PCI DSS, SOX, or GLBA mandates) by actively discarding the client's network identity signature during audit log writing cycles.

Create a file named **`bank_transfer_service.py`** and populate it with this baseline implementation:

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
        # COMPLIANCE FAULT: Violates IEEE 1028 spec by failing to log client IP parameters
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

Your second task is to build an automation agent capable of executing an autonomous code walkthrough. It must run the external baseline script, identify missing parameters based on the system's `ComplianceViolationError` signal, and patch the tracking payload structure to inject mandatory parameters.

Create **`agent_debugger.py`** to satisfy the following engineering specifications:

* 
**Immutable Inputs:** Your script must read from the baseline file (`bank_transfer_service.py`) but **never mutate it directly**. All ongoing refactoring loops must happen in-memory or be saved to a standalone staging file.


* **Isolated Target Output:** Save your final, hardened code updates to a brand-new staging file named `bank_transfer_service_healed.py`.
* **Multi-Pass Convergence Loop:** Configure an execution cycle (up to 5 iterations) to continuously capture downstream errors that surface once earlier blockers are eliminated.
* **Process Interception:** Use Python's `subprocess.run()` with `capture_output=True` to run the staging file and trap execution states without causing the orchestrator itself to crash.
* **Traceback-Driven Triage:** Route your code modifications by analyzing error keywords found inside the runtime's `stderr` channel (e.g., target the `ComplianceViolationError` text trace).
* 
**Idempotent Mitigation Logic:** Update the file buffer to strip the non-compliant note parameter string, safely injecting an authenticated dictionary field entry named `"ip_address": "127.0.0.1"` instead. Ensure your replacement loop explicitly checks if the string is already modified to prevent duplicate code stacking.


* **Pipeline Telemetry:** Upon cycle completion, compile an automated diagnostic summary named `debugging_report.md` logging the trapped tracebacks and applied structural modifications.

---

### Step 3: Implement the Independent Governance Gate (`eval_debugger.py`)

To eliminate conflicts of interest within automated infrastructure pipelines, the tool modifying code must remain completely decoupled from the system certifying compliance. You will deploy your standardized, universal evaluation module to function as your standalone quality gate.

Create **`eval_debugger.py`** to perform a **hybrid structural-and-semantic validation audit**:

1. **Dynamic Target Discovery:** The script must dynamically scan your directory workspace using file pattern filters (e.g., `glob.glob("*_healed.py")`) to find the target staging build asset.
2. **Compilation Guard:** It must programmatically execute the discovered staging build artifact, verifying that the script terminates with a perfect exit code of `0` and leaves behind zero trace errors or compliance warnings.
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

* **`bank_transfer_service.py`:** Check the file to ensure it remains completely untouched and retains its original non-compliant code.
* 
**`bank_transfer_service_healed.py`:** Confirm that this script runs seamlessly with an exit code of `0` and generates secure, trace-compliant logs.


* **`eval_results.json`:** Ensure that the verification matrix logs an `"APPROVED"` status parameter coupled with a perfect engineering score of `100`.