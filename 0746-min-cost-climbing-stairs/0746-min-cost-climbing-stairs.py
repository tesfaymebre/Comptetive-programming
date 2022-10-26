class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #bottom up space optimized dp solution
        first = 0
        second = 0
        
        for i in range(len(cost)-1,-1,-1):
            curr = cost[i] + min(first,second)
            second = first
            first = curr
            
        return min(first,second)
    
        """
        #bottom up dp solution
        dp = [0]*(len(cost)+2)
        
        for i in range(len(cost)-1,-1,-1):
            dp[i] = cost[i] + min(dp[i+1],dp[i+2])
        
        return min(dp[0],dp[1])
        """
        
    
        """
        #top down dp solution
        memo = {}
        
        def dp(i):
            if i >= len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(dp(i+1),dp(i+2))
            return memo[i]
        
        return min(dp(0),dp(1)) 
        """       