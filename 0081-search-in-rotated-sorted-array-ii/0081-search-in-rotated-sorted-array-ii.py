class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left = 0
        right = n-1
        
        while left <= right:
            while left + 1 < right and nums[left] == nums[left+1]:
                left += 1
            
            while right - 1 > left and nums[right] == nums[right-1]:
                right -= 1
                
            mid = left + (right-left)//2
            
            if target == nums[mid]:
                return True
            
            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
        return False