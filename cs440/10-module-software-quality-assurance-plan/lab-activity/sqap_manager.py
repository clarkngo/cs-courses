# Software Quality Assurance Plan Manager Layer - Project Horizon Baseline
import sys
import json

def validate_sqap_fields(plan_data):
    print("[*] Auditing Software Quality Assurance Plan (SQAP) fields...")
    
    # FAULT 1: Missing section content values. All mandatory fields must contain records.
    if not plan_data.get("purpose") or not plan_data.get("management"):
        raise ValueError("SQAPValidationError: Mandatory SQAP sections ('purpose', 'management') are empty or unassigned.")
        
    return True

def verify_sqap_references(plan_data):
    print("[*] Verifying SQAP reference citations...")
    
    # FAULT 2: Missing reference logs. References must be documented and verified.
    if not plan_data.get("references") or len(plan_data["references"]) == 0:
        raise KeyError("MissingReferencesError: SQAP reference citations are completely empty or unverified.")
        
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