class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        #bottom up dp solution
        satisfaction.sort()
        size = len(satisfaction)
        dp = [[0]*(size+2) for _ in range(size+1)]
        
        for idx in range(size-1,-1,-1):
            for time in range(size,0,-1):
                cook = satisfaction[idx]*time + dp[idx+1][time+1]
                not_cook = dp[idx+1][time]
                dp[idx][time] = max(cook,not_cook)
                
        return dp[0][1]
        
        """
        #top down dp solution
        def dp(idx,time):
            if (idx,time) not in memo:
                if idx >= len(satisfaction):
                    return 0

                cook = satisfaction[idx]*time + dp(idx+1,time+1)
                not_cook = dp(idx+1,time)

                memo[(idx,time)] = max(cook,not_cook)
                
            return memo[(idx,time)]
        
        memo = {}
        satisfaction.sort()
        return dp(0,1)
        """