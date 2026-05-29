Moving into **Module 03** represents an excellent progression in your curriculum. In Labs 01 and 02, students learned how to isolate compile-time crashes and handle input-driven non-functional vulnerabilities. Now, you are raising the bar to **Systems-Level Telemetry and Compliance Governance**.

Instead of treating the orchestrator as a simple patch-bot, this lab positions it as an **automated Site Reliability Engineering (SRE) triage worker** operating under strict architectural constraints.

By using the **Staging Build Artifact model** we perfected in the previous modules, your portfolio retains identical command-line mechanics, while the underlying domain scales beautifully into ITIL Incident Management frameworks.

---

## 🏗️ Module 03 Architecture Directory Map

```text
03-module-incident-routing/
├── incident_router.py            # Immutable Baseline (Simulates a crashing system stream)
├── agent_debugger.py             # SRE Orchestrator (Traps telemetry -> writes healed engine)
├── incident_router_healed.py     # Staging Target (Generates JSON/MD artifacts on run)
├── eval_debugger.py              # Governance Agent (Audits compilation & ITIL schema compliance)
├── debugging_report.md           # Pipeline diagnostic log (Passes structural check)
└── eval_results.json             # Final validation grading token

```

---

## 🔑 Reference Answer Keys (Instructor Verification Layer)

### 1. The Immutable Baseline (`incident_router.py`)

This script simulates a production pipeline choked by an unhandled database telemetry crash.

```python
# Incident Routing Service - Project Horizon Baseline
import json
import os

RAW_TRACEBACK = """
Traceback (most recent call last):
  File "database/connection.py", line 42, in connect
    raise SQLAlchemy.exc.OperationalError("psycopg2.OperationalError: connection to server failed: Connection timed out")
SQLAlchemy.exc.OperationalError: (psycopg2.OperationalError) connection timed out
"""

def route_incident(traceback_log):
    # FAULT: The legacy routing engine lacks an automated ITIL mapping matrix.
    # It blindly triggers system failures on unhandled core infrastructure exceptions.
    raise NotImplementedError("Automated ITIL Triage Engine not implemented. Database crash blocked pipeline.")

if __name__ == "__main__":
    print("[*] Processing incoming infrastructure telemetry streams...")
    route_incident(RAW_TRACEBACK)

```

### 2. The Updated Orchestrator (`agent_debugger.py`)

This script traps the baseline's routing failure and builds a live, idempotent ITIL classification logic layer into the staging build target.

```python
import subprocess
import os
import sys

SRC_SCRIPT = "incident_router.py"
HEALED_SCRIPT = "incident_router_healed.py"
REPORT_FILE = "debugging_report.md"

if not os.path.exists(SRC_SCRIPT):
    print(f"[-] Error: '{SRC_SCRIPT}' not found.")
    sys.exit(1)

print(f"[+] SRE Orchestrator active. Seeding staging target from '{SRC_SCRIPT}'...")

with open(SRC_SCRIPT, "r", encoding="utf-8") as f:
    baseline_source = f.read()

with open(HEALED_SCRIPT, "w", encoding="utf-8") as f:
    f.write(baseline_source)

traceback_summary = ""
patched_code_display = []

for iteration in range(5):
    with open(HEALED_SCRIPT, "r", encoding="utf-8") as f:
        script_source = f.read()

    run_check = subprocess.run(["python", HEALED_SCRIPT], capture_output=True, text=True)
    
    if run_check.returncode == 0 and os.path.exists("incidents.json"):
        print(f"[+] Quality Loop complete: Telemetry router stabilized on Pass #{iteration+1}.")
        break
        
    error_msg = run_check.stderr if run_check.stderr else run_check.stdout
    traceback_summary += f"\n--- Infrastructure Crash Trapped on Pass #{iteration+1} ---\n{error_msg}"
    
    # TRIAGE STREAM: Intercept NotImplementedError and inject the automated ITIL router block
    if "NotImplementedError" in error_msg:
        print("[*] Triage: Constructing automated ITIL mapping engine layer...")
        
        itil_engine_impl = """
    # Automated ITIL Triage Engine Implementation
    incident_data = {
        "severity": "CRITICAL",
        "category": "Database",
        "summary": "SQLAlchemy connection timed out on backend server authentication paths.",
        "remediation": "Verify VPC security group rules for ingress port 5432 and cycle target listener containers."
    }
    with open("incidents.json", "w", encoding="utf-8") as jf:
        json.dump(incident_data, jf, indent=2)
        
    with open("triage_summary.md", "w", encoding="utf-8") as mf:
        mf.write("# ITIL Emergency Incident Triage Summary\\n\\n")
        mf.write("## Metadata\\n- Domain: Data Engineering\\n- Severity: CRITICAL\\n\\n")
        mf.write("## Analysis\\nDatabase connectivity failures detected in telemetry stream log layers.")
    print("[+] ITIL Core Artifacts written out to pipeline staging.")
    return incident_data
"""
        # Swap out the error marker line smoothly
        script_source = script_source.replace('raise NotImplementedError("Automated ITIL Triage Engine not implemented. Database crash blocked pipeline.")', itil_engine_impl)
        patched_code_display.append("Injected automated ITIL classification routing structures and telemetry hooks.")
    else:
        print("[-] Stabilization threshold reached or unmapped telemetry signature encountered.")
        break

    with open(HEALED_SCRIPT, "w", encoding="utf-8") as f:
        f.write(script_source)

# Write the structural telemetry compliance log
diff_summary = "\n".join([f"- {item}" for item in patched_code_display]) if patched_code_display else "- Routing matrix verified."
with open(REPORT_FILE, "w", encoding="utf-8") as report_file:
    report_file.write(
        f"# SQA Incident Routing Engine Report\n\n"
        f"## Target File Audited\n`{SRC_SCRIPT}`\n\n"
        f"## Captured Guardrail Violations\n```text\n{traceback_summary.strip()}\n```\n\n"
        f"## Applied Structural Resilience Patches\n{diff_summary}\n"
    )
print(f"[+] Telemetry verification report logged cleanly to '{REPORT_FILE}'.")

```

### 3. The Shared/ITIL Hybrid Evaluator (`eval_debugger.py`)

This script uses the `glob` wildcard mechanism to find our staging script target, runs it, and performs both execution safety and ITIL data compliance audits.

```python
import json
import os
import sys
import subprocess
import glob

REPORT_FILE = "debugging_report.md"
OUTPUT_FILE = "eval_results.json"
INCIDENTS_JSON = "incidents.json"
TRIAGE_MD = "triage_summary.md"

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

# Step 1: Execution validation gate run
run_check = subprocess.run(["python", target_script], capture_output=True, text=True)

if run_check.returncode == 0 and os.path.exists(INCIDENTS_JSON) and os.path.exists(TRIAGE_MD):
    # Step 2: Validate generated ITIL downstream data compliance tokens
    with open(INCIDENTS_JSON, "r", encoding="utf-8") as jf:
        incident_metrics = json.load(jf)
        
    with open(TRIAGE_MD, "r", encoding="utf-8") as mf:
        triage_text = mf.read()
        
    with open(REPORT_FILE, "r", encoding="utf-8") as rf:
        report_text = rf.read()

    # ITIL Governance Constraints Verification
    is_database_category = incident_metrics.get("category") == "Database"
    is_critical_severity = incident_metrics.get("severity") == "CRITICAL"
    is_assigned_correctly = "Data Engineering" in triage_text
    is_report_valid = "Report" in report_text and "Audited" in report_text

    if is_database_category and is_critical_severity and is_assigned_correctly and is_report_valid:
        json_data = {
            "status": "APPROVED",
            "score": 100,
            "raw_ai_critique": f"Governance check passed. The script compiled cleanly, mapped the database exception to 'CRITICAL' severity, and routed the ticket to the Data Engineering domain under ITIL parameters."
        }
    else:
        json_data = {
            "status": "REJECTED",
            "score": 50,
            "raw_ai_critique": "The pipeline runs, but the generated incident artifacts failed ITIL compliance classification standards."
        }
else:
    json_data = {
        "status": "REJECTED",
        "score": 0,
        "raw_ai_critique": f"Artifact validation gate execution failed. System traceback:\n{run_check.stderr[:150]}"
    }

with open(OUTPUT_FILE, "w", encoding="utf-8") as j: json.dump(json_data, j, indent=2)
print(f"[+] Governance execution matrix output successfully to '{OUTPUT_FILE}'.")

```

---

## 📝 Complete Student Lab Manual

# Lab Manual: Self-Healing Incident Routing Engines

## Objective

In this lab, you will scale your multi-agent self-healing pipeline skills to tackle **Automated Systems Telemetry and Compliance Governance**. You will construct an orchestration architecture that simulates an automated Site Reliability Engineering (SRE) triage worker.

Your pipeline will ingest raw exception tracebacks from an unhandled production outage, dynamically infer the broken operational layer, and refactor the service to write out structured, ITIL-compliant incidents.

To preserve the integrity of your production environment, your framework must treat the original telemetry script as an immutable baseline, outputting all programmatic hotfixes to an isolated staging build artifact:

1. **The Orchestrator Agent (`agent_debugger.py`):** Programmatically triggers runtime execution, traps raw application errors, triages the exception payload, and generates a stabilized triage routing artifact.
2. **The Evaluator Agent (`eval_debugger.py`):** Acts as an independent governance gate, auditing the generated staging file and verifying that the resulting metadata maps precisely to standard ITIL Incident Management frameworks.

---

### Step 1: Initialize the Immutable Baseline (`incident_router.py`)

First, initialize your baseline application telemetry layout. This script acts as a system utility stream processor that completely locks up or errors out when it encounters a raw database connection error string.

Create a file named `incident_router.py` and populate it with the following baseline implementation:

```python
# Incident Routing Service - Project Horizon Baseline
import json
import os

RAW_TRACEBACK = """
Traceback (most recent call last):
  File "database/connection.py", line 42, in connect
    raise SQLAlchemy.exc.OperationalError("psycopg2.OperationalError: connection to server failed: Connection timed out")
SQLAlchemy.exc.OperationalError: (psycopg2.OperationalError) connection timed out
"""

def route_incident(traceback_log):
    # FAULT: The legacy routing engine lacks an automated ITIL mapping matrix.
    # It blindly triggers system failures on unhandled core infrastructure exceptions.
    raise NotImplementedError("Automated ITIL Triage Engine not implemented. Database crash blocked pipeline.")

if __name__ == "__main__":
    print("[*] Processing incoming infrastructure telemetry streams...")
    route_incident(RAW_TRACEBACK)

```

---

### Step 2: Build the Orchestrator Triage Agent (`agent_debugger.py`)

Your second task is to engineer the automated triage engine. It must read the immutable code layout, execute it via background shell processes, read the crash exceptions from the standard error track, and hotfix the router logic so it handles the incoming exception stream gracefully.

Create `agent_debugger.py` to meet the following precise structural specifications:

* **Immutable Inputs:** Your script must read from the baseline file (`incident_router.py`) but **never mutate it directly**. All refactoring iterations must happen in-memory or write to a staging workspace.
* **Isolated Target Output:** Write your stabilized, error-free code modifications to a brand-new staging file named `incident_router_healed.py`.
* **Multi-Pass Convergence Loop:** Configure a loop execution boundary (up to 5 iterations) to systematically run the staging code and clean up cascading execution faults.
* **Traceback-Driven Triage:** Direct your hotfix insertion triggers based on the exception text thrown in the runtime `stderr` payload. Your script must intercept the unhandled `NotImplementedError` and inject a structured code layer that successfully handles the database crash.
* **Downstream Artifact Generation:** The code block injected by your orchestrator into `incident_router_healed.py` must programmatically generate two compliance files when executed:
1. **`incidents.json`:** A structured dictionary file mapping exactly to the schema: `{"severity": "CRITICAL", "category": "Database", "summary": "...", "remediation": "..."}`.
2. **`triage_summary.md`:** A comprehensive markdown incident log mapping the ticket explicitly to the **Data Engineering** infrastructure domain.


* **Pipeline Telemetry:** Upon convergence, save an automated execution summary named `debugging_report.md` detailing the trapped exceptions and specific patch rules fired.

> 💡 **Design Constraint:** Ensure all patch blocks are **idempotent**. The script writer must verify that modifications do not duplicate or stack recursively across successive testing runs.

---

### Step 3: Implement the Independent Governance Gate (`eval_debugger.py`)

To fulfill compliance standards, the agent modifying code must remain completely isolated from the auditor validating the builds. You will build a decoupled evaluator script to act as your ITIL Compliance Officer gate.

Create `eval_debugger.py` to execute a **hybrid structural-and-semantic validation check**:

1. **Compilation Check:** It must programmatically discover and run your staging build artifact (`incident_router_healed.py`), verifying it terminates with a perfect exit code of `0`.
2. **ITIL Functional Audit:** It must inspect the resulting `incidents.json` and `triage_summary.md` files to verify that database connectivity failures are accurately classified under a `"CRITICAL"` severity flag, tagged with a `"Database"` category token, and assigned explicitly to the **Data Engineering** domain.
3. **Telemetry Validation:** It must confirm the existence of `debugging_report.md` featuring standard audit headers.
4. **Structured Schema Export:** Save your final output summary directly into a standardized JSON payload named `eval_results.json` using this schema:

```json
{
  "status": "APPROVED" or "REJECTED",
  "score": 100 or 0,
  "raw_ai_critique": "A brief structural analysis statement outlining pipeline verification criteria."
}

```

---

### Step 4: Execute the Multi-Agent Pipeline

Once your automation layer is ready, flush any historical tracking metrics from your workspace folder and run your pipeline end-to-end within your command terminal:

```bash
# Clean out previous execution traces
rm -f eval_results.json debugging_report.md incident_router_healed.py incidents.json triage_summary.md

# Step 1: Run the Self-Healing Telemetry Orchestrator Agent
python agent_debugger.py

# Step 2: Run the Independent ITIL Governance Gate
python eval_debugger.py

```

---

### Step 5: Verification & System Audit

To confirm that your autonomous loop is operating optimally, audit your workspace outputs:

* **`incident_router.py`:** Confirm the baseline file remains completely pristine and unchanged.
* **`incident_router_healed.py`:** Verify that the script executes with zero active exceptions and safely outputs your compliance metrics.
* **`eval_results.json`:** Ensure that the verification matrix logs an `"APPROVED"` parameter matching a perfect score of `100`.