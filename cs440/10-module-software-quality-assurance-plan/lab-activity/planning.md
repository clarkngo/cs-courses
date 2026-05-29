Moving into **Module 10**, we conclude the technical quality assurance sequence with **Software Quality Assurance Plans (SQAP) & Compliance Framework Documentation**.

Following the provisions of standard SQAP templates (such as **IEEE 730 standard requirements** for software quality governance) outlined in your course materials, an SQAP must establish an unblemished organizational blueprint. This requires ensuring that all core sections have documented operational values and that foundational references are thoroughly verified.

The baseline script models a configuration validator that triggers runtime exception tracking flags (`SQAPValidationError` and `MissingReferencesError`) when it encounters incomplete management fields or unverified references. Students will develop an orchestration layer that catches these missing configuration blocks exclusively via the standard error track (`stderr`) and dynamically injects compliant default mappings inside an isolated staging artifact.

---

## 🏗️ Module 10 Architecture Directory Map

```text
10-module-sqa-plan/
├── sqap_manager.py               # Immutable Baseline (SQAP validation module with missing data blocks)
├── agent_debugger.py             # SQA Orchestrator (Traps compliance exceptions -> builds staging asset)
├── sqap_manager_healed.py        # Staging Target Output (Generates fully complete compliant SQAP configuration)
├── eval_debugger.py              # Universal Governance Agent (Verifies execution and report tracking)
├── debugging_report.md           # Pipeline verification report (Passes structural check)
└── eval_results.json             # Final automated validation grading token

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
    "KeyError" in run_check.stderr
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

### 2. Module 10 Orchestrator Solution (`agent_debugger.py`)

*This master solution processes compliance structural warnings exclusively via the runtime `stderr` stream, maintaining flat-indentation replacements to guarantee clean compilation.*

```python
import subprocess
import os
import sys

SRC_SCRIPT = "sqap_manager.py"
HEALED_SCRIPT = "sqap_manager_healed.py"
REPORT_FILE = "debugging_report.md"

if not os.path.exists(SRC_SCRIPT):
    print(f"[-] Error: '{SRC_SCRIPT}' not found.")
    sys.exit(1)

print(f"[+] SQAP Compliance Orchestrator active. Seeding staging target from '{SRC_SCRIPT}'...")

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
        print(f"[+] Quality Loop complete: SQAP configuration boundaries stabilized on Pass #{iteration+1}.")
        break
        
    error_msg = run_check.stderr if run_check.stderr else run_check.stdout
    traceback_summary += f"\n--- Compliance Blueprint Gap Caught on Pass #{iteration+1} ---\n{error_msg}"
    
    # TRIAGE ROUTING STREAM EXCLUSIVELY DRIVEN BY THE ACTIVE RUNTIME ERROR PAYLOAD
    if "SQAPValidationError" in error_msg:
        print("[*] Triage: Injecting default compliant text fields into mandatory SQAP sections...")
        sqap_patch = (
            "print('[+] Initializing missing metadata with compliant defaults.')\n"
            "        plan_data['purpose'] = 'Defines the software quality governance criteria for Project Horizon.'\n"
            "        plan_data['management'] = 'Establishes oversight roles, organizational structures, and auditing tasks.'"
        )
        script_source = script_source.replace('raise ValueError("SQAPValidationError: Mandatory SQAP sections (\'purpose\', \'management\') are empty or unassigned.")', sqap_patch)
        patched_code_display.append("Populated mandatory SQAP metadata definitions to guarantee section coverage values (IEEE 730 guidelines).")
        
    elif "MissingReferencesError" in error_msg:
        print("[*] Triage: Re-establishing verified references citation logs...")
        ref_patch = (
            "print('[!] Reference gap detected. Appending verified compliance standards.')\n"
            "        plan_data['references'] = ['IEEE Std 730-2014 Standard for Software Quality Assurance Processes']"
        )
        script_source = script_source.replace('raise KeyError("MissingReferencesError: SQAP reference citations are completely empty or unverified.")', ref_patch)
        patched_code_display.append("Injected verified industry standards references to satisfy regulatory tracking matrices.")
    else:
        print("[-] Target stabilization threshold reached or unmapped validation profile trapped.")
        break

    with open(HEALED_SCRIPT, "w", encoding="utf-8") as f:
        f.write(script_source)

# Write out output audit report containing the exact token phrase "Audited" to pass governance
diff_summary = "\n".join([f"- {item}" for item in patched_code_display]) if patched_code_display else "- Compliance blueprints verified."
with open(REPORT_FILE, "w", encoding="utf-8") as report_file:
    report_file.write(
        f"# SQA Plan Compliance Verification & Audit Report\n\n"
        f"## Target File Audited\n`{SRC_SCRIPT}`\n\n"
        f"## Captured Guardrail Violations\n```text\n{traceback_summary.strip()}\n```\n\n"
        f"## Applied Structural Resilience Patches\n{diff_summary}\n"
    )
print(f"[+] Automated software quality plan telemetry report compiled at '{REPORT_FILE}'.")

```

---

## 📝 Complete Student Lab Manual

# Lab Manual: Software Quality Assurance Plans & Compliance Frameworks

## Objective

In this laboratory, you will explore high-level system governance and project release readiness by mastering **Software Quality Assurance Plan (SQAP) Compliance Frameworks**. Under formal software validation guidelines (such as the **IEEE 730 SQAP standard**), engineering organizations must define explicit quality goals, process controls, and management structures before signing off on deployment readiness. If an application registry encounters unpopulated governance fields or unverified standard references, the deployment lacks an audit trail, failing institutional compliance reviews.

You will engineer an autonomous self-healing governance engine inside **`agent_debugger.py`**. Your script will execute a defective analytical service layer, capture custom dashboard tracking failures from standard error buffers, and programmatically patch the math functions to deploy defensive fallbacks and boundary-clamping logic.

To protect the integrity of your continuous deployment baseline, your automated scripts must treat the initial tracking module as immutable, exporting all programmatic modifications to a separate staging build file:

1. **The Orchestrator Agent (`agent_debugger.py`):** Programmatically triggers validation executions, reads stderr trace logs to flag compliance gaps, and exports a repaired staging file.
2. **The Evaluator Agent (`eval_debugger.py`):** An environment-agnostic universal quality gate pre-provided in your repository track that executes your staging targets to verify production readiness.

---

### Step 1: Initialize the Immutable Baseline (`sqap_manager.py`)

First, initialize your baseline quality plan module. This script models an internal software review validation harness that checks for metadata compliance. It contains two distinct structural defects: it crashes with an explicit `SQAPValidationError` if mandatory fields are unpopulated, and it fails with a `MissingReferencesError` if reference citation trackers remain empty.

Create a file named **`sqap_manager.py`** and populate it with this baseline implementation:

```python
# Software Quality Assurance Plan Manager Layer - Project Horizon Baseline
import sys
import json

def validate_sqap_fields(plan_data):
    print("[*] Auditing Software Quality Assurance Plan (SQAP) fields...")
    
    # FAULT 1: Missing section content values. All mandatory fields must contain records.
    if not plan_data.get("purpose") or not plan_data.get("management"):
        raise ValueError("SQAPValidationError: Mandatory SQAP sections ('purpose', 'management') are empty or unassigned.")
        
    return True

def verify_sqap_references(plan_data):
    print("[*] Verifying SQAP reference citations...")
    
    # FAULT 2: Missing reference logs. References must be documented and verified.
    if not plan_data.get("references") or len(plan_data["references"]) == 0:
        raise KeyError("MissingReferencesError: SQAP reference citations are completely empty or unverified.")
        
    return True

if __name__ == "__main__":
    print("[*] Loading Software Quality Assurance Plan compliance framework...")
    
    # Initial incomplete configuration setup designed to trigger sequential passes
    mock_plan = {
        "purpose": "",
        "management": "",
        "references": []
    }
    
    try:
        validate_sqap_fields(mock_plan)
    except Exception as e:
        print(f"[-] Blocked by SQAP section checker: {e}", file=sys.stderr)
        raise e
        
    try:
        verify_sqap_references(mock_plan)
    except Exception as e:
        print(f"[-] Blocked by reference auditor: {e}", file=sys.stderr)
        raise e

```

---

### Step 2: Build the Orchestrator Triage Agent (`agent_debugger.py`)

Your primary engineering challenge is to write the automated SQAP compliance orchestrator script. Your program must read the baseline code module, execute it within isolated system sub-processes, capture individual `SQAPValidationError` and `MissingReferencesError` trace descriptors from `stderr`, and apply targeted substitutions to achieve convergence.

Create **`agent_debugger.py`** to meet the following configuration requirements:

* **Immutable Inputs:** Your script must read from the baseline file (`sqap_manager.py`) but **never alter it directly**. All refactoring transformations must occur in-memory or save directly to a staging file.
* **Isolated Target Output:** Save your final, error-free staging build configuration directly to a new file named `sqap_manager_healed.py`.
* **Multi-Pass Convergence Loop:** Configure an execution cycle (up to 5 iterations) to systematically catch downstream errors that surface as earlier registration blocks are refactored.
* **Process Interception:** Utilize Python’s `subprocess.run()` with `capture_output=True` to trap runtime console outputs safely without causing your orchestrator tool itself to crash.
* **Traceback-Driven Triage:** Direct your refactoring replacements by parsing specific exception keywords found inside the runtime error stream payload (`stderr`) *exclusively* to avoid priority cascade loops. Intercept missing section metadata exceptions to automatically inject compliant default string descriptions. Intercept missing reference errors to dynamically append standard verification identifiers (such as standard IEEE guidelines) into the dictionary layout.
* **Pipeline Telemetry:** Upon convergence, save an automated execution summary named `debugging_report.md` detailing the trapped exceptions and specific patch rules fired.

> 💡 **Design Constraint:** Ensure all patch blocks are strictly **idempotent**. Your script generator layer must explicitly protect its updates so that subsequent loop checks do not append duplicate or stacked logic configurations.

---

### Step 3: Run the Pre-Configured Governance Gate (`eval_debugger.py`)

Your repository directory includes an immutable automated release runner named **`eval_debugger.py`**. Do not modify this file. It scans your environment workspace to complete a **hybrid structural-and-semantic validation audit**:

1. **Dynamic Target Discovery:** Scans directory paths dynamically using text pattern wildcards (e.g., `glob.glob("*_healed.py")`) to capture and evaluate the target staging build artifact.
2. **Compilation Guard:** Runs your staging script file to confirm it successfully completes configuration loops with an exit status of `0` and throws zero lingering traceback crash exceptions.
3. **Telemetry Substring Verification:** Confirms that your generated `debugging_report.md` exists and contains the strict compliance auditing markdown substring parameters **"Report"** and **"Audited"**.
4. **Structured Schema Export:** Formats final compliance metrics straight into an industry-compliant JSON metadata token named `eval_results.json`.

---

### Step 4: Execute the Multi-Agent Pipeline

Once your automated orchestration layer is complete, flush any historical tracking indicators out of your directory workspace and execute your pipeline end-to-end within your command terminal:

```bash
# Clear downstream tracking artifacts
rm -f eval_results.json debugging_report.md sqap_manager_healed.py

# Step 1: Run your Self-Healing Governance Orchestrator Agent
python agent_debugger.py

# Step 2: Invoke the pre-provided Pipeline Governance Gate
python eval_debugger.py

```

---

### Step 5: Verification & System Audit

To confirm that your autonomous loop is operating optimally, audit your workspace outputs:

* **`sqap_manager.py`:** Check the file to ensure it remains completely untouched and retains its original incomplete specification layout.
* **`sqap_manager_healed.py`:** Confirm that this file exists, resolves mandatory field coverage constraints, injects verified industry standard references, and compiles with a clean exit status code.
* **`eval_results.json`:** Verify that the file displays an `"APPROVED"` status parameter coupled with a perfect engineering score of `100`.