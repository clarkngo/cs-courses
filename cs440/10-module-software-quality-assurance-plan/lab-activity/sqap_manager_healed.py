# Software Quality Assurance Plan Manager Layer - Project Horizon Baseline
import sys
import json

def validate_sqap_fields(plan_data):
    print("[*] Auditing Software Quality Assurance Plan (SQAP) fields...")
    
    # FAULT 1: Missing section content values. All mandatory fields must contain records.
    if not plan_data.get("purpose") or not plan_data.get("management"):
        print('[+] Initializing missing metadata with compliant defaults.')
        plan_data['purpose'] = 'Defines the software quality governance criteria for Project Horizon.'
        plan_data['management'] = 'Establishes oversight roles, organizational structures, and auditing tasks.'
        
    return True

def verify_sqap_references(plan_data):
    print("[*] Verifying SQAP reference citations...")
    
    # FAULT 2: Missing reference logs. References must be documented and verified.
    if not plan_data.get("references") or len(plan_data["references"]) == 0:
        print('[!] Reference gap detected. Appending verified compliance standards.')
        plan_data['references'] = ['IEEE Std 730-2014 Standard for Software Quality Assurance Processes']
        
    return True

if __name__ == "__main__":
    print("[*] Loading Software Quality Assurance Plan compliance framework...")
    
    # Initial incomplete configuration setup designed to trigger sequential passes
    mock_plan = {
        "purpose": "",
        "management": "",
        "references": []
    }
    
    try:
        validate_sqap_fields(mock_plan)
    except Exception as e:
        print(f"[-] Blocked by SQAP section checker: {e}", file=sys.stderr)
        raise e
        
    try:
        verify_sqap_references(mock_plan)
    except Exception as e:
        print(f"[-] Blocked by reference auditor: {e}", file=sys.stderr)
        raise e