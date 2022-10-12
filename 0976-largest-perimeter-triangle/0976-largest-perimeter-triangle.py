class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ptr = len(nums)-1
        
        while ptr >= 2:
            if nums[ptr-2] + nums[ptr-1] > nums[ptr]:
                return nums[ptr-2] + nums[ptr-1] + nums[ptr]
            
            ptr -= 1
            
        return 0