class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def helper(idx,sub1):
            if idx == len(nums) or sub1 == total - sub1:
                return sub1 == total - sub1
            
            if sub1 > total - sub1:
                return False
            
            return helper(idx+1,sub1+nums[idx]) or helper(idx+1,sub1)
        
        total = sum(nums)
        return helper(0,0)