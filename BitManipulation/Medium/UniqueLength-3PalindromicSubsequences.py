"""Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
A palindrome is a string that reads the same forwards and backwards.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters."""

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique_palindromes = 0
    
        # Iterate over each unique character as outer characters
        for ch in set(s):
            first = s.find(ch)  # First occurrence
            last = s.rfind(ch)  # Last occurrence
            
            # If valid palindrome structure is possible
            if first < last:
                # Get unique characters in the middle substring
                middle_chars = set(s[first + 1:last])
                unique_palindromes += len(middle_chars)
        
        return unique_palindromes