class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #binary search solution
        accumulate = [nums[0]]
        
        def BS(num):
            left = 0
            right = len(accumulate)-1

            while left <= right:
                mid = left + (right-left)//2
                
                if accumulate[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return left
        
        for num in nums:
            pos = BS(num)
            
            if pos == len(accumulate):
                accumulate.append(num)
            else:
                accumulate[pos] = num
                
        return len(accumulate)
    
    
        """
        #bottom up
        dp = [1]*len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
                    
        return max(dp)
        """
        
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
        
    
       