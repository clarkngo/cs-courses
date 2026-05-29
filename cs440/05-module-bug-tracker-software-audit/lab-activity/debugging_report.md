# SQA Process Compliance & Code Quality Audit Report

## Target File Audited
`task_manager_service.py`

## Captured Guardrail Violations
```text
--- Process QA Deviation Caught on Pass #1 ---
Traceback (most recent call last):
  File "/workspaces/cs-courses/cs440/05-module-bug-tracker-software-audit/task_manager_service_healed.py", line 28, in <module>
    add_task("")
  File "/workspaces/cs-courses/cs440/05-module-bug-tracker-software-audit/task_manager_service_healed.py", line 8, in add_task
    raise ValueError("AuditViolation: Empty task title allowed without validation input controls.")
ValueError: AuditViolation: Empty task title allowed without validation input controls.

--- Process QA Deviation Caught on Pass #2 ---
Traceback (most recent call last):
  File "/workspaces/cs-courses/cs440/05-module-bug-tracker-software-audit/task_manager_service_healed.py", line 30, in <module>
    add_task("<script>alert('XSS')</script>")
  File "/workspaces/cs-courses/cs440/05-module-bug-tracker-software-audit/task_manager_service_healed.py", line 12, in add_task
    raise ValueError("AuditViolation: No input sanitization detected. Vulnerable to XSS injection.")
ValueError: AuditViolation: No input sanitization detected. Vulnerable to XSS injection.

--- Process QA Deviation Caught on Pass #3 ---
Traceback (most recent call last):
  File "/workspaces/cs-courses/cs440/05-module-bug-tracker-software-audit/task_manager_service_healed.py", line 31, in <module>
    add_task("<script>alert('XSS')</script>")
  File "/workspaces/cs-courses/cs440/05-module-bug-tracker-software-audit/task_manager_service_healed.py", line 17, in add_task
    raise TypeError("AuditViolation: Status field set to numeric integer '1' instead of clear text labels.")
TypeError: AuditViolation: Status field set to numeric integer '1' instead of clear text labels.

--- Process QA Deviation Caught on Pass #4 ---
Traceback (most recent call last):
  File "/workspaces/cs-courses/cs440/05-module-bug-tracker-software-audit/task_manager_service_healed.py", line 33, in <module>
    delete_task(101)
  File "/workspaces/cs-courses/cs440/05-module-bug-tracker-software-audit/task_manager_service_healed.py", line 24, in delete_task
    raise NotImplementedError("AuditViolation: No delete function route implemented.")
NotImplementedError: AuditViolation: No delete function route implemented.
```

## Applied Structural Resilience Patches
- Implemented input string validation loops to block meaningless blank submissions (CMMI-DEV Process QA).
- Injected character entity escaping layers to mitigate XSS code injection hazards (ISO/IEC 12207).
- Refactored vague database integer markers to explicit status string attributes ('Pending').
- Completed task asset deletion lifecycles to fulfill missing functional specification layers (IEEE 1028).
