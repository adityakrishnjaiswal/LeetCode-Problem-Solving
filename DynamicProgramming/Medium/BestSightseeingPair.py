"""You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.
The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.
Return the maximum score of a pair of sightseeing spots."""

from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        max_i = values[0]  # Store the best `values[i] + i` seen so far

        for j in range(1, len(values)):
            # Calculate score with the best previous `i`
            max_score = max(max_score, max_i + values[j] - j)
            # Update max_i for the next iteration
            max_i = max(max_i, values[j] + j)
        
        return max_score
