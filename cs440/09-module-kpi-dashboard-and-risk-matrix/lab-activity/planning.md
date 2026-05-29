Moving into **Module 09**, we round out your automated software quality engineering portfolio with **KPI Dashboards & Risk Assessment Matrices**.

Following the structure of metric tracking systems and risk matrix evaluation frameworks (Impact vs. Likelihood) detailed in your lab brief, this module highlights the necessity of tracking performance health indicators while ensuring that analytical calculations maintain strict boundaries.

The baseline script simulates a calculation pipeline that throws explicit exceptions (`KPIDashboardError` and `RiskMatrixException`) when it encounters unhandled empty metric configurations or out-of-bounds matrix risk inputs. Students will write a self-healing orchestrator that captures these pipeline calculation defects exclusively via the active error stream (`stderr`) and applies defensive validation guards inside a separate staging target artifact.

---

## 🏗️ Module 09 Architecture Directory Map

```text
09-module-kpi-risk-matrix/
├── kpi_risk_service.py            # Immutable Baseline (Metrics layer with calculation gaps)
├── agent_debugger.py              # SRE Orchestrator (Traps calculation/bounds exceptions -> builds staging asset)
├── kpi_risk_service_healed.py     # Staging Target Output (Generates fully stabilized calculation engine)
├── eval_debugger.py               # Universal Governance Agent (Verifies execution and report tracking)
├── debugging_report.md            # Pipeline verification report (Passes structural check)
└── eval_results.json              # Final automated validation grading token

```

---

## 🔑 Master Answer Keys (Instructor & CI/CD Pipeline Layer)

### 1. The Universal Governance Gate (`eval_debugger.py`)

*This environment-agnostic automated release gate remains identical and completely immutable across your laboratory repository track.*

```python
# Universal Governance Gate - Project Horizon Compliance Runner
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

# Broad validation check for clean execution (Exit 0) and zero active runtime error traces
has_runtime_crash = (
    run_check.returncode != 0 or 
    "Traceback" in run_check.stderr or 
    "ValueError" in run_check.stderr or
    "TypeError" in run_check.stderr
)

if not has_runtime_crash:
    with open(REPORT_FILE, "r", encoding="utf-8") as rf:
        report_text = rf.read()
        
    is_report_valid = "Report" in report_text and "Audited" in report_text

    if is_report_valid:
        json_data = {
            "status": "APPROVED",
            "score": 100,
            "raw_ai_critique": f"The verification gate successfully certified '{target_script}'. The script compiled cleanly (Exit 0) and the orchestration report passed structural process compliance."
        }
    else:
        json_data = {
            "status": "REJECTED",
            "score": 50,
            "raw_ai_critique": "The healed staging script executes cleanly, but the companion markdown report layout failed structural auditing criteria."
        }
else:
    clipped_error = run_check.stderr.strip()[:150] if run_check.stderr else "Runtime compilation verification check failed."
    json_data = {
        "status": "REJECTED",
        "score": 0,
        "raw_ai_critique": f"Staging artifact execution gate check failed. Live crash log output:\n{clipped_error}"
    }

with open(OUTPUT_FILE, "w", encoding="utf-8") as j: json.dump(json_data, j, indent=2)
print(f"[+] Governance evaluation complete. Results written cleanly to '{OUTPUT_FILE}'.")

```

### 2. Module 09 Orchestrator Solution (`agent_debugger.py`)

*This master solution processes the metric configuration exceptions exclusively via the runtime `stderr` stream, avoiding any quote alternation or cascade evaluation loops.*

```python
import subprocess
import os
import sys

SRC_SCRIPT = "kpi_risk_service.py"
HEALED_SCRIPT = "kpi_risk_service_healed.py"
REPORT_FILE = "debugging_report.md"

if not os.path.exists(SRC_SCRIPT):
    print(f"[-] Error: '{SRC_SCRIPT}' not found.")
    sys.exit(1)

print(f"[+] KPI & Risk Orchestrator active. Seeding staging target from '{SRC_SCRIPT}'...")

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
        print(f"[+] Quality Loop complete: Metrics dashboard calculations stabilized on Pass #{iteration+1}.")
        break
        
    error_msg = run_check.stderr if run_check.stderr else run_check.stdout
    traceback_summary += f"\n--- Analytics Boundary Violation Caught on Pass #{iteration+1} ---\n{error_msg}"
    
    # TRIAGE ROUTING STREAM EXCLUSIVELY DRIVEN BY THE ACTIVE RUNTIME ERROR PAYLOAD
    if "KPIDashboardError" in error_msg:
        print("[*] Triage: Engineering defensive fallback array handlers for KPI calculations...")
        dashboard_patch = (
            "if not metrics:\n"
            "        print('[-] Metric dataset empty. Defaulting to safe baseline score evaluation.')\n"
            "        return 0.0"
        )
        script_source = script_source.replace('raise ValueError("KPIDashboardError: Empty metric telemetry dataset or invalid selection logic weights.")', dashboard_patch)
        patched_code_display.append("Injected array validation fallback controls to safeguard dashboard calculations from empty metrics evaluation hooks.")
        
    elif "RiskMatrixException" in error_msg:
        print("[*] Triage: Injecting 5x5 boundary-clamping mitigation guards...")
        bounds_patch = (
            "print('[!] Out of bounds matrix inputs detected. Applying boundary clamping mitigation.')\n"
            "        impact = max(1, min(5, impact))\n"
            "        likelihood = max(1, min(5, likelihood))"
        )
        script_source = script_source.replace('raise TypeError("RiskMatrixException: Risk evaluation scores out of valid 5x5 metrics boundaries.")', bounds_patch)
        patched_code_display.append("Refactored risk calculation vectors to apply mathematical boundary clamping controls across 5x5 matrices.")
    else:
        print("[-] Target stabilization threshold reached or unmapped validation profile trapped.")
        break

    with open(HEALED_SCRIPT, "w", encoding="utf-8") as f:
        f.write(script_source)

# Write out output audit report containing the exact token phrase "Audited" to pass governance
diff_summary = "\n".join([f"- {item}" for item in patched_code_display]) if patched_code_display else "- Analytics vectors verified."
with open(REPORT_FILE, "w", encoding="utf-8") as report_file:
    report_file.write(
        f"# SQA Metrics Assessment & Risk Profiling Report\n\n"
        f"## Target File Audited\n`{SRC_SCRIPT}`\n\n"
        f"## Captured Guardrail Violations\n```text\n{traceback_summary.strip()}\n```\n\n"
        f"## Applied Structural Resilience Patches\n{diff_summary}\n"
    )
print(f"[+] Automated telemetry analytics report compiled at '{REPORT_FILE}'.")

```

---

## 📝 Student Lab Manual

# Lab Manual: KPI Dashboards & Risk Assessment Matrices

## Objective

In this laboratory, you will explore metrics optimization and analytical reliability by mastering **KPI Dashboards and Risk Matrix Mapping Governance**. Across enterprise software configurations, analytics pipelines must handle missing data points cleanly and enforce hard containment bounds across dimensional scales (such as standard 5x5 corporate risk impact frameworks). Unhandled calculation anomalies or data overflow vectors corrupt metric dashboard charts and trip pipeline runtime exceptions.

You will engineer an autonomous self-healing calculation engine inside **`agent_debugger.py`**. Your script will execute a defective analytical service layer, capture custom dashboard tracking failures from standard error buffers, and programmatically patch the math functions to deploy defensive fallbacks and boundary-clamping logic.

To maintain an unblemished development tracking environment, your orchestration code must treat the original software application as immutable, routing all refactored fixes to a standalone staging file:

1. **The Orchestrator Agent (`agent_debugger.py`):** Programmatically triggers runtime analytics checks, processes standard error streams to isolate calculation violations, and writes an optimized staging build file.
2. **The Evaluator Agent (`eval_debugger.py`):** An environment-agnostic universal governance gate runner pre-provided in your repository track that executes your staging targets to verify production readiness.

---

### Step 1: Initialize the Immutable Baseline (`kpi_risk_service.py`)

First, initialize your baseline application module. This script models an analytical processing engine that contains two distinct calculation defects: it crashes with a `KPIDashboardError` when passed an empty metrics selection list, and it fails with a `RiskMatrixException` when values exceed the standard 5x5 calculation ceiling.

Create a file named **`kpi_risk_service.py`** and populate it with this baseline implementation:

```python
# KPI Dashboard & Risk Matrix Service Layer - Project Horizon Baseline
import sys

def calculate_kpi_efficiency(metrics):
    print("[*] Evaluating KPI dashboard metrics...")
    
    # FAULT 1: Missing array validation guard. An empty list dataset will trigger a crash.
    if not metrics or len(metrics) == 0:
        raise ValueError("KPIDashboardError: Empty metric telemetry dataset or invalid selection logic weights.")
        
    return sum(metrics) / len(metrics)

def assess_risk_matrix(impact, likelihood):
    print(f"[*] Mapping risk matrix bounds: Impact={impact}, Likelihood={likelihood}...")
    
    # FAULT 2: Missing containment guards. Values must map strictly within a 1 to 5 scale.
    if impact < 1 or impact > 5 or likelihood < 1 or likelihood > 5:
        raise TypeError("RiskMatrixException: Risk evaluation scores out of valid 5x5 metrics boundaries.")
        
    return impact * likelihood

if __name__ == "__main__":
    print("[*] Loading metric assessment and risk profiling tracks...")
    
    # Sequential calculation verification hurdles designed to trigger tracebacks across passes
    try:
        calculate_kpi_efficiency([])
    except Exception as e:
        print(f"[-] Blocked by dashboard outlier: {e}", file=sys.stderr)
        raise e
        
    try:
        assess_risk_matrix(6, 4)
    except Exception as e:
        print(f"[-] Blocked by risk assessment boundaries: {e}", file=sys.stderr)
        raise e

```

---

### Step 2: Build the Orchestrator Triage Agent (`agent_debugger.py`)

Your primary engineering challenge is to write the automated analytics compliance orchestrator script. Your program must read the baseline code module, execute it within isolated system sub-processes, capture individual `KPIDashboardError` and `RiskMatrixException` trace descriptors from `stderr`, and apply targeted substitutions to achieve convergence.

Create **`agent_debugger.py`** to meet the following configuration requirements:

* **Immutable Inputs:** Your script must read from the baseline file (`kpi_risk_service.py`) but **#never alter it directly**. All refactoring transformations must occur in-memory or save directly to a staging file.
* **Isolated Target Output:** Save your final, error-free staging build configuration directly to a new file named `kpi_risk_service_healed.py`.
* **Multi-Pass Convergence Loop:** Configure an execution cycle (up to 5 iterations) to systematically catch downstream errors that surface as earlier mathematical registration blocks are refactored.
* **Process Interception:** Utilize Python’s `subprocess.run()` with `capture_output=True` to trap runtime console outputs safely without causing your orchestrator tool itself to crash.
* **Traceback-Driven Triage:** Direct your refactoring replacements by parsing specific exception keywords found inside the runtime error stream payload (`stderr`) *exclusively* to avoid priority cascade loops. Intercept missing metric arrays to deploy a defensive fallback calculation scoring default. Intercept out-of-bounds matrix indicators to inject standard min-max boundary clamping controls across the 5x5 impact grid.
* **Pipeline Telemetry:** Upon convergence, save an automated execution summary named `debugging_report.md` detailing the trapped exceptions and specific patch rules fired.

> 💡 **Design Constraint:** Ensure all patch blocks are strictly **idempotent**. Your script generator layer must explicitly protect its updates so that subsequent loop checks do not append duplicate or stacked logic configurations.

---

### Step 3: Run the Independent Governance Gate (`eval_debugger.py`)

Your repository directory includes a pre-provided, immutable automated release runner named **`eval_debugger.py`**. Do not modify this file. It scans your environment workspace to complete a **hybrid structural-and-semantic validation audit**:

1. **Dynamic Target Discovery:** Scans directory paths dynamically using text pattern wildcards (e.g., `glob.glob("*_healed.py")`) to capture and evaluate the target staging build artifact.
2. **Compilation Guard:** Runs your staging script file to confirm it successfully completes configuration loops with an exit status of `0` and throws zero lingering traceback crash exceptions.
3. **Telemetry Substring Verification:** Confirms that your generated `debugging_report.md` exists and contains the strict compliance auditing markdown substring parameters **"Report"** and **"Audited"**.
4. **Structured Schema Export:** Formats final compliance metrics straight into an industry-compliant JSON metadata token named `eval_results.json`.

---

### Step 4: Execute the Multi-Agent Pipeline

Once your automated orchestration layer is complete, flush any historical tracking indicators out of your directory workspace and execute your pipeline end-to-end within your command terminal:

```bash
# Clear downstream tracking artifacts
rm -f eval_results.json debugging_report.md kpi_risk_service_healed.py

# Step 1: Run your Self-Healing Metrics Orchestrator Agent
python agent_debugger.py

# Step 2: Invoke the pre-provided Pipeline Governance Gate
python eval_debugger.py

```

---

### Step 5: Verification & System Audit

To confirm that your autonomous loop is operating optimally, audit your workspace outputs:

* **`kpi_risk_service.py`:** Check the file to ensure it remains completely untouched and retains its original unvalidated configuration layout.
* **`kpi_risk_service_healed.py`:** Confirm that this file exists, safely processes empty metric streams, applies mathematical boundary clamping constraints across the risk grid, and compiles with a clean exit status code.
* **`eval_results.json`:** Verify that the file displays an `"APPROVED"` status parameter coupled with a perfect engineering score of `100`.