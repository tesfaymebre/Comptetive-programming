class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #bottom up dp solution
        n = len(days)
        dp = [float('inf')]*(n+1)
        dp[n] = 0
        
        for idx in range(n-1,-1,-1):
            for i,passes in enumerate([1,7,30]):
                temp = bisect.bisect_left(days,days[idx]+passes-1)
                
                if temp < n and days[temp] == days[idx]+passes-1:
                    dp[idx] = min(dp[idx],costs[i] + dp[temp+1])
                else:
                    dp[idx] = min(dp[idx],costs[i]+dp[temp])
                    
        return dp[0]
        
        """
        #top down dp solution
        def dp(idx):
            if idx not in memo:
                if idx >= len(days):
                    return 0

                cost = float('inf')
                for i,passes in enumerate([1,7,30]):
                    temp = bisect.bisect_left(days,days[idx]+passes-1)

                    if temp < len(days) and days[temp] == days[idx]+passes-1:
                        cost = min(costs[i] + dp(temp+1),cost)
                    else:
                        cost = min(costs[i] + dp(temp),cost)

                memo[idx] = cost
                
            return memo[idx]
        
        memo = {}
        return dp(0)
        """