"""You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise."""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0  # Tracks the farthest index reachable
    
        for i in range(len(nums)):
            if i > farthest:  # If current index is beyond farthest reachable index
                return False
            farthest = max(farthest, i + nums[i])  # Update farthest reachable index
        
        return True