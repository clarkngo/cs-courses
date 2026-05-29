# Service Configuration Manager Layer - Project Horizon Baseline
import sys

def register_service(name, url, health_check, env):
    print(f"[*] Auditing service registration item: Name='{name}', Environment='{env}'...")
    
    # FAULT 1: Missing structural environment tracking whitelist lookup.
    # Allowed targets must be limited exclusively to: 'dev', 'staging', 'prod'
    if env not in ['dev', 'staging', 'prod']:
        ALLOWED_ENVS = ['dev', 'staging', 'prod']
    if env not in ALLOWED_ENVS:
        print(f'[-] Invalid environment configuration item {env} blocked. Defaulting to dev.')
        env = 'dev'
        
    print(f"[+] Successfully verified configuration items for environment context: {env}")
    return True

def verify_service_reachability(url):
    print(f"[*] Checking configuration route connectivity: URL='{url}'...")
    
    # FAULT 2: Unhandled exception path. If the service metadata endpoint is down, 
    # the application must catch the failure and gracefully return "unreachable" instead of crashing.
    try:
        raise ConnectionError()
    except ConnectionError:
        print('[!] Service metadata endpoint unreachable. Registering fallback placeholder state.')
        return 'unreachable'

if __name__ == "__main__":
    print("[*] Initiating configuration management validation checklist...")
    
    # Sequential hurdles designed to test multi-pass self-healing execution
    try:
        register_service("payment_service", "https://api.example.com/pay", "/health", "invalid_env")
    except Exception as e:
        print(f"[-] Blocked by exception track: {e}", file=sys.stderr)
        raise e
        
    try:
        verify_service_reachability("https://api.example.com/pay")
    except Exception as e:
        print(f"[-] Blocked by exception track: {e}", file=sys.stderr)
        raise e