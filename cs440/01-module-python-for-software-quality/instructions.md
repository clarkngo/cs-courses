# Lab Manual: Multi-Agent Software Quality Assurance (SQA) Loop

## Objective

In this lab, you will transition from manual debugging to building an autonomous, traceback-driven self-healing pipeline. You will construct a two-agent architecture:

1. **The Orchestrator Agent (`agent_debugger.py`):** Programmatically executes code, traps system tracebacks, and applies automated hotfixes.
2. **The Evaluator Agent (`eval_debugger.py`):** Acts as an independent quality gate, validating the system state and outputting standardized compliance metrics.

---

### Step 1: Initialize the Target Code Baseline (`hos01.py`)

First, create your target file containing common software faults that your automation loop must identify and resolve.

Create a file named `hos01.py` and populate it with the following flawed implementation:

```python
# Fault 1: SyntaxError (Mismatched bracket formatting)
def print_items(items):
    for i in range(len(items)):
        print(items[i

# Fault 2: NameError (Variable typo tracking)
def circle_area(radius):
    return 3.14 * radius * radus

# Fault 3: ZeroDivisionError (Unhandled mathematical edge case)
def divide(a, b):
    return a / b

# Fault 4: Logical/Syntax Mismatch (Assignment instead of equality comparison)
def check_name(name):
    if name = "":
        return True
    return False

if __name__ == "__main__":
    print("Running Quality Controls...")
    try: print_items([1, 2, 3])
    except: pass
    try: print(circle_area(5))
    except: pass
    try: print(divide(10, 0))
    except: pass
    try: check_name("Student")
    except: pass

```

---

### Step 2: Build the Orchestrator Triage Agent (`agent_debugger.py`)

Your first task is to build an automation agent that mimics a human engineer: it runs the script, reads the error stream (`stderr`), fixes the *active* blocker, and repeats until the compiler is satisfied.

Create `agent_debugger.py`. Your script must satisfy these core technical requirements:

* Utilize a multi-pass loop (up to 5 iterations) to catch cascading, sequential bugs.
* Use Python's `subprocess.run()` with `capture_output=True` to trap runtime exceptions cleanly without crashing the orchestrator itself.
* Implement a **Traceback Triage routing mechanism** that targets string signatures inside the compiler error message rather than scanning raw code strings.
* Automatically write a compliance artifact named `debugging_report.md` detailing every error caught and patch applied.

> **Key Design Concept:** Ensure your string mutations are *idempotent*. If a fix has already been applied in Pass 1, your code must not duplicate or stack modifiers in Pass 2.

---

### Step 3: Implement the Independent Governance Gate (`eval_debugger.py`)

In automated software development, the entity that fixes the code should never be the entity that grades or signs off on it. You will now build an independent evaluator script.

Create `eval_debugger.py`. It must programmatically verify the system state by performing a **hybrid structural-and-semantic validation check**:

1. It must execute the modified `hos01.py` file to verify it returns an exit code of `0` (clean compilation).
2. It must verify that `debugging_report.md` exists and contains the programmatic logs.
3. It must output the final verdict strictly formatted to a standardized JSON schema named `eval_results.json` matching this layout:

```json
{
  "status": "APPROVED" or "REJECTED",
  "score": 100 or 0,
  "raw_ai_critique": "Detailed analysis string here."
}

```

---

### Step 4: Execute the Multi-Agent Lifecycle

Once your architecture is fully constructed, run the entire automation loop sequentially inside your development environment terminal:

```bash
# Clear any historical execution tracking artifacts
rm -f eval_results.json debugging_report.md

# Trigger the Orchestrator to step through and heal the file target
python agent_debugger.py

# Trigger the Evaluator to verify compliance and output your grade metrics
python eval_debugger.py

```

### Step 5: Verification & Verification Audit

To verify your pipeline works flawlessly, open your workspace files and confirm the following:

* **`hos01.py`:** Check the file to ensure the typos are cleared, the print bracket is closed, the equality comparison uses `==`, and the division method has a defensive `if b == 0:` guard rail.
* **`eval_results.json`:** Confirm that your grading matrix registers a passing score of `100` and an `"APPROVED"` status string.
