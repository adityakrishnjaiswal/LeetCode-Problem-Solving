"""You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1]."""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0  # Already at the last index
        
        jumps = 0          # Count of jumps
        current_reach = 0  # Current maximum reach
        next_reach = 0     # Next maximum reach
        
        for i in range(n - 1):
            next_reach = max(next_reach, i + nums[i])
            
            if i == current_reach:
                jumps += 1
                current_reach = next_reach
                
                if current_reach >= n - 1:
                    break  # If we can reach the end, stop early
        
        return jumps
