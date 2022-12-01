class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dp(i, part):
            if (i, part) in memo:
                return memo[(i, part)]
            if part == 0:
                return True
            if i >= len(nums):
                return False
            
            if dp(i + 1 , part - nums[i]) or dp(i + 1, part):
                memo[(i, part)] = True
                return True
            memo[(i, part)] = False
            return False
        
        memo = {}
        totalSum = sum(nums)
        if totalSum % 2 == 1:
            return False
        
        partition = totalSum // 2
        return dp(0, partition)
        
        