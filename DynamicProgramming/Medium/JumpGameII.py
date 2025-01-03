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
        
        # Step 1: Initialize DP array
        dp = [float('inf')] * n
        dp[0] = 0  # Starting point requires no jump
        
        # Step 2: Fill the DP array
        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i:  # Check if we can jump from j to i
                    dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[-1]
