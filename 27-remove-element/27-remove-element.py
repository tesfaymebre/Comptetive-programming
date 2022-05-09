class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = len(nums) - 1
        k = 0
        
        while p1 < p2:
            if nums[p1] == val:
                while p2 > p1 and nums[p2] == val:
                    p2 -= 1
                
                nums[p1],nums[p2] = nums[p2],nums[p1]
            
            p1 += 1
        
        return nums.index(val) if val in nums else len(nums)
        