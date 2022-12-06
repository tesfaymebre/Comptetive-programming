class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #space optimized bottom up dp solution
        size = len(coins)
        dp = [0]+[float('inf')]*amount
        
        for capacity in range(amount+1):
            
            for i in range(size):
                if capacity >= coins[i]:
                    dp[capacity] = min(dp[capacity],1 + dp[capacity-coins[i]])
            
        return dp[amount] if dp[amount] != float('inf') else -1
        
        """
        # space optimized top down dp solution
        def helper(capacity):
            if capacity not in memo:
                if capacity == 0:
                    return 0

                count = float('inf')

                for i in range(len(coins)):
                    if capacity >= coins[i]:
                        count = min(count,1 + helper(capacity-coins[i]))

                memo[capacity] = count
            
            return memo[capacity]
        
        memo = {}
        ans = helper(amount)
        
        return ans if ans != float('inf') else -1
        """
        
        """
        #bottom up dp solution
        size = len(coins)
        dp = [[0]+[float('inf')]*(amount) for _ in range(size+1)]
        
        for pos in range(size-1,-1,-1):
            for capacity in range(amount+1):
                pick = float('inf')
                
                if capacity >= coins[pos]:
                    pick = 1 + dp[pos][capacity-coins[pos]]
                    
                not_pick = dp[pos+1][capacity]
                
                dp[pos][capacity] = min(pick,not_pick)
                
        ans = dp[0][amount]
        return ans if ans != float('inf') else -1
        """
        
        """
        #top down dp solution
        
        def dp(pos,capacity):
            if (pos,capacity) not in memo:
                if capacity == 0:
                    return 0
                if pos == len(coins):
                    return float('inf')

                pick = float('inf')

                if capacity >= coins[pos]:
                    pick = 1 + dp(pos,capacity-coins[pos])

                not_pick = dp(pos+1,capacity)

                memo[(pos,capacity)] = min(pick,not_pick)
                
            return memo[(pos,capacity)]
        
        memo = {}
        ans = dp(0,amount)
        
        return ans if ans != float('inf') else -1
        """
        