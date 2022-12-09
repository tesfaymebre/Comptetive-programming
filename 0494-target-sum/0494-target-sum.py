class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #bottom up dp soltution
        size = len(nums)
        total = sum(nums)
        
        dp = [[0]*(2*total+max(nums)+1) for _ in range(size+1)]
        dp[size][target+total] = 1
        
        for idx in range(size-1,-1,-1):
            for curr_sum in range(-total,total+1):
                dp[idx][curr_sum + total] += dp[idx+1][curr_sum-nums[idx]+total]
                dp[idx][curr_sum + total] += dp[idx+1][curr_sum+nums[idx]+total]
                
        return dp[0][total]
                
        
        """
        #top down dp solution
        
        def dp(idx,total):
            if (idx,total) not in memo:
                if idx == len(nums):
                    return total == target
                
                memo[(idx,total)] = dp(idx+1,total+nums[idx]) + dp(idx+1,total-nums[idx])
                
            return memo[(idx,total)]
        
        memo = {}
        
        return dp(0,0)
        """