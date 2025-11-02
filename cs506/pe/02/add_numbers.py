def add_numbers():
    """
    Prompts the user for two numbers, adds them, and prints the result.
    Handles ValueError if a non-numeric input is provided.

    Explanation:
    ------------
    - Use input() to get user values.
    - Try converting to int and add them.
    - Catch ValueError and display friendly message.

    Example:
    --------
    Input: 10, 20
    Output: The sum is 30
    Input: ten, 20
    Output: Please enter valid numbers only.
    """

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        total = num1 + num2
        print(f"The sum is {total}")
    except ValueError:
        print("Please enter valid numbers only.")


# ✅ To test interactively, uncomment the line below
# add_numbers()
