class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #bottom up dp solution

        n = len(prices)
        max_transactions = 2  
        dp = [[[0 for _ in range(2)] for _ in range(max_transactions + 1)] for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for transaction in range(1,max_transactions + 1):
                for bought in range(2):
                    profit = dp[i+1][transaction][bought]
                    
                    if bought:
                        profit = max(profit, dp[i + 1][transaction - 1][0] + prices[i])
                    else:
                        profit = max(profit, dp[i + 1][transaction][1] - prices[i])
                        
                    dp[i][transaction][bought] = profit
        
        return dp[0][2][0]

        
        """
        # top  down dp solution
        memo = {}
        
        def dp(i, transaction, bought):
            if (i,transaction,bought) not in memo:
                if i >= len(prices) or transaction == 0:
                    return 0

                # Skip
                profit = dp(i + 1, transaction, bought);

                # Sell
                if bought:
                    profit = max(profit, dp(i + 1, transaction - 1, not bought) + prices[i])
                # Buy
                else:
                    profit = max(profit, dp(i + 1, transaction, not bought) - prices[i])

                memo[(i,transaction,bought)] = profit
                
            return memo[(i,transaction,bought)]
        
        return dp(0, 2, False)
        """