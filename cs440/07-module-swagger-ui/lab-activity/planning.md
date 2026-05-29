Moving into **Module 06** introduces the final structural phase of your automation architecture: **Automated Test Framework Integration & Test Case Masking Remediation**.

In previous exercises, your students handled system-level anomalies, runtime tracebacks, and process audits. In this final lab module, they will learn to distinguish between application code defects and **flawed/masked test cases**.

Using the real-world fintech limits documented in your testing brief (a **$10,000 per-transaction cap** and a **$25,000 cumulative daily limit**), students will build an engineering orchestration layer that programmatically diagnoses a broken test runner workflow and heals it by refactoring transaction sequences to expose hidden operational bottlenecks.

---

## 🏗️ Module 06 Architecture Directory Map

```text
06-module-test-frameworks/
├── bank_processor.py             # Immutable Baseline (Fintech module with a masked validation test)
├── agent_debugger.py             # Test Orchestrator (Traps masking failures -> builds staging build)
├── bank_processor_healed.py      # Staging Target Output (Generates decoupled error-free verification)
├── eval_debugger.py              # Universal Governance Agent (Verifies execution and report tracking)
├── debugging_report.md           # Pipeline verification report (Passes structural check)
└── eval_results.json             # Final automated validation grading token

```

---

## 🔑 Reference Answer Keys (Instructor Verification Layer)

### 1. The Immutable Baseline (`bank_processor.py`)

This file models a production financial layer containing robust defensive validations , alongside an inline verification suite that accidentally masks a daily transaction threshold check by attempting to send an oversized lump-sum amount first.

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

### 2. The Refactored Orchestrator (`agent_debugger.py`)

This script copies the baseline file into the staging target, captures the resulting `ValueError: Transfer exceeds per-transaction limit.` inside its process handler execution track , and seamlessly updates the transaction architecture into distinct, incremental validation chunks.

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
    
    # TRIAGE ROUTING STREAM: Detect the masked verification logic exception trace
    if "per-transaction limit" in error_msg or "account.transfer(15000)" in script_source:
        print("[*] Triage: Refactoring masked boundary condition transaction sequences...")
        
        # Unmask the execution flow by converting the lump sum into safe, multi-step allocations
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

# Export structural pipeline markdown log metadata parameters
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

## 📝 Complete Student Lab Manual

# Lab Manual: Automated Test Framework Integration & Test Case Masking

## Objective

In this lab, you will complete your automated CI/CD engine progression by mastering **Test Case Masking Remediation and Boundary Condition Analysis**. In professional enterprise settings, tests themselves can feature architectural bugs. A poorly structured verification script can trigger an unintended error block early on, completely masking a major design vulnerability downstream.

You will construct a two-agent architecture modeling an advanced test validation automation engine. Your framework will analyze transaction limit limits matching fintech regulations, intercept premature validation errors, and programmatically rewrite the execution sequence to verify true system thresholds.

To preserve the baseline layout of your core directory workspace, your scripts must treat the initial tracking module as an immutable asset, exporting all programmatic modifications to a separate, staging build file:

1. 
**The Orchestrator Agent (`agent_debugger.py`):** Programmatically triggers validation executions, reads stderr trace logs to flag masked exceptions, and exports a repaired staging file.


2. **The Evaluator Agent (`eval_debugger.py`):** Acts as an independent quality officer, verifying compilation integrity and compliance report tracking parameters.

---

### Step 1: Initialize the Immutable Baseline (`bank_processor.py`)

First, create your target application transaction service layer. This module features pristine production logic definitions but maps an active boundary verification suite that completely invalidates its own execution flow by violating per-transfer limits while trying to test daily aggregate capacities.

Create a file named **`bank_processor.py`** and populate it with this implementation:

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

Your second task is to design your autonomous test suite refactoring orchestrator. Your script must read the baseline code module, execute it within isolated background process pools, read the `ValueError` string traces thrown in `stderr` , and apply targeted replacements to cleanly isolate the secondary daily transfer ceiling validation.

Create **`agent_debugger.py`** to meet the following engineering specifications:

* **Immutable Inputs:** Your script must read from the baseline file (`bank_processor.py`) but **never alter it directly**. All refactoring transformations must happen in-memory or be saved to a staging file.
* **Isolated Target Output:** Save your final, hardened code updates to a brand-new staging file named `bank_processor_healed.py`.
* **Multi-Pass Convergence Loop:** Configure an execution cycle (up to 5 iterations) to continuously capture downstream errors that surface once earlier blockers are eliminated.
* **Process Interception:** Utilize Python’s `subprocess.run()` with `capture_output=True` to trap raw standard error channels cleanly.
* 
**Traceback-Driven Triage:** Route your modifications based on the specific exception text thrown in the runtime stream. Intercept instances where a premature per-transaction error masks daily limits, and programmatically split the transaction footprint into distinct, incremental allocations that remain safely under individual transfer limits while successfully testing daily capacity thresholds.


* **Pipeline Telemetry:** Upon convergence, save an automated execution summary named `debugging_report.md` detailing the trapped exceptions and specific patch rules fired.

> 💡 **Design Constraint:** Ensure all patch blocks are strictly **idempotent**. The script generation engine must explicitly verify that corrections do not duplicate or stack recursively across successive testing runs.

---

### Step 3: Deploy the Universal Governance Gate (`eval_debugger.py`)

To ensure total separation of concerns, drop your environmental-agnostic universal governance script into your workspace directory. This validator functions as your production release gatekeeper, scanning the execution space for compilation metrics without maintaining hardcoded filename rules.

Confirm your **`eval_debugger.py`** executes the following steps accurately:

1. **Dynamic Artifact Discovery:** Automatically scans directory folders using wildcard text patterns (e.g., `glob.glob("*_healed.py")`) to capture the staging target file.
2. **Compilation Guard:** Runs the discovered script file to confirm it successfully completes execution tracking loops with a standard exit code of `0` and throws zero lingering traceback crash exceptions.
3. **Telemetry Substring Verification:** Confirms that `debugging_report.md` exists and contains the strict compliance auditing markdown substring parameters **"Report"** and **"Audited"**.
4. **Structured Schema Export:** Formats final metrics straight into an industry-compliant JSON metadata token named `eval_results.json`.

---

### Step 4: Execute the Multi-Agent Pipeline

Once your automated testing architecture is complete, flush any historical tracking indicators out of your directory workspace and execute your pipeline end-to-end within your command terminal:

```bash
# Clear downstream tracking artifacts
rm -f eval_results.json debugging_report.md bank_processor_healed.py

# Step 1: Run the Self-Healing Test Orchestration Agent
python agent_debugger.py

# Step 2: Run the Standardized Independent Governance Gate
python eval_debugger.py

```

---

### Step 5: Verification & System Audit

To confirm that your autonomous loop is operating optimally, audit your workspace outputs:

* 
**`bank_processor.py`:** Check the file to ensure it remains completely untouched and retains its original masked code.


* 
**`bank_processor_healed.py`:** Confirm that this file exists and contains the unmasked sequence, breaking the single oversized transaction into multi-step requests that pass individual caps but trigger daily caps properly.


* **`eval_results.json`:** Verify that the file displays an `"APPROVED"` status parameter coupled with a perfect engineering score of `100`.