class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        result = 0
        minBuy = prices[0]

        # Attempt to optimize

        for i in range(1, len(prices)):
            minBuy = min(minBuy, prices[i - 1])

            maxProfit = prices[i] - minBuy

            result = max(maxProfit, result)
        
        return result