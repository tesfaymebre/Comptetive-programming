class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        current_product = 1
        left = 0
        
        for right in range(len(nums)):
            current_product *= nums[right]
            
            while left <= right and current_product >= k:
                current_product /= nums[left]
                left += 1
                
            count += right - left + 1 
            
        return count
        