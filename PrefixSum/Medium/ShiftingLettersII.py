"""You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.
Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').
Return the final string after all such shifts to s are applied."""

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift = [0] * (n + 1)  # Initialize difference array
        
        # Apply shifts using difference array technique
        for start, end, direction in shifts:
            if direction == 1:
                shift[start] += 1
                shift[end + 1] -= 1
            else:
                shift[start] -= 1
                shift[end + 1] += 1
        
        # Calculate prefix sum to get the final shift for each character
        for i in range(1, n):
            shift[i] += shift[i - 1]
        
        # Build the final string
        result = []
        for i in range(n):
            # Normalize the shift to handle negative shifts
            normalized_shift = (shift[i] % 26 + 26) % 26
            new_char = chr((ord(s[i]) - ord('a') + normalized_shift) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)   