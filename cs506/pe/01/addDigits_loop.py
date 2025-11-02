def addDigits_loop(num: int) -> int:
    """
    Repeatedly adds all its digits until the result has only one digit (using a loop).
    """
    while num >= 10:
        digit_sum = 0
        # Sum the digits of the current number
        while num > 0:
            digit_sum += num % 10
            num //= 10
        num = digit_sum
    return num

# Example Usage:
# print(f"Add Digits (Loop) for 38: {addDigits_loop(38)}")  # Output: 2
