"""Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise."""

from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If k is greater than the length of the string, return False
        if k > len(s):
            return False
        
        odd_count = 0
        
        # Iterate over the frequency counts and track the number of odd frequencies
        for count in Counter(s).values():
            if count % 2 != 0:
                odd_count += 1
        
        # If odd_count is greater than k, it's not possible to form k palindromes
        return odd_count <= k