from typing import List

def checkIfExist(arr: List[int]) -> bool:
    """
    Checks if there exist two distinct integers N and M in the array such that N = 2 * M.
    """
    seen = set()
    
    for num in arr:
        # Check if 2*num (N = 2*M) OR num/2 (M = N/2) is already in the set
        # The first case handles N = 2*M.
        # The second case handles M = N/2, but we must check for floating point
        # division remainder to ensure it's an integer division (i.e., N is even).
        
        # 1. Check for N = 2 * num (if num is M, is 2*M in seen?)
        if 2 * num in seen:
            return True
        
        # 2. Check for M = num / 2 (if num is N, is N/2 in seen?)
        # Check if num is even and num / 2 is in the set.
        if num % 2 == 0 and num // 2 in seen:
            return True
        
        # Add the current number to the set for future checks
        seen.add(num)
        
    return False

# Example Usage 1:
# print(f"Exists in [10,2,5,3]: {checkIfExist([10,2,5,3])}")    # Output: True (10 = 2*5)

# Example Usage 2:
# print(f"Exists in [7,1,14,11]: {checkIfExist([7,1,14,11])}")  # Output: True (14 = 2*7)

# Example Usage 3:
# print(f"Exists in [3,1,7,11]: {checkIfExist([3,1,7,11])}")    # Output: False

# Edge Case (Zero): The only issue is [0, 0] must return True (0=2*0, i!=j), 
# while [0] must return False. Our check handles this because we only add the number
# to the set *after* the check. For arr=[0, 0]:
#   - Loop 1 (num=0): Check 2*0 (0) and 0/2 (0). 0 not in seen. Add 0. seen={0}.
#   - Loop 2 (num=0): Check 2*0 (0). 0 **is** in seen. Returns True. (Correct)
# print(f"Exists in [0, 0]: {checkIfExist([0, 0])}")            # Output: True
# print(f"Exists in [0]: {checkIfExist([0])}")                  # Output: False
