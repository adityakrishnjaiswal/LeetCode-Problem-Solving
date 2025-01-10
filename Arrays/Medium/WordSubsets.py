"""You are given two string arrays words1 and words2.
A string b is a subset of string a if every letter in b occurs in a including multiplicity.
For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.
Return an array of all the universal strings in words1. You may return the answer in any order"""

from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Step 1: Calculate the max frequency of each character required by words2
        required = Counter()
        
        for word in words2:
            word_count = Counter(word)
            for char, count in word_count.items():
                required[char] = max(required[char], count)
        
        # Step 2: Check each word in words1 if it is a superset of required characters
        result = []
        
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= required[char] for char in required):
                result.append(word)
        
        return result