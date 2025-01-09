"""You are given an array of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s."""

from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        a=0
        for word in words:
            if pref == word[:len(pref)]:
                a+=1
        return a