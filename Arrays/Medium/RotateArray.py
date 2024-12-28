"""Given an integer array nums, rotate the array to the right by k steps, where k is non-negative."""

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the array to the right by k steps.
        """
        n = len(nums)
        k %= n  
        
        
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)