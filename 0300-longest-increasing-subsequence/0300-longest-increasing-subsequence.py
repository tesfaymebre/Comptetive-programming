class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #bottom up
        dp = [1]*len(nums)
        maxi = 1
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
                    maxi = max(maxi,dp[i])
                    
        return maxi
        """
        #top down
        @cache
        def dfs(k,prev):
	        if k==len(nums):
	        	return 0
	        longest = 0
	        for i in range(k,len(nums)):
	        	if nums[i] > prev:
	        		curr = 1 + dfs(i+1, nums[i])
	        		longest = max(longest, curr)
	        return longest
        return dfs(0,-float("inf"))
        """
        
    
       