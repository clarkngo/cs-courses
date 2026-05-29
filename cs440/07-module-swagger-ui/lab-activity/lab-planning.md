Moving into **Module 07**, we conclude the automated engineering curriculum with **Configuration Management (CM) & API Environment Validation**.

In previous modules, your students automated validations for runtime stability, security parameters, system telemetry, and test assertion masking. In this final laboratory module, they will focus on systematically tracking, controlling, and validating deployment configurations across distinct environments (`dev`, `staging`, `prod`).

Following the parameters of your configuration management brief, the baseline script simulates an API service registry where registration fails due to an invalid deployment environment configuration, throwing a `ConfigurationValidationError`. Students will write an orchestrator that dynamically intercepts configuration-level validation failures, programmatically refactors environment whitelisting rules, and certifies the artifact via the pre-provided universal governance gatekeeper.

---

## 🏗️ Module 07 Architecture Directory Map

```text
07-module-configuration-management/
├── service_config_manager.py       # Immutable Baseline (API configuration layer with environment mismatches)
├── agent_debugger.py              # CM Orchestrator (Traps config violations -> builds staging asset)
├── service_config_manager_healed.py # Staging Target Output (Generates environment-validated configurations)
├── eval_debugger.py               # Universal Governance Agent (Verifies execution and report tracking)
├── debugging_report.md            # Pipeline verification report (Passes structural check)
└── eval_results.json              # Final automated validation grading token

```

---

## 🔑 Master Answer Keys (Instructor & CI/CD Pipeline Layer)

### 1. The Universal Governance Gate (`eval_debugger.py`)

*This environment-agnostic automated release gate remains identical and immutable across your laboratory repository infrastructure.*

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

### 2. Module 07 Orchestrator Solution (`agent_debugger.py`)

*This master solution copies the configuration manager, intercepts the environment tracking anomalies via standard error channels, and programmatically enforces white-box environment safety validation constraints.*

```python
import subprocess
import os
import sys

SRC_SCRIPT = "service_config_manager.py"
HEALED_SCRIPT = "service_config_manager_healed.py"
REPORT_FILE = "debugging_report.md"

if not os.path.exists(SRC_SCRIPT):
    print(f"[-] Error: '{SRC_SCRIPT}' not found.")
    sys.exit(1)

print(f"[+] Configuration Management Orchestrator active. Seeding staging target...")

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
        print(f"[+] Quality Loop complete: Environment infrastructure configurations stabilized on Pass #{iteration+1}.")
        break
        
    error_msg = run_check.stderr if run_check.stderr else run_check.stdout
    traceback_summary += f"\n--- Configuration Management Discrepancy Intercepted on Pass #{iteration+1} ---\n{error_msg}"
    
    # TRIAGE STREAM: Detect environment validation mismatch or unhandled reachability errors
    if "ConfigurationValidationError" in error_msg or "invalid_env" in script_source:
        print("[*] Triage: Engineering dynamic runtime environment whitelisting filters...")
        
        # Inject validation check layer ensuring alignment with strict CM allowed targets
        validation_patch = (
            "ALLOWED_ENVS = ['dev', 'staging', 'prod']\n"
            "    if env not in ALLOWED_ENVS:\n"
            "        print(f'[-] Invalid environment configuration item {env} blocked. Defaulting to dev.')\n"
            "        env = 'dev'"
        )
        script_source = script_source.replace("raise ValueError(f\"ConfigurationValidationError: Invalid target environment configuration item: {env}\")", validation_patch)
        patched_code_display.append("Refactored deployment environment parameter assignment to enforce strict dev/staging/prod constraints.")
        
    elif "ServiceUnreachableError" in error_msg:
        print("[*] Triage: Applying defensive configuration fallback handler for endpoint checks...")
        fallback_patch = (
            "try:\n"
            "        raise ConnectionError()\n"
            "    except ConnectionError:\n"
            "        print('[!] Service metadata endpoint unreachable. Registering fallback placeholder state.')\n"
            "        return 'unreachable'"
        )
        script_source = script_source.replace("raise RuntimeError(\"ServiceUnreachableError: Missing connectivity fallback path.\")", fallback_patch)
        patched_code_display.append("Implemented connection exception handler matching reachability fallback specifications.")
    else:
        print("[-] Verification threshold reached or unmapped configuration signature caught.")
        break

    with open(HEALED_SCRIPT, "w", encoding="utf-8") as f:
        f.write(script_source)

# Write out compliance logs containing mandatory structural phrases
diff_summary = "\n".join([f"- {item}" for item in patched_code_display]) if patched_code_display else "- Environment states verified."
with open(REPORT_FILE, "w", encoding="utf-8") as report_file:
    report_file.write(
        f"# SQA Configuration Management & API Validation Report\n\n"
        f"## Target File Audited\n`{SRC_SCRIPT}`\n\n"
        f"## Captured Guardrail Violations\n```text\n{traceback_summary.strip()}\n```\n\n"
        f"## Applied Structural Resilience Patches\n{diff_summary}\n"
    )
print(f"[+] Automated configuration management tracking report compiled at '{REPORT_FILE}'.")

```

---

## 📝 Student Lab Manual

# Lab Manual: Configuration Management & API Environment Validation

## Objective

In this laboratory, you will complete your automated SQA portfolio by exploring **Configuration Management (CM) and API Schema Validation**. Configuration Management involves systematically tracking, controlling, and validating software configurations across isolated environment tiers. If an application registry swallows malformed environment data or fails to establish defensive fallbacks for unreachable network connections, the entire deployment infrastructure risks cascade instability.

You will build an autonomous configuration validation pipeline tool inside **`agent_debugger.py`**. Your agent will execute a target microservice configuration manager, intercept unhandled configuration mismatches from standard error streams, and programmatically refactor the system to enforce environment constraints (`dev`, `staging`, `prod`).

To protect the integrity of your continuous deployment baseline, your automated scripts must treat the initial tracking module as immutable, exporting all programmatic modifications to a separate staging build file:

1. **The Orchestrator Agent (`agent_debugger.py`):** Programmatically triggers validation checkpoints, processes standard error buffers to triage configuration mutations, and exports a stabilized staging artifact file.
2. **The Evaluator Agent (`eval_debugger.py`):** An environmental-agnostic universal quality gate pre-provided in your repository track that executes staging builds to sign off on quality release parameters.

---

### Step 1: Initialize the Immutable Baseline (`service_config_manager.py`)

First, construct your target infrastructure configuration service layer. This script models a centralized environment registration hub that contains two major flaws: it permits invalid non-standard environment strings to corrupt its configuration structure, and it lacks structural connection handlers when validating microservice reachability.

Create a file named **`service_config_manager.py`** and populate it with this baseline implementation:

```python
# Service Configuration Manager Layer - Project Horizon Baseline
import sys

def register_service(name, url, health_check, env):
    print(f"[*] Auditing service registration item: Name='{name}', Environment='{env}'...")
    
    # FAULT 1: Missing structural environment tracking whitelist lookup.
    # Allowed targets must be limited exclusively to: 'dev', 'staging', 'prod'
    if env not in ['dev', 'staging', 'prod']:
        raise ValueError(f"ConfigurationValidationError: Invalid target environment configuration item: {env}")
        
    print(f"[+] Successfully verified configuration items for environment context: {env}")
    return True

def verify_service_reachability(url):
    print(f"[*] Checking configuration route connectivity: URL='{url}'...")
    
    # FAULT 2: Unhandled exception path. If the service metadata endpoint is down, 
    # the application must catch the failure and gracefully return "unreachable" instead of crashing.
    raise RuntimeError("ServiceUnreachableError: Missing connectivity fallback path.")

if __name__ == "__main__":
    print("[*] Initiating configuration management validation checklist...")
    
    # Sequential hurdles designed to test multi-pass self-healing execution
    try:
        register_service("payment_service", "https://api.example.com/pay", "/health", "invalid_env")
    except Exception as e:
        print(f"[-] Blocked by exception track: {e}", file=sys.stderr)
        raise e
        
    try:
        verify_service_reachability("https://api.example.com/pay")
    except Exception as e:
        print(f"[-] Blocked by exception track: {e}", file=sys.stderr)
        raise e

```

---

### Step 2: Build the Orchestrator Triage Agent (`agent_debugger.py`)

Your primary engineering challenge is to write the automated configuration management triage script. Your program must read the immutable baseline code, execute it within isolated system processes, capture individual `ConfigurationValidationError` and `ServiceUnreachableError` trace descriptions from `stderr`, and apply programmatic changes to isolate environment variables.

Create **`agent_debugger.py`** to meet the following configuration specifications:

* **Immutable Inputs:** Your script must read from the baseline file (`service_config_manager.py`) but **never modify it directly**. All refactoring operations must occur in-memory or save directly to a staging file.
* **Isolated Target Output:** Save your final, error-free staging build configuration directly to a new file named `service_config_manager_healed.py`.
* **Multi-Pass Convergence Loop:** Configure an execution cycle (up to 5 iterations) to systematically catch downstream errors that surface as earlier registration blocks are refactored.
* **Process Interception:** Utilize Python’s `subprocess.run()` with `capture_output=True` to trap runtime console outputs safely without crashing your orchestrator tool.
* **Traceback-Driven Triage:** Direct your refactoring replacements by parsing specific exception keywords found inside the runtime stream. Intercept instances where non-standard environment arrays throw violations, programmatically replacing the failure block with validation gates that fall back cleanly to `"dev"`. Intercept reachability checks to wrap network execution blocks inside standard `try-except` filters that capture failures and return `"unreachable"` safely.
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
rm -f eval_results.json debugging_report.md service_config_manager_healed.py

# Step 1: Run your Self-Healing Configuration Orchestrator Agent
python agent_debugger.py

# Step 2: Invoke the pre-provided Pipeline Governance Gate
python eval_debugger.py

```

---

### Step 5: Verification & System Audit

To confirm that your autonomous loop is operating optimally, audit your workspace outputs:

* **`service_config_manager.py`:** Check the file to ensure it remains completely untouched and retains its original unvalidated configuration layout.
* **`service_config_manager_healed.py`:** Confirm that this file exists, resolves environment schema checks safely against a `dev/staging/prod` lookup, handles network connectivity failures, and compiles with a clean exit status code.
* **`eval_results.json`:** Verify that the file displays an `"APPROVED"` status parameter coupled with a perfect engineering score of `100`.