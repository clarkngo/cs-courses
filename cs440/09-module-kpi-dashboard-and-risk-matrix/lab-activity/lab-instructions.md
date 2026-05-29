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