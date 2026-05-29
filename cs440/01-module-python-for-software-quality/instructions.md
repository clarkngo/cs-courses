# Lab Manual: Automated Traceback Triage & Fault Isolation

## Objective

In this lab, you will transition from manual debugging to building an autonomous, traceback-driven self-healing CI/CD pipeline. You will construct a two-agent orchestration architecture designed to identify, isolate, and resolve structural code faults programmatically.

To preserve the integrity of your deployment pipeline, your framework must treat the original codebase as an immutable baseline, outputting all programmatic hotfixes to an isolated staging build artifact:

1. **The Orchestrator Agent (`agent_debugger.py`):** Programmatically triggers runtime execution, traps active compiler errors, triages the error stream, and outputs a corrected build artifact.
2. **The Evaluator Agent (`eval_debugger.py`):** Acts as an independent governance gate, validating the staging build asset and outputting standardized compliance metrics.

---

### Step 1: Initialize the Immutable Baseline (`system_utilities.py`)

First, create your target application service layer. This file contains a collection of legacy codebase helper utilities riddled with intentional formatting, runtime, and syntax faults.

Create a file named `system_utilities.py` and populate it with the following baseline implementation:

```python
# Core System Utilities Layer - Project Horizon Baseline

# Fault 1: SyntaxError (Mismatched bracket/parenthesis truncation)
def print_items(items):
    for i in range(len(items)):
        print(items[i

# Fault 2: NameError (Implicit variable tracking typo)
def circle_area(radius):
    return 3.14 * radius * radus

# Fault 3: ZeroDivisionError (Unhandled mathematical bounds hazard)
def divide(a, b):
    return a / b

# Fault 4: Logical/Syntax Mismatch (Token assignment instead of comparison)
def check_name(name):
    if name = "":
        return True
    return False

if __name__ == "__main__":
    print("Running system quality diagnostics...")
    try: print_items([1, 2, 3])
    except: pass
    try: print(circle_area(5))
    except: pass
    try: print(divide(10, 0))
    except: pass
    try: check_name("Clark")
    except: pass

```

---

### Step 2: Build the Orchestrator Triage Agent (`agent_debugger.py`)

Your second task is to build the automation engine that mimics an engineer's debugging cycle: it runs the script, captures the active compiler bottleneck via the standard error stream, resolves it, and iterates until the runtime environment returns a clean exit code.

Create `agent_debugger.py` to meet the following engineering specifications:

* **Immutable Inputs:** Your script must read from the baseline file (`system_utilities.py`) but **never mutate it directly**. All ongoing refactoring loops must happen in-memory or be saved to a standalone staging file.
* **Isolated Target Output:** The final, error-free output buffer must be written to a brand-new staging file named `system_utilities_healed.py`.
* **Multi-Pass Convergence Loop:** Configure an execution cycle (up to 5 iterations) to continuously capture downstream exceptions that surface once earlier blockers are eliminated.
* **Process Interception:** Utilize Python’s `subprocess.run()` with `capture_output=True` to trap raw console outputs without causing the orchestrator itself to crash.
* **Traceback-Driven Triage:** Route your code modifications by analyzing the error keywords found inside the runtime's `stderr` channel (e.g., matching exception signatures like `ZeroDivisionError`, `NameError`, or specific line failures) rather than executing blind string swaps.
* **Pipeline Telemetry:** Upon cycle completion, compile an automated diagnostic summary named `debugging_report.md` logging the trapped tracebacks and applied programmatic overrides.

> 💡 **Design Constraint:** Ensure all patch algorithms are strictly **idempotent**. The script generation layer must safeguard its corrections so that consecutive loop runs do not stack duplicated or corrupt syntax elements (such as appending redundant closing characters `])])`).

---

### Step 3: Implement the Independent Governance Gate (`eval_debugger.py`)

To prevent a conflict of interest in automated workflows, the tool that alters a software asset must never be the tool that signs off on its production readiness. You will build a separate validation gate.

Create `eval_debugger.py` to perform a **hybrid structural-and-semantic validation audit**:

1. **Compilation Check:** It must programmatically execute the staging build artifact (`system_utilities_healed.py`) and verify that it achieves a clean compilation exit code of `0`.
2. **Telemetry Validation:** It must verify the physical presence of `debugging_report.md` and check that the orchestrator logged valid patch data.
3. **Structured Schema Export:** It must format the final certification status into a standardized JSON token named `eval_results.json` adhering to this schema:

```json
{
  "status": "APPROVED" or "REJECTED",
  "score": 100 or 0,
  "raw_ai_critique": "A brief structural analysis statement detailing pipeline verification criteria."
}

```

---

### Step 4: Execute the Multi-Agent Pipeline

Once your automation scripts are ready, flush any historical tracking indicators out of your directory workspace and execute the pipeline end-to-end within your command line terminal:

```bash
# Clean out previous execution traces
rm -f eval_results.json debugging_report.md system_utilities_healed.py

# Step 1: Run the Self-Healing Orchestration Agent
python agent_debugger.py

# Step 2: Run the Independent Compliance Evaluator Gate
python eval_debugger.py

```

---

### Step 5: Verification & System Audit

To confirm that your autonomous loop is operating optimally, audit your workspace outputs:

* **`system_utilities.py`:** Check the file to ensure it remains completely untouched and retains its original buggy baseline code.
* **`system_utilities_healed.py`:** Confirm that this file exists and contains the syntactically correct print methods, repaired variable names, zero-division protective blocks, and proper comparison operators (`==`).
* **`eval_results.json`:** Verify that the file displays an `"APPROVED"` status parameter coupled with a perfect engineering score of `100`.