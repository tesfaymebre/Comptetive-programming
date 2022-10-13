class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        
        if not nums: return ans
        
        left,right = 0,len(nums) - 1
        
        while left <= right:
            mid = left + (right - left)//2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        if left < len(nums) and nums[left] == target: ans[0] = left
        
        left,right = 0,len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        if nums[left-1] == target: ans[1] = left-1
                
        return ans