class Solution:
    def minDifference(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 3:
            return 0
        
        nums.sort()
        smallest = float('inf')
        
        for i in range(4):
            smallest = min(smallest,nums[i-4] - nums[i])
            
        return smallest