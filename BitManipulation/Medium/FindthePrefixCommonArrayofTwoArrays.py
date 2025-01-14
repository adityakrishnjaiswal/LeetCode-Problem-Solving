"""You are given two 0-indexed integer permutations A and B of length n.
A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.
Return the prefix common array of A and B.
A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once."""

from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen_A = set()
        seen_B = set()
        C = [0] * n
        
        for i in range(n):
            seen_A.add(A[i])
            seen_B.add(B[i])
            # Compute the common elements count
            C[i] = len(seen_A & seen_B)
        
        return C