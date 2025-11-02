def addDigits_onetime(num: int) -> int:
    """
    Repeatedly adds all its digits until the result has only one digit 
    (without loop/recursion, using the digital root property).
    """
    if num == 0:
        return 0
    # The digital root is 9 if the number is a multiple of 9 (and not 0), 
    # otherwise it is num % 9.
    if num % 9 == 0:
        return 9
    else:
        return num % 9
    
    # Alternatively, the formula 1 + (num - 1) % 9 handles both cases 
    # for num > 0 concisely:
    # return 1 + (num - 1) % 9

# Example Usage:
# print(f"Add Digits (Formula) for 38: {addDigits_onetime(38)}")  # Output: 2
# print(f"Add Digits (Formula) for 0: {addDigits_onetime(0)}")    # Output: 0
# print(f"Add Digits (Formula) for 9: {addDigits_onetime(9)}")    # Output: 9
# print(f"Add Digits (Formula) for 18: {addDigits_onetime(18)}")  # Output: 9
