class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
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