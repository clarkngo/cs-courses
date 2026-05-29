Moving into **Module 05** expands your automated quality framework into the critical domain of **Internal Software Auditing and Process QA Frameworks**. In previous modules, your students developed pipelines to handle runtime stability, input anomalies, and regulatory log fields. In this exercise, they will simulate an automated internal quality audit matching formal engineering frameworks (such as **IEEE 1028 design reviews, CMMI-DEV QA standards, and ISO/IEC 12207 secure lifecycle processes**).

Following the metrics discovered in your audit report walkthrough document, the target codebase contains serious implementation defects: allowing blank input strings, missing essential data manipulation endpoints, using vague numeric status fields, and exposing clear vulnerabilities to Cross-Site Scripting (XSS) via un-escaped fields.

Students will build an autonomous audit compliance orchestrator that discovers these architectural deficiencies sequentially across a multi-pass loop, programmatically injecting code-level guardrails and schema corrections.

---

## 🏗️ Module 05 Architecture Directory Map

```text
05-module-software-audit/
├── task_manager_service.py        # Immutable Baseline (Legacy task logic with structural audit gaps)
├── agent_debugger.py              # Audit Orchestrator (Traps audit exceptions -> builds staging asset)
├── task_manager_service_healed.py # Staging Target Output (Generates fully compliant sanitized backend)
├── eval_debugger.py               # Universal Governance Agent (Verifies compilation and report tracking)
├── debugging_report.md            # Pipeline verification report (Passes structural check)
└── eval_results.json              # Final automated validation grading token

```

---

## 🔑 Reference Answer Keys (Instructor Verification Layer)

### 1. The Immutable Baseline (`task_manager_service.py`)

This file models a legacy project tool backend that lacks validation, lacks structural deletion properties, uses vague tracking labels, and ignores injection hazards.

```python
# Task Manager Service Layer - Project Horizon Baseline
import json
import os

def add_task(title, status=1):
    # Fault 1 & 5: Gaps in Input Control and Sanitization
    if title == "":
        raise ValueError("AuditViolation: Empty task title allowed without validation input controls.")
        
    if "<script>" in title:
        raise ValueError("AuditViolation: No input sanitization detected. Vulnerable to XSS injection.")
        
    # Fault 3: Uninformative and vague status logging metrics
    if status == 1:
        raise TypeError("AuditViolation: Status field set to numeric integer '1' instead of clear text labels.")
        
    print(f"[+] Task stored successfully: Title='{title}', Status='{status}'")
    return True

def delete_task(task_id):
    # Fault 2: Functional Lifecycle Gap
    raise NotImplementedError("AuditViolation: No delete function route implemented.")

if __name__ == "__main__":
    print("[*] Invoking internal software process audit simulation...")
    
    # Sequential verification hurdles designed to trigger tracebacks across passes
    add_task("")
    add_task("<script>alert('XSS')</script>")
    add_task("Complete SQA Module 05 Review", status=1)
    delete_task(101)

```

### 2. The Refactored Orchestrator (`agent_debugger.py`)

This answer key script copies the baseline into the staging workspace, executes the code iteratively to capture each distinct `AuditViolation` message, and applies precise, regular-expression refactoring patterns.

```python
import subprocess
import os
import sys
import re

SRC_SCRIPT = "task_manager_service.py"
HEALED_SCRIPT = "task_manager_service_healed.py"
REPORT_FILE = "debugging_report.md"

if not os.path.exists(SRC_SCRIPT):
    print(f"[-] Error: '{SRC_SCRIPT}' not found.")
    sys.exit(1)

print(f"[+] Audit Orchestrator active. Seeding staging file from '{SRC_SCRIPT}'...")

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
        print(f"[+] Quality Loop complete: Process compliance verified on Pass #{iteration+1}.")
        break
        
    error_msg = run_check.stderr if run_check.stderr else run_check.stdout
    traceback_summary += f"\n--- Process QA Deviation Caught on Pass #{iteration+1} ---\n{error_msg}"
    
    # TRIAGE ROUTING STRATEGIES
    if "Empty task title" in error_msg:
        print("[*] Triage: Engineering CMMI-aligned validation guard rail...")
        script_source = script_source.replace(
            'if title == "":\n        raise ValueError("AuditViolation: Empty task title allowed without validation input controls.")',
            'if title == "" or title.isspace():\n        print("[-] Rejected empty input payload.")\n        return False'
        )
        patched_code_display.append("Implemented input string validation loops to block meaningless blank submissions (CMMI-DEV Process QA).")
        
    elif "No input sanitization" in error_msg:
        print("[*] Triage: Deploying ISO/IEC 12207 secure code sanitization wrapper...")
        script_source = "import html\n" + script_source.replace(
            'if "<script>" in title:\n        raise ValueError("AuditViolation: No input sanitization detected. Vulnerable to XSS injection.")',
            'title = html.escape(title)\n    print("[+] Input text sanitized via html entities.")'
        )
        patched_code_display.append("Injected character entity escaping layers to mitigate XSS code injection hazards (ISO/IEC 12207).")
        
    elif "numeric integer '1'" in error_msg:
        print("[*] Triage: Refactoring status schema mapping parameters...")
        script_source = script_source.replace(
            'if status == 1:\n        raise TypeError("AuditViolation: Status field set to numeric integer \'1\' instead of clear text labels.")',
            'if status == 1:\n        status = "Pending"'
        )
        patched_code_display.append("Refactored vague database integer markers to explicit status string attributes ('Pending').")
        
    elif "No delete function" in error_msg:
        print("[*] Triage: Resolving functional gap to fulfill IEEE 1028 requirements...")
        resolved_deletion = """print(f"[+] Purging task entity {task_id} from tracking index.")
    return True"""
        script_source = script_source.replace('raise NotImplementedError("AuditViolation: No delete function route implemented.")', resolved_deletion)
        patched_code_display.append("Completed task asset deletion lifecycles to fulfill missing functional specification layers (IEEE 1028).")
        
    else:
        print("[-] Target stabilization point reached or unmapped validation profile trapped.")
        break

    with open(HEALED_SCRIPT, "w", encoding="utf-8") as f:
        f.write(script_source)

# Write output audit report (Crucial: Include the exact token phrase "Audited" to pass governance)
diff_summary = "\n".join([f"- {item}" for item in patched_code_display]) if patched_code_display else "- Process metrics fully verified."
with open(REPORT_FILE, "w", encoding="utf-8") as report_file:
    report_file.write(
        f"# SQA Process Compliance & Code Quality Audit Report\n\n"
        f"## Target File Audited\n`{SRC_SCRIPT}`\n\n"
        f"## Captured Guardrail Violations\n```text\n{traceback_summary.strip()}\n```\n\n"
        f"## Applied Structural Resilience Patches\n{diff_summary}\n"
    )
print(f"[+] Automated telemetry audit report written out to '{REPORT_FILE}'.")

```

---

## 📝 Complete Student Lab Manual

# Lab Manual: Internal Software Audits & Quality Compliance Frameworks

## Objective

In this lab, you will move beyond isolated functional script checking up to formal **Software Quality Assurance Process Auditing**. You will construct a two-agent architecture designed to model an automated internal quality auditor.

Your automation pipeline will run a defective service layer, intercept compliance exceptions matching structural vulnerabilities defined by **IEEE 1028, CMMI-DEV, and ISO/IEC 12207 frameworks**, and programmatically patch the backend to enforce secure code validation guidelines.

To maintain an immutable, reusable baseline across development and testing cycles, your orchestrator must preserve the original application code intact, exporting all programmatically refactored solutions to a separate, staging build asset file:

1. 
**The Orchestrator Agent (`agent_debugger.py`):** Programmatically runs background application checks, captures code compliance tracebacks, triages architectural defects, and exports an updated staging file.


2. **The Evaluator Agent (`eval_debugger.py`):** Acts as an independent governance gate, programmatically evaluating the resulting staging asset file to certify overall system quality compliance.

---

### Step 1: Initialize the Immutable Baseline (`task_manager_service.py`)

First, initialize your baseline application module. This script contains basic scaffolding loops but intentionally violates multiple core software engineering process benchmarks—specifically including missing entity lifecycle manipulation channels, empty input field allowances, and zero character sanitization barriers.

Create a file named **`task_manager_service.py`** and populate it with this baseline implementation:

```python
# Task Manager Service Layer - Project Horizon Baseline
import json
import os

def add_task(title, status=1):
    # Fault 1 & 5: Gaps in Input Control and Sanitization
    if title == "":
        raise ValueError("AuditViolation: Empty task title allowed without validation input controls.")
        
    if "<script>" in title:
        raise ValueError("AuditViolation: No input sanitization detected. Vulnerable to XSS injection.")
        
    # Fault 3: Uninformative and vague status logging metrics
    if status == 1:
        raise TypeError("AuditViolation: Status field set to numeric integer '1' instead of clear text labels.")
        
    print(f"[+] Task stored successfully: Title='{title}', Status='{status}'")
    return True

def delete_task(task_id):
    # Fault 2: Functional Lifecycle Gap
    raise NotImplementedError("AuditViolation: No delete function route implemented.")

if __name__ == "__main__":
    print("[*] Invoking internal software process audit simulation...")
    
    # Sequential verification hurdles designed to trigger tracebacks across passes
    add_task("")
    add_task("<script>alert('XSS')</script>")
    add_task("Complete SQA Module 05 Review", status=1)
    delete_task(101)

```

---

### Step 2: Build the Orchestrator Triage Agent (`agent_debugger.py`)

Your second task is to design an automated audit orchestrator. Your script must read the baseline code module, execute it within isolated background process pools, read the `AuditViolation` identifiers thrown in `stderr`, and apply targeted programmatic replacements to achieve compliance.

Create **`agent_debugger.py`** to meet the following engineering specifications:

* 
**Immutable Inputs:** Your script must read from the baseline file (`task_manager_service.py`) but **never alter it directly**. All refactoring transformations must happen in-memory or be saved to a staging file.


* **Isolated Target Output:** Save your final, hardened code updates to a brand-new staging file named `task_manager_service_healed.py`.
* **Multi-Pass Convergence Loop:** Configure an execution cycle (up to 5 iterations) to continuously capture downstream errors that surface once earlier blockers are eliminated.
* **Process Interception:** Utilize Python’s `subprocess.run()` with `capture_output=True` to trap raw standard error channels cleanly.
* **Traceback-Driven Triage:** Route your modifications based on the specific exception text thrown in the runtime `stderr` stream. Your rules must intercept and resolve:
* Catch empty title entries and replace them with structural field validation safeguards (**CMMI-DEV Process QA**).


* Catch raw injection patterns and wrap inputs in safe character escaping filters (**ISO/IEC 12207 Secure Lifecycle Processes**).


* Catch uninformative status indicators and map them to explicit descriptive string labels.


* Catch missing entity deletion endpoints and insert valid functional purging control channels (**IEEE 1028 Design Review Standard**).




* **Pipeline Telemetry:** Upon convergence, save an automated execution summary named `debugging_report.md` detailing the trapped exceptions and specific patch rules fired.

> 💡 **Design Constraint:** Ensure all patch blocks are **idempotent**. The script generation engine must explicitly verify that corrections do not duplicate or stack recursively across successive testing runs.

---

### Step 3: Implement the Independent Governance Gate (`eval_debugger.py`)

To prevent conflicts of interest in automated verification systems, the tool modifying code must remain decoupled from the runner certifying its quality. You will drop your universal evaluation module into the folder to function as your standalone quality gate.

Deploy **`eval_debugger.py`** to execute a **hybrid structural-and-semantic validation audit**:

1. **Dynamic Target Discovery:** The script must dynamically scan your directory workspace using file pattern filters (e.g., `glob.glob("*_healed.py")`) to find the target staging build asset.
2. **Compilation Guard:** It must programmatically execute the discovered staging build artifact, verifying that the script terminates with a perfect exit code of `0` and leaves behind zero trace errors or compliance warnings.
3. **Telemetry Validation:** It must confirm the existence of `debugging_report.md` and check that it contains the strict compliance auditing markdown substring parameters **"Report"** and **"Audited"**.
4. **Structured Schema Export:** Save your final compliance evaluations directly into a standardized JSON payload named `eval_results.json` matching this layout:

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
rm -f eval_results.json debugging_report.md task_manager_service_healed.py

# Step 1: Run the Self-Healing Audit Compliance Orchestrator Agent
python agent_debugger.py

# Step 2: Run the Standardized Independent Governance Gate
python eval_debugger.py

```

---

### Step 5: Verification & System Audit

To confirm that your autonomous loop is operating optimally, audit your workspace outputs:

* 
**`task_manager_service.py`:** Check the file to ensure it remains completely untouched and retains its original buggy codebase.


* 
**`task_manager_service_healed.py`:** Confirm that this file exists and contains the sanitized inputs, complete deletion blocks, string-mapped statuses, and robust input guards.


* **`eval_results.json`:** Verify that the file displays an `"APPROVED"` status parameter coupled with a perfect engineering score of `100`.