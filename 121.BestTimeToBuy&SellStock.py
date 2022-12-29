"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan&id=level-1
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sellDate = 0
        holdDate = -math.inf

        for price in prices:
            sellDate = max(sellDate, holdDate+price)
            holdDate = max(holdDate, -price)
        return sellDate