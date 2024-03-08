class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def helper(minimized_largest_sum):
            subarrays = 1
            curr_sum = 0
            
            for num in nums:
                curr_sum += num
                
                if curr_sum > minimized_largest_sum:
                    subarrays += 1
                    curr_sum = num
                    
                if subarrays > k:
                    return False
                
            return True
    
        left = max(nums)
        right = sum(nums)
        best = right
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if helper(mid):
                right = mid - 1
                best = mid
            else:
                left = mid + 1
                
        return best