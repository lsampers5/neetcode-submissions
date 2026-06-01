class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        result = 0
        buy = []

        # Attempt to optimize

        for i in range(1, len(prices)):
            buy.append(prices[i - 1])

            maxProfit = prices[i] - min(buy)

            result = max(maxProfit, result)
        
        return result