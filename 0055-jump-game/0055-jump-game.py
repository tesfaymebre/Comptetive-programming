class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]
        
        for i in range(len(nums)-1):
            jump = max(jump,nums[i])
            
            if jump == 0:
                return False
            
            jump -= 1
        
        return True
                