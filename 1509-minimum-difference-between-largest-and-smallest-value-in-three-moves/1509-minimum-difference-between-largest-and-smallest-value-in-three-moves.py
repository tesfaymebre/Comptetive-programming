class Solution:
    def minDifference(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 3:
            return 0
        
        nums.sort()
        first = max(nums[3:]) - min(nums[3:])
        second = max(nums[:size-3]) - min(nums[:size-3])
        third = max(nums[2:size-1]) - min(nums[2:size-1])
        fourth = max(nums[1:size-2]) - min(nums[1:size-2])
                    
        return min(first,second,third,fourth)