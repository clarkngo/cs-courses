# Lab Manual: Chaos Engineering & Input Guardrails

## Objective

In this lab, you will transition from catching simple compile-time syntax errors to defending a production system against non-functional vulnerabilities (NFRs)—specifically performance bottlenecks, security flaws, and structural fragility. You will construct a two-agent chaos injection and self-healing pipeline.

To preserve the integrity of your deployment pipeline, your framework must treat the original codebase as an immutable baseline, outputting all programmatic hotfixes to an isolated staging build artifact:

1. **The Orchestrator Agent (`agent_debugger.py`):** Programmatically triggers runtime execution, traps input violations or system tracebacks, triages the error streams, and outputs a corrected build artifact.
2. **The Evaluator Agent (`eval_debugger.py`):** Acts as an independent governance gate, validating the staging build asset and outputting standardized compliance metrics.

---

### Step 1: Initialize the Immutable Baseline (`production_service.py`)

First, create your target application service layer. This file contains a collection of legacy codebase functions riddled with severe non-functional defects, including arbitrary code execution vectors, inefficient algorithms, and unhandled collection lookup exceptions.

Create a file named `production_service.py` and populate it with the following baseline implementation:

```python
# Production Service Layer - Project Horizon Baseline

# Fault 1: Performance Bottleneck (Inefficient O(n²) nested loop algorithm)
def find_duplicates(lst):
    for i in lst:
        if lst.count(i) > 1:
            return True
    return False

print(find_duplicates([1, 2, 3, 4, 5, 1]))

# Fault 2: Security Vulnerability (Arbitrary code execution via raw input eval)
def execute_expression(expr):
    return eval(expr)

print(execute_expression("os.system('rm -rf /')"))

# Fault 3: Maintainability Flaw (Hardcoded infrastructure parameters)
def connect():
    host = 'localhost'
    port = 3306
    print(f"Connecting to {host}:{port}")

connect()

# Fault 4: Readability Bloat (Verbose and redundant boolean logic check)
def is_true(val):
    if val == True:
        return True
    else:
        return False

print(is_true(True))

# Fault 5: Reliability Hazard (Direct key access vulnerable to fatal KeyErrors)
def get_user_language(user):
    return user['language']

print(get_user_language({'name': 'Alice'}))

if __name__ == '__main__':
    print('[+] System operational diagnostics loaded.')

```

---

### Step 2: Build the Orchestrator Triage Agent (`agent_debugger.py`)

Your second task is to build the automation engine that identifies non-functional flaws. It must programmatically run the script, capture active runtime behavior or telemetry data via standard streams, isolate weaknesses, and execute target modifications before compiling a hardened staging script.

Create `agent_debugger.py` to meet the following engineering specifications:

* **Immutable Inputs:** Your script must read from the baseline file (`production_service.py`) but **never mutate it directly**. All ongoing refactoring loops must happen in-memory or be saved to a standalone staging file.
* **Isolated Target Output:** The final, hardened output buffer must be written to a brand-new staging file named `production_service_healed.py`.
* **Multi-Pass Convergence Loop:** Configure an execution cycle (up to 5 iterations) to continuously capture downstream errors that surface once earlier blockers or vulnerabilities are eliminated.
* **Process Interception:** Utilize Python’s `subprocess.run()` with `capture_output=True` to trap both raw console output and error streams cleanly.
* **Traceback-Driven Triage:** Route your code modifications by analyzing error keywords found inside the runtime's `stderr` channel or tracking structural signatures within the string context. Your rules must explicitly mitigate:
* Code injection risks by stripping arbitrary `eval()` execution vectors and replacing them with safe abstract syntax trees like `ast.literal_eval()`.
* Reliability crashes by swapping unshielded dictionary lookups with default fallback parameters.
* Computational complexity bottlenecks by refactoring nested `O(n²)` lookup arrays into linear-time `O(n)` hashing sets.


* **Pipeline Telemetry:** Upon cycle completion, compile an automated diagnostic summary named `debugging_report.md` logging the trapped tracebacks and applied structural changes.

> 💡 **Design Constraint:** Ensure all patch algorithms are strictly **idempotent**. The script generation layer must safeguard its corrections so that consecutive loop runs do not stack duplicated or corrupt syntax elements into the staging target.

---

### Step 3: Implement the Independent Governance Gate (`eval_debugger.py`)

To prevent a conflict of interest in automated development lifecycles, the tool that alters a software asset must never be the tool that signs off on its production readiness. You will build a separate validation gate script.

Create `eval_debugger.py` to perform a **hybrid structural-and-semantic validation audit**:

1. **Compilation & Guardrail Check:** It must programmatically execute the staging build artifact (`production_service_healed.py`) and verify that it achieves a clean compilation exit code of `0` and contains no lingering `KeyError` signatures in its error buffers.
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
rm -f eval_results.json debugging_report.md production_service_healed.py

# Step 1: Run the Self-Healing Chaos Pipeline Agent
python agent_debugger.py

# Step 2: Run the Independent Compliance Evaluator Gate
python eval_debugger.py

```

---

### Step 5: Verification & System Audit

To confirm that your autonomous loop is operating optimally, audit your workspace outputs:

* **`production_service.py`:** Check the file to ensure it remains completely untouched and retains its original buggy baseline code.
* **`production_service_healed.py`:** Confirm that this file exists and contains the syntactically secure `ast.literal_eval()` calls, dictionary queries using fallback `.get()` defaults, simplified boolean evaluations, and linear-time `O(n)` duplication checks.
* **`eval_results.json`:** Verify that the file displays an `"APPROVED"` status parameter coupled with a perfect engineering score of `100`.