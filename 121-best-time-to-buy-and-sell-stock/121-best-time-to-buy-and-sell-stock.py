class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = prices[-1]
        profit = 0
        
        for i in range(len(prices)-2,-1,-1):
            if prices[i] >= maxx:
                maxx = prices[i]
            else:
                profit = max(profit, maxx - prices[i])
        return profit
                