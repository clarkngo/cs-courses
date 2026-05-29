# SQA Standalone Script Fault Isolation Report

## Target File Audited
`system_utilities.py`

## Captured Multi-Fault Execution Tracebacks
```text
--- Error Trapped on Pass #1 ---
  File "/workspaces/cs-courses/cs440/01-module-python-for-software-quality/system_utilities.py", line 4
    print(items[i
               ^
SyntaxError: '[' was never closed

--- Error Trapped on Pass #2 ---
  File "/workspaces/cs-courses/cs440/01-module-python-for-software-quality/system_utilities.py", line 16
    if name = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

## Programmatic Self-Healing Diffs Applied
- Fixed print statement bracket cutoff error.
- Swapped variable assignment token '=' with equality operator '=='.
