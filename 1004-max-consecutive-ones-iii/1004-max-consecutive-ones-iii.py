class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right = 0,0
        
        while right < len(nums):
            k -= 1 - nums[right]
            right += 1
            
            if k < 0:
                k += 1 - nums[left]
                left += 1
                
        return right - left