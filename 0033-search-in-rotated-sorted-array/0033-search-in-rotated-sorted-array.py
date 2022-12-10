class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        
        for i in range(1,n):
            if nums[i-1] > nums[i]:
                left = i
                break
                
        right = (left-1)+len(nums)
        
        while left <= right:
            mid = left + (right-left)//2
            
            if nums[mid%n] > target:
                right = mid - 1
            elif nums[mid%n] < target:
                left = mid + 1
            else:
                return mid%n
            
        return -1