"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation."""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # Initialize answer array with 1
        
        # Step 1: Calculate prefix products
        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product  # Store prefix product so far
            prefix_product *= nums[i]   # Update prefix product
        
        # Step 2: Calculate suffix products and finalize result
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product  # Multiply current answer by suffix product
            suffix_product *= nums[i]    # Update suffix product
        
        return answer