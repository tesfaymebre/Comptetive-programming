class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        for j in range(1,len(nums) + 2,1):
            if j not in nums:
                return j