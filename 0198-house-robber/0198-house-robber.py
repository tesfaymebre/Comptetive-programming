class Solution:
    def rob(self, nums: List[int]) -> int:
        
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