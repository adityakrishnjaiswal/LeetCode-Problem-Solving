"""You are given a list of strings of the same length words and a string target.
Your task is to form target using the given words under the following rules:
target should be formed from left to right.
To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.
Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7."""

from collections import Counter
from functools import lru_cache
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(words), len(words[0])  # m: number of words, n: length of each word
        
        # Step 1: Count character frequencies in each column
        freq = [Counter() for _ in range(n)]
        for col in range(n):
            for word in words:
                freq[col][word[col]] += 1
        
        # Step 2: DP memoization
        @lru_cache(None)
        def dp(i, j):
            """
            i: index of the current target character
            j: current column index in words
            """
            # Base cases
            if i == len(target): 
                return 1  # Successfully formed the target
            if j == n:
                return 0  # Ran out of columns
            
            # Option 1: Skip this column
            res = dp(i, j + 1) % MOD  
            
            # Option 2: Use this column if possible
            char = target[i]
            if char in freq[j]:
                res += freq[j][char] * dp(i + 1, j + 1)
                res %= MOD
            
            return res
        
        return dp(0, 0)
