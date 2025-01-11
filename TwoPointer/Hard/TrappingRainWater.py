"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining."""

from typing import List

class Solution:
    def trap(self, height: list[int]) -> int:
        if not height or len(height) < 3:
            return 0  # No water can be trapped with less than 3 bars
        
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_trapped = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1
        
        return water_trapped