# Integer Trap
```
def calculate_total(price, quantity):
    """
    Calculates the total price of an order.
    TODO: Add input validation to prevent negative quantities.
    """
    
    # --- WRITE YOUR SECURITY CHECK BELOW THIS LINE ---
    if quantity < 0:
        return 0
    
    # -------------------------------------------------
    
    total_cost = price * quantity
    return total_cost
```

# Missing Gate
```
def run_pipeline():
    """
    Simulates the Automated Build Pipeline.
    TODO: Insert a Security Gate that STOPS deployment on failure.
    """
    
    print("--- STARTING PIPELINE ---")
    
    stage_checkout()
    stage_build()
    
    # --- ADD SECURITY GATE BELOW ---
    # Tip: if not stage_security_scan(): ...
    if not stage_security_scan():
        print("CRITICAL ERROR: Security scan failed. Aborting deployment.")
        return  # This stops the function and prevents stage_deploy()
    # -------------------------------
    
    # -------------------------------
    
    stage_deploy()
    print("--- PIPELINE FINISHED ---")
```

# Brute Force Balance
```
def check_login(input_password, real_password, user_data):
    """
    Validates login and handles lockout logic.
    """
    
    # 1. SECURITY CHECK: Is the account already locked?
    if user_data['failed_attempts'] >= 3:
        return "LOCKED"
    
    # 2. PASSWORD CHECK
    if input_password == real_password:
        # USABILITY: Reset the counter on success so old mistakes 
        # don't haunt the user later.
        user_data['failed_attempts'] = 0 
        return "SUCCESS"
    else:
        # SECURITY: Increment the failure count on wrong attempts.
        user_data['failed_attempts'] += 1
        return "FAIL"
```

# Architect Gate
```
# GLOBAL PERMISSION CONFIGURATION
ROLE_PERMISSIONS = {
    "SUPER_ADMIN":  ["create_users", "delete_users", "view_data"],
    "ADMIN_VIEWER": ["view_data"],  # READ ONLY!
    "MANAGER":      ["create_users", "view_data"],
    "USER":         ["view_data"]
}

def delete_user_action(user_role):
    """
    Determines if a user is allowed to delete an account.
    """
    
    # --- FIXED SECURE CODE ---
    # 1. Get the list of permissions for this user_role from ROLE_PERMISSIONS
    permissions = ROLE_PERMISSIONS.get(user_role, [])
    
    # 2. Check if "delete_users" exists in that list
    if "delete_users" in permissions:
        return "AUTHORIZED"
    
    return "DENIED"
```

# Salted Vault
```
import hashlib
import secrets

def save_user(username, password):
    # 1. Generate a random salt (16 hex chars)
    my_salt = secrets.token_hex(16)
    
    # 2. Combine Salt + Password and Hash it using SHA-256
    combined = (my_salt + password).encode()
    my_hash = hashlib.sha256(combined).hexdigest()
    
    # 3. Return the storage dictionary
    return {'salt': my_salt, 'hash': my_hash}
```
# Malicious Link
```
import html

def sanitize_link(user_url):
    # 1. SECURITY CHECK: Validate Protocol
    # Ensure it starts with approved web protocols
    if not (user_url.startswith("http://") or user_url.startswith("https://")):
        return "#"
    
    # 2. SANITIZATION: Escape characters
    # This prevents "quote breaking" attacks in the HTML attribute
    return html.escape(user_url)
```    

# Shattered Database
```
import sqlite3

def login_user(cursor, username, password):
    # Use placeholders (?) and pass parameters as a tuple
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    
    return cursor.fetchone()
```

# Invisible Request
```
def process_transfer(session, amount, user_token):
    """
    Processes a money transfer.
    session: Dictionary containing 'username' and 'csrf_token'
    amount: Dollar amount to transfer
    user_token: The token sent in the HTML form request
    """
    
    # 1. Authentication Check (Already Implemented)
    if 'username' not in session:
        return "Error: Please log in."
        
    # 2. VULNERABILITY: Missing Token Check!
    # Currently, we just accept the request if they are logged in.
    # TODO: Check if user_token matches session['csrf_token']
    #       If not match, return "CSRF Blocked"
    
    # 2. SECURITY CHECK: Validate CSRF Token
    # Compare the user_token from the form against the session's csrf_token
    if user_token != session['csrf_token']:
        # 3. Block if Mismatch: The simulation specifically looks for "Access Denied"
        return "Access Denied"
    return f"Success! Transferred ${amount}."
```
# Data Integrity
```
import hmac
import hashlib

def sign_message(secret_key, message):
    # 1. Convert inputs to bytes
    key_bytes = secret_key.encode()
    msg_bytes = message.encode()
    
    # 2. Create HMAC object using SHA-256
    my_hmac = hmac.new(key_bytes, msg_bytes, hashlib.sha256)
    
    # 3. Return the hex digest
    return my_hmac.hexdigest()

```
# Secure Header
```
def get_security_headers():
    headers = {
        "Content-Type": "text/html",
        "X-Powered-By": "Python"
    }
    
    # 1. Add 'Content-Security-Policy' key
    # 2. Set value to "default-src 'self'" to only allow your own domain
    headers["Content-Security-Policy"] = "default-src 'self'"
    
    return headers #
```