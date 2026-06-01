class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        result = 0

        # I have failed a lot so I guess just gonna brute force it so I could get something working

        for buy in range(len(prices) - 1):

            for sell in range(buy, len(prices)):

                profit = prices[sell] - prices[buy]

                result = max(profit, result)
        
        return result



            




        