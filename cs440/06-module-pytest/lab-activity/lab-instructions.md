Got it. Let’s separate the infrastructure from the assignment guidelines. In a production-grade CI/CD curriculum, **`eval_debugger.py`** functions as a read-only, black-box grading gate pre-configured in the repository ecosystem, while students are tasked with engineering the dynamic triage logic inside **`agent_debugger.py`**.

Here is the decoupled architecture layout, providing the complete master answer keys first, followed by the clean student lab manual.

---

# 🔑 Master Answer Keys (Instructor & CI/CD Pipeline Layer)

### 1. The Universal Governance Gate (`eval_debugger.py`)

*Deploy this exact script across all laboratory workspaces. It serves as an immutable, environment-agnostic automated release gate.*

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

### 2. Module 06 Orchestrator Solution (`agent_debugger.py`)

```python
import subprocess
import os
import sys

SRC_SCRIPT = "bank_processor.py"
HEALED_SCRIPT = "bank_processor_healed.py"
REPORT_FILE = "debugging_report.md"

if not os.path.exists(SRC_SCRIPT):
    print(f"[-] Error: '{SRC_SCRIPT}' not found.")
    sys.exit(1)

print(f"[+] SQA Test Orchestrator active. Seeding staging target from '{SRC_SCRIPT}'...")

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
        print(f"[+] Quality Loop complete: Test logic boundaries stabilized on Pass #{iteration+1}.")
        break
        
    error_msg = run_check.stderr if run_check.stderr else run_check.stdout
    traceback_summary += f"\n--- Test Validation Masking Intercepted on Pass #{iteration+1} ---\n{error_msg}"
    
    if "per-transaction limit" in error_msg or "account.transfer(15000)" in script_source:
        print("[*] Triage: Refactoring masked boundary condition transaction sequences...")
        
        corrected_sequence = (
            "account.transfer(9000)  # Safe Transaction 1\n"
            "    account.transfer(9000)  # Safe Transaction 2 (Total: 18000)\n"
            "    try:\n"
            "        account.transfer(8000)  # Pushes aggregate to 26000 (Triggers Daily Limit)\n"
            "        raise AssertionError('TestFailed: Daily limit check bypassed.')\n"
            "    except ValueError as e:\n"
            "        if 'daily transfer limit' in str(e):\n"
            "            print('[+] Success: Daily transfer limit guard verified successfully.')\n"
            "        else:\n"
            "            raise e"
        )
        
        script_source = script_source.replace("account.transfer(15000)", corrected_sequence)
        patched_code_display.append("Refactored masked validation calls into safe incremental allocations to evaluate true daily limits.")
    else:
        print("[-] Verification ceiling reached or unknown error signature caught.")
        break

    with open(HEALED_SCRIPT, "w", encoding="utf-8") as f:
        f.write(script_source)

diff_summary = "\n".join([f"- {item}" for item in patched_code_display]) if patched_code_display else "- Test vectors verified."
with open(REPORT_FILE, "w", encoding="utf-8") as report_file:
    report_file.write(
        f"# SQA Test Framework & Boundary Validation Report\n\n"
        f"## Target File Audited\n`{SRC_SCRIPT}`\n\n"
        f"## Captured Guardrail Violations\n```text\n{traceback_summary.strip()}\n```\n\n"
        f"## Applied Structural Resilience Patches\n{diff_summary}\n"
    )
print(f"[+] Automated test telemetry report written out to '{REPORT_FILE}'.")

```

---

## 📝 Revised Student Lab Manual

# Lab Manual: Automated Test Framework Integration & Test Case Masking

## Objective

In this lab, you will complete your automated CI/CD engine progression by mastering **Test Case Masking Remediation and Boundary Condition Analysis**. In enterprise software settings, verification test suites themselves can contain architectural flaws. A poorly structured test case can trigger an unintended validation exception early in its execution thread, completely masking a major design vulnerability downstream.

You will construct an autonomous test engineering validation agent inside **`agent_debugger.py`**. Your framework will analyze transaction boundary limits matching fintech regulations, intercept premature masking errors, and programmatically refactor execution blocks to verify true system thresholds.

To ensure the architectural baseline of your development workspace remains untainted, your automation tools must treat the original software testing module as an immutable asset, exporting all programmatic fixes to a separate staging build file:

1. **The Orchestrator Agent (`agent_debugger.py`):** Programmatically triggers validation executions, processes standard error buffers to isolate masked test exceptions, and exports a repaired staging file.
2. **The Evaluator Agent (`eval_debugger.py`):** An immutable, pre-provided pipeline grading gate that executes your staging builds to verify quality compliance.

---

### Step 1: Initialize the Immutable Baseline (`bank_processor.py`)

First, create your target application transaction service layer. This module features production logic definitions containing a per-transaction limit ($10,000) and a cumulative daily transfer volume limit ($25,000). It also includes an inline verification suite that accidentally masks the daily aggregate limit by attempting a single oversized transfer of $15,000 first.

Create a file named **`bank_processor.py`** and populate it with this baseline implementation:

```python
# Bank Processing & Verification Layer - Project Horizon Baseline
import sys

class BankAccount:
    DAILY_LIMIT = 25000
    TRANSACTION_LIMIT = 10000

    def __init__(self, balance):
        self.balance = balance
        self.daily_transferred = 0

    def transfer(self, amount):
        # Limit Requirement 1: Per-transaction ceiling verification
        if amount > self.TRANSACTION_LIMIT:
            raise ValueError("Transfer exceeds per-transaction limit.")
        # Limit Requirement 2: Cumulative daily volume calculation
        if self.daily_transferred + amount > self.DAILY_LIMIT:
            raise ValueError("Transfer exceeds daily transfer limit.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
            
        self.balance -= amount
        self.daily_transferred += amount
        return True

def verify_limits():
    print("[*] Running system limit boundary test suite...")
    account = BankAccount(50000)
    
    # FAULT: The verification logic intends to audit the cumulative daily threshold ($25,000).
    # However, it attempts a single transfer of $15,000 first.
    # This prematurely trips the per-transaction limit logic ($10,000), masking the downstream validation.
    account.transfer(15000) 
    
    print("[+] Boundary check suite processed successfully.")

if __name__ == "__main__":
    verify_limits()

```

---

### Step 2: Build the Orchestrator Triage Agent (`agent_debugger.py`)

Your primary engineering task is to design the autonomous test suite refactoring orchestrator. Your script must read the baseline code module, execute it within isolated background process pools, catch the premature transaction limit `ValueError` string trace thrown in `stderr`, and apply targeted replacements to cleanly isolate the secondary daily transfer ceiling validation.

Create **`agent_debugger.py`** to meet the following engineering specifications:

* **Immutable Inputs:** Your script must read from the baseline file (`bank_processor.py`) but **never alter it directly**. All refactoring transformations must happen in-memory or be saved to a staging file.
* **Isolated Target Output:** Save your final, hardened code updates to a brand-new staging file named `bank_processor_healed.py`.
* **Multi-Pass Convergence Loop:** Configure an execution cycle (up to 5 iterations) to continuously capture downstream errors that surface once earlier blockers are eliminated.
* **Process Interception:** Utilize Python’s `subprocess.run()` with `capture_output=True` to trap raw standard error channels cleanly without crashing the orchestrator loop.
* **Traceback-Driven Triage:** Route your modifications based on the specific exception text thrown in the runtime stream. Intercept instances where the per-transaction error masks daily limits, and programmatically split the single transaction footprint into distinct, incremental transfer blocks (e.g., allocations under $10,000 each) that successfully test daily capacity thresholds without violating the per-transaction ceiling.
* **Pipeline Telemetry:** Upon convergence, save an automated execution summary named `debugging_report.md` detailing the trapped exceptions and specific patch rules fired.

> 💡 **Design Constraint:** Ensure all patch blocks are strictly **idempotent**. The script generation engine must explicitly verify that corrections do not duplicate or stack recursively across successive testing runs.

---

### Step 3: Run the Independent Governance Gate (`eval_debugger.py`)

Your repository workspace includes a pre-provided, immutable automated release gate runner named **`eval_debugger.py`**. Do not modify this file. It programmatically executes a **hybrid structural-and-semantic validation audit**:

1. **Dynamic Target Discovery:** Automatically scans directory folders using wildcard text patterns (e.g., `glob.glob("*_healed.py")`) to find your generated staging build asset.
2. **Compilation Guard:** Runs your staging script file to confirm it successfully completes execution tracking loops with a standard exit code of `0` and throws zero lingering traceback crash exceptions.
3. **Telemetry Substring Verification:** Confirms that your generated `debugging_report.md` exists and contains the strict compliance auditing markdown substring parameters **"Report"** and **"Audited"**.
4. **Structured Schema Export:** Formats final metrics straight into an industry-compliant JSON metadata token named `eval_results.json`.

---

### Step 4: Execute the Multi-Agent Pipeline

Once your automated orchestration layer is complete, flush any historical tracking indicators out of your directory workspace and execute your pipeline end-to-end within your command terminal:

```bash
# Clear downstream tracking artifacts
rm -f eval_results.json debugging_report.md bank_processor_healed.py

# Step 1: Run your Self-Healing Test Orchestration Agent
python agent_debugger.py

# Step 2: Invoke the pre-provided Pipeline Governance Gate
python eval_debugger.py

```

---

### Step 5: Verification & System Audit

To confirm that your autonomous loop is operating optimally, audit your workspace outputs:

* **`bank_processor.py`:** Check the file to ensure it remains completely untouched and retains its original masked test layout.
* **`bank_processor_healed.py`:** Confirm that this file exists and contains the unmasked test sequence, breaking the single oversized transaction into incremental chunks that safely evaluate the daily limit constraints.
* **`eval_results.json`:** Verify that the file displays an `"APPROVED"` status parameter coupled with a perfect engineering score of `100`.