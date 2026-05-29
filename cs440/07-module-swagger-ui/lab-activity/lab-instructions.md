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