class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        i,j = 0,0
        min_size = len(nums)
        total = 0
        
        while j < len(nums):
            total += nums[j]
            j += 1
            
            while total >= target and i < j:
                min_size = min(min_size,j-i)
                total -= nums[i]
                i += 1
                
        return min_size