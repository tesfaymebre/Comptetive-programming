class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #bottom up dp solution
        
        size = len(coins)
        dp = [[1]+[0]*amount for _ in range(size+1)]
        
        for pos in range(size-1,-1,-1):
            for capacity in range(amount+1):
                if capacity >= coins[pos]:
                    dp[pos][capacity] = dp[pos][capacity-coins[pos]] + dp[pos+1][capacity]
                else:
                    dp[pos][capacity] = dp[pos+1][capacity]
                    
        return dp[0][amount]
        
        """
        #top down dp solution with memoization
        
        def helper(pos,capacity):
            if (pos,capacity) not in memo:
                if capacity == 0:
                    return 1

                if pos == len(coins):
                    return 0

                pick = 0

                if capacity >= coins[pos]:
                    pick += helper(pos,capacity-coins[pos])

                not_pick = helper(pos+1,capacity)

                memo[(pos,capacity)] = pick + not_pick   
                
            return memo[(pos,capacity)]
        
        memo = {}
        return helper(0,amount)
        """