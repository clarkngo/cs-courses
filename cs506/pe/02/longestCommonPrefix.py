def longestCommonPrefix(strs: list[str]) -> str:
    """
    Find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    Explanation:
    ------------
    - Compare characters vertically (column by column).
    - Stop when a mismatch is found or one string ends.
    - If no mismatch, the entire prefix is common.

    Example:
    --------
    >>> longestCommonPrefix(["flower", "flow", "flight"])
    'fl'
    >>> longestCommonPrefix(["dog", "racecar", "car"])
    ''
    """

    # Edge case: if input list is empty
    if not strs:
        return ""

    # Assume first string as prefix
    prefix = strs[0]

    # Compare prefix with all other strings
    for word in strs[1:]:
        # Shrink prefix until it matches the beginning of 'word'
        while not word.startswith(prefix):
            prefix = prefix[:-1]  # remove last character
            if prefix == "":
                return ""
    return prefix


# ✅ Test cases
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Expected: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))     # Expected: ""
