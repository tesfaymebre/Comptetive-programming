class Solution:
    def check(self, nums: List[int]) -> bool:
        x = 0
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                x = i + 1
                break
        sorted_nums = sorted(nums)
        
        for j in range(len(nums)):
            if sorted_nums[j] != nums[(j+x)% len(nums)]:
                return False
        return True