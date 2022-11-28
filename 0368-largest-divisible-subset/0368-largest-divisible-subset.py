class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        #bottom up solution
        nums.sort()
        dp = [[num] for num in nums]
        idx_max = 0
        
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i] % nums[j] == 0) and len(dp[i]) < len(dp[j])+1:
                    dp[i] = dp[j] + [nums[i]]
                    
            if len(dp[idx_max]) < len(dp[i]):
                idx_max = i
        
        return dp[idx_max]
    
        """
        #top down solution
        seen = {}
        
        def helper(idx,path):
            if len(self.res) < len(path):
                self.res = path[:]
            
            for i in range(idx+1,len(nums)):
                if nums[i] % nums[idx] == 0:
                    if nums[i] not in seen or seen[nums[i]] < len(path):
                        seen[nums[i]] = len(path)
                        helper(i,path + [nums[i]])
                    
            return
        
        nums.sort()
        self.res = []
        
        for i in range(len(nums)):
            helper(i,[nums[i]])
       
        return self.res
        """
            