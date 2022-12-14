class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up dp solution
        
        size = len(nums)
        dp = [0]*(size+2)
        
        for idx in range(size-1,-1,-1):
            pick = nums[idx] + dp[idx+2]
            not_pick = dp[idx+1]
            
            dp[idx] = max(pick,not_pick)
            
        return dp[0]
        
        """
        #top down dp solution
        
        def dp(idx):
            if idx not in memo:
                if idx >= len(nums):
                    return 0

                pick = nums[idx] + dp(idx+2)
                not_pick = dp(idx+1)

                memo[idx] = max(pick,not_pick)
                
            return memo[idx]
        
        memo = {}
        return dp(0)
        """