"""Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums."""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0  # Pointer for the valid position
    
        for i in range(len(nums)):
            if j < 2 or nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1