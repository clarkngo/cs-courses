# SQA Configuration Management & API Validation Report

## Target File Audited
`service_config_manager.py`

## Captured Guardrail Violations
```text
--- Configuration Management Discrepancy Intercepted on Pass #1 ---
[-] Blocked by exception track: ConfigurationValidationError: Invalid target environment configuration item: invalid_env
Traceback (most recent call last):
  File "/workspaces/cs-courses/cs440/07-module-swagger-ui/lab-activity/service_config_manager_healed.py", line 30, in <module>
    raise e
  File "/workspaces/cs-courses/cs440/07-module-swagger-ui/lab-activity/service_config_manager_healed.py", line 27, in <module>
    register_service("payment_service", "https://api.example.com/pay", "/health", "invalid_env")
  File "/workspaces/cs-courses/cs440/07-module-swagger-ui/lab-activity/service_config_manager_healed.py", line 10, in register_service
    raise ValueError(f"ConfigurationValidationError: Invalid target environment configuration item: {env}")
ValueError: ConfigurationValidationError: Invalid target environment configuration item: invalid_env

--- Configuration Management Discrepancy Intercepted on Pass #2 ---
[-] Blocked by exception track: ServiceUnreachableError: Missing connectivity fallback path.
Traceback (most recent call last):
  File "/workspaces/cs-courses/cs440/07-module-swagger-ui/lab-activity/service_config_manager_healed.py", line 39, in <module>
    raise e
  File "/workspaces/cs-courses/cs440/07-module-swagger-ui/lab-activity/service_config_manager_healed.py", line 36, in <module>
    verify_service_reachability("https://api.example.com/pay")
  File "/workspaces/cs-courses/cs440/07-module-swagger-ui/lab-activity/service_config_manager_healed.py", line 23, in verify_service_reachability
    raise RuntimeError("ServiceUnreachableError: Missing connectivity fallback path.")
RuntimeError: ServiceUnreachableError: Missing connectivity fallback path.
```

## Applied Structural Resilience Patches
- Refactored deployment environment parameter assignment to enforce strict dev/staging/prod constraints.
- Implemented connection exception handler matching reachability fallback specifications.
