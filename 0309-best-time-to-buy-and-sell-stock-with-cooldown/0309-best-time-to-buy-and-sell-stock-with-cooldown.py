class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #bottom up dp solution
        size = len(prices)
        dp = [[0,0] for _ in range(size+2)]
        
        for idx in range(size-1,-1,-1):
            for status in ['sell','buy']:
                profit = 0
                
                if status == 'buy':
                    buy = -1*prices[idx] + dp[idx+1][1]
                    not_buy = dp[idx+1][0]
                    profit += max(buy,not_buy)
                    dp[idx][0] = profit
                else:
                    sell = prices[idx] + dp[idx+2][0]
                    not_sell = dp[idx+1][1]
                    profit += max(sell,not_sell)
                    dp[idx][1] = profit
                    
        return dp[0][0]
        
        """
        #top down dp solution
        
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
        
        #time complexity: O(2n)== O(n)
        #space complexity: O(2n) == O(n)
        """
        