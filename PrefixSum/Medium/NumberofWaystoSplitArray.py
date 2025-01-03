"""You are given a 0-indexed integer array nums of length n.
nums contains a valid split at index i if the following are true:
The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums."""



from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        
        # Step 2: Initialize prefix sum and valid split counter
        prefix_sum = 0
        valid_split_count = 0
        
        # Step 3: Iterate through the array (excluding the last index)
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            right_sum = total_sum - prefix_sum
            
            # Step 4: Check if the current split is valid
            if prefix_sum >= right_sum:
                valid_split_count += 1
        
        return valid_split_count