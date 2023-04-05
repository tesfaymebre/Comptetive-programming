class Solution:
    def check(self,mid,nums):
        last = nums[-1]
        
        for i in range(len(nums)-1,0,-1):
            if last > mid:
                last = nums[i-1] + last - mid
            else:
                last = nums[i-1]
               
        if last > mid:
            return False
        
        return True
    
    def minimizeArrayValue(self, nums: List[int]) -> int:
        left = 0
        right = max(nums)
        
        while left <= right:
            mid = left + (right - left)//2
            
            if self.check(mid,nums):
                right = mid - 1
            else:
                left = mid + 1
                
        return left