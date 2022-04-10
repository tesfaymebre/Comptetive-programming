class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i, memo = {}):
            if i in memo:
                return memo[i]
            
            if i >= len(cost) - 2:
                return cost[i]
            
            memo[i] = cost[i] + min(dp(i+1,memo), dp(i + 2, memo))
            return memo[i]
        
        return min(dp(0), dp(1))
        