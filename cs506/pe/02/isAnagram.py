from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    """
    Determine if string 't' is an anagram of string 's'.
    
    Parameters:
    -----------
    s : str
        The original string.
    t : str
        The string to compare against 's'.
        
    Returns:
    --------
    bool
        True if 't' is an anagram of 's', False otherwise.
    
    Example:
    --------
    >>> isAnagram("anagram", "nagaram")
    True
    >>> isAnagram("rat", "car")
    False
    """

    # 🧩 Step 1: Quick length check — if different, can't be anagrams
    if len(s) != len(t):
        return False

    # 🧩 Step 2: Use Counter to count frequency of each character
    counter_s = Counter(s)
    counter_t = Counter(t)

    # 🧩 Step 3: Compare both dictionaries
    return counter_s == counter_t


# ✅ Test cases
print(isAnagram("anagram", "nagaram"))  # Expected output: True
print(isAnagram("rat", "car"))          # Expected output: False
print(isAnagram("", ""))                # Expected output: True
