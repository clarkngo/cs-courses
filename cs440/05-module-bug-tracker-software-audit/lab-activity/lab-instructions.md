Yes, presenting the finalized, fully synchronized version of the **Module 05 Lab Manual** ensures everything aligns with the decoupled architecture and our universal evaluation gatekeeper.

This layout incorporates the exact cross-references to industry quality standards (IEEE 1028, CMMI-DEV, and ISO/IEC 12207) established in your audit documentation.

---

# Lab Manual: Internal Software Audits & Quality Compliance Frameworks

## Objective

In this lab, you will advance from isolated functional script debugging to formal **Software Quality Assurance Process Auditing**. You will construct a two-agent architecture designed to model an automated internal quality auditor.

Your automation pipeline will execute a legacy task utility backend, intercept custom compliance exceptions mapping to structural process flaws defined by **IEEE 1028 design reviews, CMMI-DEV process controls, and ISO/IEC 12207 secure lifecycle frameworks**, and programmatically refactor the target asset to enforce code compliance guidelines.

To maintain a reusable, pristine baseline across your development and verification cycles, your orchestrator must treat the original codebase as immutable, exporting all programmatic hotfixes to an isolated staging build asset file:

1. **The Orchestrator Agent (`agent_debugger.py`):** Programmatically runs background application checks, traps process compliance tracebacks, triages architectural defects, and exports an updated staging file.
2. **The Evaluator Agent (`eval_debugger.py`):** Acts as an independent governance gate, evaluating the resulting staging asset file to certify overall system quality compliance.

---

### Step 1: Initialize the Immutable Baseline (`task_manager_service.py`)

First, initialize your baseline application module. This script contains basic scaffolding loops but intentionally violates multiple core software engineering process benchmarks—specifically including missing entity lifecycle manipulation channels, empty input field allowances, uninformative status markers, and zero character sanitization barriers.

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

Your second task is to design an automated audit orchestrator. Your script must read the baseline code module, execute it within isolated background process pools, read the custom `AuditViolation` identifiers thrown in `stderr`, and apply targeted programmatic replacements to achieve compliance.

Create **`agent_debugger.py`** to meet the following engineering specifications:

* **Immutable Inputs:** Your script must read from the baseline file (`task_manager_service.py`) but **never alter it directly**. All refactoring transformations must happen in-memory or be saved to a staging file.
* **Isolated Target Output:** Save your final, hardened code updates to a brand-new staging file named `task_manager_service_healed.py`.
* **Multi-Pass Convergence Loop:** Configure an execution cycle (up to 5 iterations) to continuously capture downstream errors that surface once earlier blockers are eliminated.
* **Process Interception:** Utilize Python’s `subprocess.run()` with `capture_output=True` to trap raw standard error channels cleanly.
* **Traceback-Driven Triage:** Route your modifications based on the specific exception text thrown in the runtime `stderr` stream. Your rules must intercept and resolve:
* Catch empty title entries and replace them with structural field validation guards to ensure process maturity (**CMMI-DEV Process QA**).


* Catch raw injection patterns and wrap inputs in safe character escaping filters to block Cross-Site Scripting (XSS) hazards (**ISO/IEC 12207 Secure Lifecycle Processes**).


* Catch uninformative status indicators and map the vague numeric integer `"1"` to explicit text labels like `"Pending"`.


* Catch missing entity deletion endpoints and insert a valid functional purging control route (**IEEE 1028 Review Standard**).




* **Pipeline Telemetry:** Upon convergence, save an automated execution summary named `debugging_report.md` detailing the trapped exceptions and specific patch rules fired.

> 💡 **Design Constraint:** Ensure all patch blocks are strictly **idempotent**. The script generation engine must explicitly verify that corrections do not duplicate or stack recursively across successive testing runs.

---

### Step 3: Implement the Independent Governance Gate (`eval_debugger.py`)

To prevent conflicts of interest in automated verification systems, the tool modifying code must remain completely decoupled from the runner certifying its quality. You will drop your universal evaluation module into the folder to function as your standalone quality gate.

Deploy **`eval_debugger.py`** to execute a **hybrid structural-and-semantic validation audit**:

1. **Dynamic Target Discovery:** The script must dynamically scan your directory workspace using wildcard pattern filters (e.g., `glob.glob("*_healed.py")`) to identify the target staging build asset.
2. **Compilation Guard:** It must programmatically execute the discovered staging build artifact, verifying that the script terminates with a perfect exit code of `0` and leaves behind zero trace errors or compliance warnings.
3. **Telemetry Validation:** It must confirm the physical existence of `debugging_report.md` and check that it contains the strict compliance auditing markdown substring parameters **"Report"** and **"Audited"**.
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

* **`task_manager_service.py`:** Check the file to ensure it remains completely untouched and retains its original buggy codebase.
* **`task_manager_service_healed.py`:** Confirm that this file exists and contains the sanitized inputs, complete deletion blocks, explicit string-mapped statuses, and robust input guards.
* **`eval_results.json`:** Verify that the file displays an `"APPROVED"` status parameter coupled with a perfect engineering score of `100`.

---

Now that Modules 01, 02, 03, 04, and 05 are completely streamlined into this automated, repeatable pipeline framework, would you like to sketch out the design parameters or initial files for Module 06?