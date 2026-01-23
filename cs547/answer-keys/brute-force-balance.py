def check_login(input_password, real_password, user_data):
    """
    Validates login and handles lockout logic.
    Args:
      input_password (str): What the user typed.
      real_password (str): The correct password.
      user_data (dict): A dictionary containing:
                        {'failed_attempts': 0}
    
    Returns: "SUCCESS", "FAIL", or "LOCKED"
    """
    # 1. SECURITY CHECK: Is the account already locked?
    # TODO: Check if user_data['failed_attempts'] >= 3
    if user_data['failed_attempts'] >= 3:
        return "LOCKED"
    
    
    # 2. PASSWORD CHECK
    if input_password == real_password:
        # TODO: USABILITY - Reset the counter on success!
        user_data['failed_attempts'] = 0
        return "SUCCESS"
    else:
        # TODO: SECURITY - Increment the counter on failure
        user_data['failed_attempts'] += 1
        return "FAIL"

        


