# SQA Chaos Engineering & Input Guardrail Report

## Target Service Verified
`production_service.py`

## Captured Guardrail Violations
```text
--- Guardrail Exception Trapped on Pass #1 ---
Traceback (most recent call last):
  File "/workspaces/cs-courses/cs440/02-module-non-functional-requirements/production_service.py", line 14, in <module>
    print(execute_expression("os.system('rm -rf /')"))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspaces/cs-courses/cs440/02-module-non-functional-requirements/production_service.py", line 12, in execute_expression
    return eval(expr)
           ^^^^^^^^^^
  File "<string>", line 1, in <module>
NameError: name 'os' is not defined. Did you forget to import 'os'?

--- Guardrail Exception Trapped on Pass #2 ---
Traceback (most recent call last):
  File "/workspaces/cs-courses/cs440/02-module-non-functional-requirements/production_service.py", line 38, in <module>
    print(get_user_language({'name': 'Alice'}))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspaces/cs-courses/cs440/02-module-non-functional-requirements/production_service.py", line 36, in get_user_language
    return user['language']
           ~~~~^^^^^^^^^^^^
KeyError: 'language'
```

## Applied Structural Resilience Patches
- Secured execute_expression endpoint against arbitrary string injections using AST.
- Resolved KeyError vulnerability by applying dictionary fallback defaults.
