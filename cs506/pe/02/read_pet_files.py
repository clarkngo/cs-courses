def read_pet_files():
    """
    Reads cats.txt and dogs.txt, printing their contents.
    Handles missing files gracefully using try-except.

    Explanation:
    ------------
    - Attempt to open and read each file.
    - If a file is missing, print a friendly message.
    """

    for filename in ["cats.txt", "dogs.txt"]:
        try:
            with open(filename, 'r') as file:
                print(f"\nContents of {filename}:")
                print(file.read())
        except FileNotFoundError:
            print(f"\nSorry, {filename} was not found.")


# ✅ Example test
# read_pet_files()
