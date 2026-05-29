# KPI Dashboard & Risk Matrix Service Layer - Project Horizon Baseline
import sys

def calculate_kpi_efficiency(metrics):
    print("[*] Evaluating KPI dashboard metrics...")
    
    # FAULT 1: Missing array validation guard. An empty list dataset will trigger a crash.
    if not metrics or len(metrics) == 0:
        print('[-] Metric dataset empty. Defaulting to safe baseline score evaluation.')
        return 0.0
        
    return sum(metrics) / len(metrics)

def assess_risk_matrix(impact, likelihood):
    print(f"[*] Mapping risk matrix bounds: Impact={impact}, Likelihood={likelihood}...")
    
    # FAULT 2: Missing containment guards. Values must map strictly within a 1 to 5 scale.
    if impact < 1 or impact > 5 or likelihood < 1 or likelihood > 5:
        print('[!] Out of bounds matrix inputs detected. Applying boundary clamping mitigation.')
        impact = max(1, min(5, impact))
        likelihood = max(1, min(5, likelihood))
        
    return impact * likelihood

if __name__ == "__main__":
    print("[*] Loading metric assessment and risk profiling tracks...")
    
    # Sequential calculation verification hurdles designed to trigger tracebacks across passes
    try:
        calculate_kpi_efficiency([])
    except Exception as e:
        print(f"[-] Blocked by dashboard outlier: {e}", file=sys.stderr)
        raise e
        
    try:
        assess_risk_matrix(6, 4)
    except Exception as e:
        print(f"[-] Blocked by risk assessment boundaries: {e}", file=sys.stderr)
        raise e