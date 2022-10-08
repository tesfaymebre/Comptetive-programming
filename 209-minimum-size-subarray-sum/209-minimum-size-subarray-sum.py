class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        min_size = len(nums) + 1
        total = 0
        
        for j in range(len(nums)):
            total += nums[j]
            
            while total >= target:
                min_size = min(min_size,j - i + 1)
                total -= nums[i]
                i += 1
                
        return min_size if min_size != len(nums) + 1 else 0