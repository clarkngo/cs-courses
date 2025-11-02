def count_words(filename: str) -> int:
    """
    Takes a text file as input and returns the number of words in it.

    Explanation:
    ------------
    - Open the file in read mode.
    - Split text into words using .split().
    - Count the number of words.

    Example:
    --------
    >>> count_words("sample.txt")
    42
    """
    try:
        with open(filename, 'r') as file:
            text = file.read()
        words = text.split()
        return len(words)
    except FileNotFoundError:
        print("File not found. Please check the filename.")
        return 0


# ✅ Example test (use your own text file)
# print(count_words("sample.txt"))
