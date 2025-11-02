def strStr(haystack: str, needle: str) -> int:
    """
    Return the index of the first occurrence of 'needle' in 'haystack'.
    If 'needle' is not found, return -1.
    
    Parameters:
    -----------
    haystack : str
        The main string in which to search.
    needle : str
        The substring to find.
        
    Returns:
    --------
    int
        The starting index of the first occurrence of 'needle' in 'haystack',
        or -1 if not found. Returns 0 if 'needle' is an empty string.
    
    Example:
    --------
    >>> strStr("hello", "ll")
    2
    >>> strStr("aaaaa", "bba")
    -1
    >>> strStr("abc", "")
    0
    """

    # 🧩 Step 1: Handle edge case where needle is empty
    if needle == "":
        return 0

    # 🧩 Step 2: Get lengths to control iteration bounds
    n, m = len(haystack), len(needle)

    # 🧩 Step 3: Iterate through haystack until there's no room for needle
    for i in range(n - m + 1):
        # Extract substring of same length as needle
        window = haystack[i:i + m]

        # 🧩 Step 4: Compare window with needle
        if window == needle:
            return i  # Found match at index i

    # 🧩 Step 5: If loop completes without finding a match
    return -1


# ✅ Test cases
print(strStr("hello", "ll"))    # Expected output: 2
print(strStr("aaaaa", "bba"))   # Expected output: -1
print(strStr("abc", ""))        # Expected output: 0
