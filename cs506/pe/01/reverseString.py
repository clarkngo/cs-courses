from typing import List

def reverseString(s: List[str]) -> None:
    """
    Reverses a string (list of characters) in-place with O(1) extra memory.
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Swap the characters at the left and right pointers
        s[left], s[right] = s[right], s[left]
        
        # Move the pointers towards the center
        left += 1
        right -= 1

# Example Usage 1:
# arr1 = ["h","e","l","l","o"]
# reverseString(arr1)
# print(f"Reversed 1: {arr1}")  # Output: ['o', 'l', 'l', 'e', 'h']

# Example Usage 2:
# arr2 = ["H","a","n","n","a","h"]
# reverseString(arr2)
# print(f"Reversed 2: {arr2}")  # Output: ['h', 'a', 'n', 'n', 'a', 'H']
