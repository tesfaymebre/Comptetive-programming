class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #dp with hash
        
        steps = defaultdict(int)
        steps[0] = 1
        
        for val in nums:
            next_steps = defaultdict(int)
            
            for step in steps:
                next_steps[step+val] += steps[step]
                next_steps[step-val] += steps[step]
                
            steps = next_steps
            
        return steps[target]
        
        """
        #space optimized bottom up dp soltution
        
        size = len(nums)
        total = sum(nums)
        
        dp = [[0]*(2*total+max(nums)+1) for _ in range(2)]
        dp[size&1][target+total] = 1
        
        for idx in range(size-1,-1,-1):
            for curr_sum in range(-total,total+1):
                dp[idx&1][curr_sum + total] = dp[(idx+1)&1][curr_sum-nums[idx]+total]
                dp[idx&1][curr_sum + total] += dp[(idx+1)&1][curr_sum+nums[idx]+total]
                
        return dp[0][total]
    
        #time complexity: O(total*n) 
        #space complexity: O(2*total) = O(total)
        """
    
        """
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
        
        #time complexity: O(2*total*n) = O(total*n) 
                            where total = sum(nums) and n = len(nums)
        #space complexity: O(total*n)
        """
                
        
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
        
        #time complexity: O(2*total*n) = O(total*n) 
                            where total = sum(nums) and n = len(nums)
        #space complexity: O(total*n)
         
        """