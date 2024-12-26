"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""

from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty HashMap (dictionary) to store numbers and their corresponding indices
        num_map = {}
        
        # Iterate through the list of numbers and their indices
        for i, num in enumerate(nums):
            # Calculate the complement (the number we need to find)
            complement = target - num  
            
            # Check if the complement exists in the HashMap
            if complement in num_map:
                # If found, return the indices of the current number and the complement
                return [num_map[complement], i]
            
            # Otherwise, store the current number and its index in the HashMap
            num_map[num] = i
