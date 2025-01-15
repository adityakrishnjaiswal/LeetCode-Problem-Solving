"""Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ""."""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        if prefix == "":
            return ""
        for i in range (len(strs)):
            if prefix == "":
                exit
            for j in range (len(prefix)):
                if len(prefix) == 0:
                    return ""
                if len(prefix)<j:
                    exit
                elif j==len(strs[i]) or prefix[j] != strs[i][j]:
                    prefix = prefix[:j]
                    exit
        return prefix