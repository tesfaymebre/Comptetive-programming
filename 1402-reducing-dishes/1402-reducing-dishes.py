class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
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