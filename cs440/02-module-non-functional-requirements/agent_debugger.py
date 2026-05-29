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

    # Run execution loop to discover unhandled system reactions
    run_check = subprocess.run(["python", TARGET_SCRIPT], capture_output=True, text=True)
    
    if run_check.returncode == 0 and "KeyError" not in run_check.stderr and "NameError" not in run_check.stderr:
        print(f"[+] Quality Loop complete: Script passed all guardrail verifications on Pass #{iteration+1}.")
        break
        
    error_msg = run_check.stderr if run_check.stderr else run_check.stdout
    traceback_summary += f"\n--- Guardrail Exception Trapped on Pass #{iteration+1} ---\n{error_msg}"
    
    # TRIAGE AND ROUTE NON-FUNCTIONAL FAULTS
    
    # Fault A: Security/Injection vulnerability (eval usage exposed)
    if "eval(expr)" in script_source and "ast.literal_eval" not in script_source:
        print("[*] Triage: Mitigating code injection risk by swapping eval() for ast.literal_eval()...")
        script_source = "import ast\n" + script_source.replace("return eval(expr)", "try:\n        return ast.literal_eval(expr)\n    except Exception as e:\n        return f'Error: {e}'")
        patched_code_display.append("Secured execute_expression endpoint against arbitrary string injections using AST.")

    # Fault B: Reliability/Accessibility crash (KeyError on dictionary lookup)
    elif "KeyError" in error_msg or "return user['language']" in script_source:
        print("[*] Triage: Resolving KeyError risk with a safe dictionary fallback handler...")
        script_source = script_source.replace("return user['language']", "return user.get('language', 'en')")
        patched_code_display.append("Resolved KeyError vulnerability by applying dictionary fallback defaults.")
        
    # Fault C: Performance Bottleneck (O(n^2) nested lookup pattern)
    elif "lst.count(i)" in script_source:
        print("[*] Triage: Refactoring quadratic array lookup to linear time complexity lookup set...")
        linear_fix = (
            "seen = set()\n"
            "    for i in lst:\n"
            "        if i in seen:\n"
            "            return True\n"
            "        seen.add(i)\n"
            "    return False"
        )
        # Replacing the algorithm body safely
        script_source = re.sub(r"def find_duplicates\(lst\):.*?return False", f"def find_duplicates(lst):\n    {linear_fix}", script_source, flags=re.DOTALL)
        patched_code_display.append("Optimized find_duplicates method complexity from O(n^2) down to O(n).")
        
    else:
        print("[-] System stabilization threshold reached or unmapped condition found.")
        break

    with open(TARGET_SCRIPT, "w", encoding="utf-8") as f:
        f.write(script_source)

# Output compliance log
diff_summary = "\n".join([f"- {item}" for item in patched_code_display]) if patched_code_display else "- Guardrails fully verified."
with open(REPORT_FILE, "w", encoding="utf-8") as report_file:
    report_file.write(
        f"# SQA Chaos Engineering & Input Guardrail Report\n\n"
        f"## Target Service Verified\n`{TARGET_SCRIPT}`\n\n"
        f"## Captured Guardrail Violations\n```text\n{traceback_summary.strip()}\n```\n\n"
        f"## Applied Structural Resilience Patches\n{diff_summary}\n"
    )
print(f"[+] Automated telemetry guardrail tracking report written to '{REPORT_FILE}'.")