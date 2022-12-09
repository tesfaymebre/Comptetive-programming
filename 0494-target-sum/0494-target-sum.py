class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(idx,total):
            if (idx,total) not in memo:
                if idx == len(nums):
                    return total == target
                
                memo[(idx,total)] = dp(idx+1,total+nums[idx]) + dp(idx+1,total-nums[idx])
                
            return memo[(idx,total)]
        
        memo = {}
        
        return dp(0,0)