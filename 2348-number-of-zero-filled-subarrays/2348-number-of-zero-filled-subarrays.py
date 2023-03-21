class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] != 0:
                left = right + 1
            else:
                count += right - left + 1
                
        return count