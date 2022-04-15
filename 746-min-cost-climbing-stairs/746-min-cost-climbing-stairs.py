class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {len(cost)-2: cost[-2], len(cost)-1: cost[-1]}
        
        def dp(i):
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(dp(i+1),dp(i+2))
            return memo[i]
        
        return min(dp(0),dp(1))        