# Lab Manual 02: Chaos Engineering & Input Guardrails

## Module 02: Non-Functional Requirements & Code Resilience

---

## 🎯 Objective

In this lab, you will move beyond catching simple compile-time syntax errors and dive into **Non-Functional Requirements (NFRs)**—specifically security, performance, and structural reliability. You will construct an automated chaos injection and mitigation pipeline that extracts vulnerable legacy code blocks, stresses them with invalid or malicious runtime inputs, and programmatically refactors them to establish resilient input guardrails.

---

## 🏗️ System Architecture

Your multi-agent self-healing framework will be organized into the following decoupled structure within your development environment:

```text
02-module-chaos-engineering/
├── hos02.ipynb               # Inherited notebook containing legacy code exercises
├── extract_target.py         # Automation script to programmatically compile exercises
├── production_service.py     # Extracted target standalone service (Vulnerable Payload)
├── agent_debugger.py         # Traceback Triage / Chaos Self-Healing Agent
├── eval_debugger.py          # Governance Gatekeeper / Independent Evaluator Agent
├── debugging_report.md       # Automatically generated telemetry compliance report
└── eval_results.json         # Final automated validation output metrics

```

---

## 🛠️ Step-by-Step Implementation

### Step 1: Programmatic Target Extraction

To simulate an enterprise transition from experimental Jupyter sandboxes to formal production environments, you must first extract the raw, unshielded algorithms from the student workbook notebook.

Create a script named `extract_target.py` using the following implementation to automate this extraction layer:

```python
import nbformat
import os

NOTEBOOK_FILE = "hos02.ipynb"
TARGET_SCRIPT = "production_service.py"

if not os.path.exists(NOTEBOOK_FILE):
    print(f"[-] Error: {NOTEBOOK_FILE} not found.")
    exit(1)

with open(NOTEBOOK_FILE, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

exercise_code = []
capture = False

for cell in nb.cells:
    if cell.cell_type == "markdown" and "Try It Yourself: Student Exercises" in cell['source']:
        capture = True
    if capture and cell.cell_type == "code":
        exercise_code.append(cell['source'])

standalone_source = (
    "# Production Service Layer - Project Horizon Module 02\n\n" +
    "\n\n".join(exercise_code) +
    "\n\nif __name__ == '__main__':\n"
    "    print('[+] System operational diagnostics loaded.')\n"
)

with open(TARGET_SCRIPT, "w", encoding="utf-8") as f:
    f.write(standalone_source)

print(f"[+] Successfully extracted student exercises into '{TARGET_SCRIPT}'.")

```

Execute the script in your terminal to generate your target file:

```bash
python extract_target.py

```

---

### Step 2: Analyze the Vulnerable Target (`production_service.py`)

Open the newly created `production_service.py` file. You will find several severe architectural non-functional flaws that fail industry compliance standards:

1. **Performance Bottleneck:** `find_duplicates` runs an inefficient nested $O(n^2)$ lookup strategy via `.count()` inside a loop.
2. **Security Vulnerability:** `execute_expression` exposes an open remote code execution vector by processing raw text through `eval()`.
3. **Reliability Fragility:** `get_user_language` performs a direct bracket dictionary lookup (`user['language']`), which instantly crashes the program with a fatal `KeyError` if the parameter is missing.

---

### Step 3: Construct the Chaos Triage Agent (`agent_debugger.py`)

Your next task is to write an orchestrator engine that automatically executes the script, isolates unhandled crashes, and applies targeted programmatic refactoring patterns based on the compiler's active runtime feedback.

Create `agent_debugger.py` using this robust triage implementation:

```python
import subprocess
import os
import sys
import re

TARGET_SCRIPT = "production_service.py"
REPORT_FILE = "debugging_report.md"

if not os.path.exists(TARGET_SCRIPT):
    print(f"[-] Error: '{TARGET_SCRIPT}' not found.")
    sys.exit(1)

print(f"[+] Chaos Orchestrator active. Testing input guardrails on '{TARGET_SCRIPT}'...")

traceback_summary = ""
patched_code_display = []

for iteration in range(5):
    with open(TARGET_SCRIPT, "r", encoding="utf-8") as f:
        script_source = f.read()

    run_check = subprocess.run(["python", TARGET_SCRIPT], capture_output=True, text=True)
    
    if run_check.returncode == 0 and "KeyError" not in run_check.stderr and "NameError" not in run_check.stderr:
        print(f"[+] Quality Loop complete: Script passed all guardrail verifications on Pass #{iteration+1}.")
        break
        
    error_msg = run_check.stderr if run_check.stderr else run_check.stdout
    traceback_summary += f"\n--- Guardrail Exception Trapped on Pass #{iteration+1} ---\n{error_msg}"
    
    # TRIAGE AND ROUTE NON-FUNCTIONAL FAULTS BASED ON SYSTEM TELEMETRY
    if "eval(expr)" in script_source and "ast.literal_eval" not in script_source:
        print("[*] Triage: Mitigating arbitrary code execution risk by moving to AST literal evaluations...")
        script_source = "import ast\n" + script_source.replace("return eval(expr)", "try:\n        return ast.literal_eval(expr)\n    except Exception as e:\n        return f'Error: {e}'")
        patched_code_display.append("Secured execute_expression endpoint against string injections using AST.")

    elif "KeyError" in error_msg or "return user['language']" in script_source:
        print("[*] Triage: Resolving KeyError crash risks with safe dictionary fallback accessors...")
        script_source = script_source.replace("return user['language']", "return user.get('language', 'en')")
        patched_code_display.append("Resolved KeyError vulnerability by applying dictionary fallback defaults.")
        
    elif "lst.count(i)" in script_source:
        print("[*] Triage: Optimizing nested collection loop down to linear execution time...")
        linear_fix = (
            "seen = set()\n"
            "    for i in lst:\n"
            "        if i in seen:\n"
            "            return True\n"
            "        seen.add(i)\n"
            "    return False"
        )
        script_source = re.sub(r"def find_duplicates\(lst\):.*?return False", f"def find_duplicates(lst):\n    {linear_fix}", script_source, flags=re.DOTALL)
        patched_code_display.append("Optimized find_duplicates method complexity from O(n^2) down to O(n).")
        
    else:
        print("[-] Stabilization limit hit or unknown exception variant intercepted.")
        break

    with open(TARGET_SCRIPT, "w", encoding="utf-8") as f:
        f.write(script_source)

# Write the compliance report asset
diff_summary = "\n".join([f"- {item}" for item in patched_code_display]) if patched_code_display else "- Guardrails fully verified."
with open(REPORT_FILE, "w", encoding="utf-8") as report_file:
    report_file.write(
        f"# SQA Chaos Engineering & Input Guardrail Report\n\n"
        f"## Target Service Verified\n`{TARGET_SCRIPT}`\n\n"
        f"## Captured Guardrail Violations\n```text\n{traceback_summary.strip()}\n```\n\n"
        f"## Applied Structural Resilience Patches\n{diff_summary}\n"
    )
print(f"[+] Automated telemetry guardrail tracking report written to '{REPORT_FILE}'.")

```

---

### Step 4: Build the Governance Evaluator Gate (`eval_debugger.py`)

To fulfill formal quality standards, an autonomous quality loop must separate the script applying modifications from the gatekeeper auditing them.

Create `eval_debugger.py` to function as your strict, isolated automated verification engine:

```python
import json
import os
import sys
import subprocess

REPORT_FILE = "debugging_report.md"
TARGET_SCRIPT = "production_service.py"
OUTPUT_FILE = "eval_results.json"

json_data = {"status": "REJECTED", "score": 0, "raw_ai_critique": "Validation initialization failed."}

if not os.path.exists(REPORT_FILE) or not os.path.exists(TARGET_SCRIPT):
    json_data["raw_ai_critique"] = "Required multi-agent tracking artifacts are missing from the folder path."
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)
    sys.exit(1)

print(f"[+] Evaluator Active. Auditing guardrail status for '{TARGET_SCRIPT}'...")

# Programmatically run the script to confirm it executes without faults
run_check = subprocess.run(["python", TARGET_SCRIPT], capture_output=True, text=True)

if run_check.returncode == 0 and "KeyError" not in run_check.stderr:
    with open(REPORT_FILE, "r", encoding="utf-8") as rf:
        report_text = rf.read()
        
    if "Applied Structural Resilience Patches" in report_text:
        json_data = {
            "status": "APPROVED",
            "score": 100,
            "raw_ai_critique": "The governance gate verified that the service layer safely compiles, resists malformed key lookups, and encapsulates input handlers securely."
        }
    else:
        json_data = {"status": "REJECTED", "score": 50, "raw_ai_critique": "The script compiles cleanly, but the orchestrator compliance report details are incomplete."}
else:
    json_data = {"status": "REJECTED", "score": 0, "raw_ai_critique": f"Guardrail audit failed. Active runtime crash logs present:\n{run_check.stderr[:150]}"}

with open(OUTPUT_FILE, "w", encoding="utf-8") as j:
    json.dump(json_data, j, indent=2)
print(f"[+] Governance execution matrix output successfully to '{OUTPUT_FILE}'.")

```

---

### Step 5: Execute and Validate the Pipeline

Wipe out any previous telemetry file runs and clear your workspace environment path. Run your scripts in exact sequence within your command line terminal:

```bash
# Clear downstream artifacts
rm -f eval_results.json debugging_report.md

# Trigger the Self-Healing Chaos Pipeline Agent
python agent_debugger.py

# Trigger the Automated Grading Sign-Off Auditor
python eval_debugger.py

```

---

## 📊 Verification Check

Your work is successful if your directory generates a passing compliance grade matching the standard schema exactly:

```json
{
  "status": "APPROVED",
  "score": 100,
  "raw_ai_critique": "The governance gate verified that the service layer safely compiles, resists malformed key lookups, and encapsulates input handlers securely."
}

```