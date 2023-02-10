class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans_reverse = []
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                ans_reverse.append(nums[left]**2)
                left += 1
            else:
                ans_reverse.append(nums[right]**2)
                right -= 1
                
        return ans_reverse[::-1]