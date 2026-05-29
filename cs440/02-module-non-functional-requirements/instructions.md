# Lab Manual: Chaos Engineering & Input Guardrails

## Objective

In this lab, you will transition from catching simple compile-time syntax errors to defending a production system against non-functional vulnerabilities (NFRs)—specifically performance bottlenecks, security flaws, and structural fragility. You will construct a two-agent chaos injection and self-healing pipeline:

1. **The Orchestrator Agent (`agent_debugger.py`):** Programmatically triggers runtime execution, traps input violations or system tracebacks, and applies automated refactoring patches.
2. **The Evaluator Agent (`eval_debugger.py`):** Acts as an independent quality gate, verifying the updated code state and outputting standardized compliance metrics.

---

### Step 1: Initialize the Target Code Baseline (`production_service.py`)

First, create your target application service layer containing the unshielded legacy functions that your automation loop must identify and harden.

Create a file named `production_service.py` and populate it with the following baseline implementation:

```python
# Production Service Layer - Project Horizon Module 02

def find_duplicates(lst):
    for i in lst:
        if lst.count(i) > 1:
            return True
    return False

print(find_duplicates([1, 2, 3, 4, 5, 1]))

def execute_expression(expr):
    return eval(expr)

print(execute_expression("os.system('rm -rf /')"))

def connect():
    host = 'localhost'
    port = 3306
    print(f"Connecting to {host}:{port}")

connect()

def is_true(val):
    if val == True:
        return True
    else:
        return False

print(is_true(True))

def get_user_language(user):
    return user['language']

print(get_user_language({'name': 'Alice'}))

if __name__ == '__main__':
    print('[+] System operational diagnostics loaded.')

```

---

### Step 2: Build the Orchestrator Triage Agent (`agent_debugger.py`)

Your second task is to build an automation agent capable of triaging non-functional flaws. It must programmatically run the script, read the standard output or error streams, isolate runtime vulnerabilities, and apply programmatic refactoring patterns based on active feedback.

Create `agent_debugger.py` to meet the following strict technical specifications:

* **Multi-Pass Logic:** Implement an execution loop that runs for up to 5 iterations to dynamically catch cascading or sequential runtime errors as previous blocks are patched.
* **Process Capturing:** Use Python’s `subprocess.run()` with `capture_output=True` and `text=True` to trap execution states without crashing the orchestrator engine.
* **Traceback Triage Routing:** Route your healing modifications using the text content inside `stderr` or `stdout`. Your rules must intercept specific signatures:
* Catch arbitrary code injection vulnerabilities stemming from `eval(expr)` usage.
* Catch data lookup crash risks resulting from unmitigated `KeyError` exceptions.
* Catch performance bottlenecks driven by nested $O(n^2)$ lookup algorithms like `.count()` within loops.


* **Automated Logging:** The script must write a markdown audit log named `debugging_report.md` that chronicles the exact exceptions trapped and the specific mitigation rules fired.

> 💡 **Design Constraint:** Your self-healing hotfixes must be **idempotent**. The agent must explicitly check if a correction is already present before altering the script buffer to avoid recursive code duplication.

---

### Step 3: Implement the Independent Governance Gate (`eval_debugger.py`)

In automated software development lifecycles, the agent implementing code modifications must remain entirely decoupled from the system certifying compliance. You will construct an isolated validator script to serve as your quality gate.

Create `eval_debugger.py` to programmatically execute a **hybrid structural-and-semantic validation check**:

1. **Compilation Guard:** It must run the modified `production_service.py` to confirm that the script terminates with an exit code of `0` and contains no lingering `KeyError` signatures in its error buffers.
2. **Telemetry Validation:** It must confirm the physical existence of `debugging_report.md` and check that the file features populated execution headers.
3. **Structured Metrics Export:** It must compile its final compliance verdict and output it directly to a file named `eval_results.json` adhering strictly to this layout:

```json
{
  "status": "APPROVED" or "REJECTED",
  "score": 100 or 0,
  "raw_ai_critique": "A brief structural analysis statement detailing pipeline pass/fail criteria."
}

```

---

### Step 4: Execute the Multi-Agent Lifecycle

Once your scripts are compiled, clear any downstream artifacts and execute the entire automated engineering pipeline sequentially inside your terminal environment:

```bash
# Clear downstream tracking artifacts
rm -f eval_results.json debugging_report.md

# Trigger the Orchestrator to step through and apply input guardrails
python agent_debugger.py

# Trigger the Evaluator to verify compliance and compile your metrics
python eval_debugger.py

```

---

### Step 5: Verification & Verification Audit

To verify that your autonomous pipeline operates properly, inspect your workspace files and confirm the following post-execution properties:

* **`production_service.py`:** Confirm that `eval()` has been cleanly stripped or wrapped in safe abstract syntax handlers (`ast.literal_eval`), dictionary queries utilize fallback `.get()` defaults, and the duplicate evaluator functions run in linear time complexity ($O(n)$) using hashing collections.
* **`eval_results.json`:** Confirm that your grading matrix registers an `"APPROVED"` status parameter and a full score of `100`.