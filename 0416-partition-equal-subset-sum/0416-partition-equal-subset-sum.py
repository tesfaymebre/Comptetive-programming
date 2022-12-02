class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #space optimized bottom up dp solution
        
        total = sum(nums)
        maxx = max(nums)
        
        if total & 1 == 1:
            return False
        
        dp = [True]+[False]*(total//2 + maxx)
        
        
        for idx in range(len(nums)):
            for curr_total in range((total//2),-1,-1):
                dp[curr_total] = dp[curr_total-nums[idx]] or dp[curr_total]
                
            if dp[total//2]:
                return True
            
        return False
        
        """
        #bottom up dp solution
        total = sum(nums)
        maxx = max(nums)
        
        if total & 1 == 1:
            return False
        
        dp = [[True]+[False]*(total//2 + maxx) for _ in range(len(nums)+1)]
        
        
        for idx in range(1,len(nums)+1):
            for curr_total in range(total//2 + 1):
                dp[idx][curr_total] = dp[idx-1][curr_total-nums[idx-1]] or dp[idx-1][curr_total]
                
            if dp[idx][total//2]:
                return True
            
        return False
        """
        
        """
        # top down dp solution
        memo = {}
        
        def helper(idx,curr_total):
            if (idx,curr_total) not in memo:
            
                if curr_total == 0:
                    return True

                if idx == len(nums) or curr_total < 0:
                    return False

                memo[(idx,curr_total)] = helper(idx+1,curr_total-nums[idx]) or helper(idx+1,curr_total)
            
            return memo[(idx,curr_total)]
        
        total = sum(nums)
        
        if total&1 == 1:
            return False
        
        return helper(0,total//2)
        """
        