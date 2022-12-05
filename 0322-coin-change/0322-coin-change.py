class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
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