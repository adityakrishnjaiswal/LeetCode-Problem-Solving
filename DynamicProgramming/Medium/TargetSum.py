"""You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target."""

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # Step 1: Calculate the total sum of the array
        total_sum = sum(nums)
        
        # Step 2: Check if a valid subset sum exists
        # (total_sum + target) must be even, and total_sum must be >= abs(target)
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0
        
        # Step 3: Calculate the subset sum to find
        # Subset sum problem: Find a subset with sum = (total_sum + target) / 2
        target_sum = (total_sum + target) // 2
        
        # Step 4: Initialize a DP array to store the number of ways to form each sum
        dp = [0] * (target_sum + 1)
        dp[0] = 1  # Base case: There is one way to make sum 0 (empty subset)
        
        # Step 5: Iterate through each number in nums
        for num in nums:
            # Traverse the DP array backwards to avoid overwriting values
            for j in range(target_sum, num - 1, -1):
                # Update the number of ways to achieve sum j
                dp[j] += dp[j - num]
        
        # Step 6: Return the number of ways to achieve the target subset sum
        return dp[target_sum]
