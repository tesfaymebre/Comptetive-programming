class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        
        def dp(pos:int,bought:bool) -> int:
            if pos == len(prices):
                return 0
            
            if (pos,bought) in memo:
                return memo[(pos,bought)]
            
            max_profit = 0
            
            if not bought:
                max_profit = max(max_profit,dp(pos+1,True) - prices[pos])
            else:
                max_profit = max(max_profit,dp(pos+1,False) + prices[pos] - fee)
                
            max_profit = max(max_profit,dp(pos+1,bought))
            
            memo[(pos,bought)] = max_profit
            return memo[(pos,bought)]
        
        return dp(0,False)
        