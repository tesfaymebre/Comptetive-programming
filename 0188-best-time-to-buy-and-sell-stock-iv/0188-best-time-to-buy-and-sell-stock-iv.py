class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
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
        
        return dp(0, k, False)