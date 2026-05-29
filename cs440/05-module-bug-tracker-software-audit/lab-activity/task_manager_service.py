# Task Manager Service Layer - Project Horizon Baseline
import json
import os

def add_task(title, status=1):
    # Fault 1 & 5: Gaps in Input Control and Sanitization
    if title == "":
        raise ValueError("AuditViolation: Empty task title allowed without validation input controls.")
        
    if "<script>" in title:
        raise ValueError("AuditViolation: No input sanitization detected. Vulnerable to XSS injection.")
        
    # Fault 3: Uninformative and vague status logging metrics
    if status == 1:
        raise TypeError("AuditViolation: Status field set to numeric integer '1' instead of clear text labels.")
        
    print(f"[+] Task stored successfully: Title='{title}', Status='{status}'")
    return True

def delete_task(task_id):
    # Fault 2: Functional Lifecycle Gap
    raise NotImplementedError("AuditViolation: No delete function route implemented.")

if __name__ == "__main__":
    print("[*] Invoking internal software process audit simulation...")
    
    # Sequential verification hurdles designed to trigger tracebacks across passes
    add_task("")
    add_task("<script>alert('XSS')</script>")
    add_task("Complete SQA Module 05 Review", status=1)
    delete_task(101)