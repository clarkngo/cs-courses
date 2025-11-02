from typing import List

def removeDuplicates(nums: List[int]) -> int:
    """
    Removes duplicates in-place from a sorted array and returns the new length.
    """
    if not nums:
        return 0
    
    # 'i' is the slow-pointer, tracking the position of the next unique element
    i = 0 
    
    # 'j' is the fast-pointer, iterating through the array
    for j in range(1, len(nums)):
        # If the current element (j) is different from the last unique element (i),
        # it means we've found a new unique number.
        if nums[j] != nums[i]:
            i += 1
            # Overwrite the element at i+1 with the new unique value
            nums[i] = nums[j]
            
    # The new length is i + 1 (since i is a 0-based index)
    return i + 1

# Example Usage 1:
# nums1 = [1,1,2]
# length1 = removeDuplicates(nums1)
# print(f"New length 1: {length1}, Array prefix: {nums1[:length1]}")  
# # Output: 2, Array prefix: [1, 2]

# Example Usage 2:
# nums2 = [0,0,1,1,1,2,2,3,3,4]
# length2 = removeDuplicates(nums2)
# print(f"New length 2: {length2}, Array prefix: {nums2[:length2]}")  
# # Output: 5, Array prefix: [0, 1, 2, 3, 4]
