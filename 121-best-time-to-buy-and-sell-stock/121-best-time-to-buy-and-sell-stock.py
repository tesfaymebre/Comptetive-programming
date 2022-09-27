class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = prices[0]
        profit = 0
        
        for x in prices:
            profit = max(profit, x - minn)
            minn = min(minn,x)
            
        return profit
                