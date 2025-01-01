"""You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve."""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # Initialize DP table
        dp = [[0, 0] for _ in range(n)]
        
        # Base case
        dp[0][0] = -prices[0]  # Holding a stock on day 0
        dp[0][1] = 0           # Not holding a stock on day 0
        
        # Fill DP table
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])  # Hold state
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])  # No-Hold state
        
        # Return the maximum profit at the end without holding a stock
        return dp[n-1][1]