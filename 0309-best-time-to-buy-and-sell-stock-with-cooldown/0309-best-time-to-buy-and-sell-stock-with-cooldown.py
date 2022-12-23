class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dp(idx,status):
            if (idx,status) not in memo:
                if idx >= len(prices):
                    return 0

                profit = 0

                if status == 'buy':
                    buy = -1*prices[idx] + dp(idx+1,'sell')
                    not_buy = dp(idx+1,'buy')
                    profit += max(buy,not_buy)
                else:
                    sell = prices[idx] + dp(idx+2,'buy')
                    not_sell = dp(idx+1,'sell')
                    profit += max(sell,not_sell)

                memo[(idx,status)] = profit
                
            return memo[(idx,status)]
        
        memo = {}
        max_profit = dp(0,'buy')
        
        return max_profit