class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = float('inf')
        highestProfit = 0
        for n in prices:
            lowestPrice = min(lowestPrice,n)
            highestProfit = max((n-lowestPrice),highestProfit)

        return highestProfit

        