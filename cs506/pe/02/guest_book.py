def guest_book():
    """
    Continuously prompt users for their name.
    Print a greeting and record each visit in guest_book.txt.

    Explanation:
    ------------
    - Use a while loop for continuous input.
    - Stop loop when user enters 'quit'.
    - Write each name to guest_book.txt on a new line.

    Example:
    --------
    Input: Alice → Output: Welcome, Alice!
    File Content: Alice
    """

    while True:
        name = input("Enter your name (or 'quit' to exit): ")
        if name.lower() == 'quit':
            print("Goodbye!")
            break
        print(f"Welcome, {name}!")
        with open("guest_book.txt", "a") as file:
            file.write(f"{name}\n")


# ✅ To test interactively, uncomment below
# guest_book()
