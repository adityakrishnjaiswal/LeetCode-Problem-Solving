"""Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring."""

class Solution:
    def maxScore(self, s: str) -> int:
        # Initial counts
        total_ones = s.count('1')  # Total ones in the string
        left_zeros = 0  # Track zeros in the left part
        right_ones = total_ones  # Initially, right contains all ones
        
        max_score = 0
        
        # Iterate through the string, except the last character
        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zeros += 1  # Add to left zeros
            else:
                right_ones -= 1  # Remove from right ones
            
            # Calculate the score for the current split
            current_score = left_zeros + right_ones
            max_score = max(max_score, current_score)
        
        return max_score
        