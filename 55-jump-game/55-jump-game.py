class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]
        
        for i in range(len(nums)):
            if nums[i] == 0 and jump == 0 and i!=len(nums)-1:
                return False
            jump = max(jump,nums[i])
            jump -= 1
        
        return True
                