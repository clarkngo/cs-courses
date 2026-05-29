import html
# Task Manager Service Layer - Project Horizon Baseline
import json
import os

def add_task(title, status=1):
    # Fault 1 & 5: Gaps in Input Control and Sanitization
    if title == "" or title.isspace():
        print("[-] Rejected empty input payload.")
        return False
        
    title = html.escape(title)
    print("[+] Input text sanitized via html entities.")
        
    # Fault 3: Uninformative and vague status logging metrics
    if status == 1:
        status = "Pending"
        
    print(f"[+] Task stored successfully: Title='{title}', Status='{status}'")
    return True

def delete_task(task_id):
    # Fault 2: Functional Lifecycle Gap
    print(f"[+] Purging task entity {task_id} from tracking index.")
    return True

if __name__ == "__main__":
    print("[*] Invoking internal software process audit simulation...")
    
    # Sequential verification hurdles designed to trigger tracebacks across passes
    add_task("")
    add_task("<script>alert('XSS')</script>")
    add_task("Complete SQA Module 05 Review", status=1)
    delete_task(101)