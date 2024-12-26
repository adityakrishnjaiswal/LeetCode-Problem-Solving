"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets."""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the array to make it easier to find triplets
        nums.sort()
        
        result = []  # This will store the list of valid triplets
        
        # Step 2: Iterate through the array, fixing one number at a time
        for i in range(len(nums) - 2):  # We stop 2 elements before the end to leave space for the left and right pointers
            
            # Step 3: Skip duplicate values for the fixed number (nums[i])
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # If the current number is the same as the previous one, skip it to avoid duplicates
            
            left, right = i + 1, len(nums) - 1  # Initialize two pointers: left just after the current number, right at the end
            
            # Step 4: Use the two-pointer approach to find the remaining two numbers
            while left < right:
                total = nums[i] + nums[left] + nums[right]  # Calculate the sum of the current triplet
                
                if total == 0:  # If the sum is zero, we found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])  # Add the triplet to the result list
                    left += 1  # Move the left pointer to the right
                    right -= 1  # Move the right pointer to the left
                    
                    # Step 5: Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    # Step 6: Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif total < 0:  # If the sum is less than zero, we need a larger sum
                    left += 1  # Move the left pointer to the right to increase the sum
                else:  # If the sum is greater than zero, we need a smaller sum
                    right -= 1  # Move the right pointer to the left to decrease the sum
        
        # Step 7: Return the list of triplets
        return result
