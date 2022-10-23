class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        
        nums = list(map(str,nums))
        for i in range(1,len(nums)):
            j = i-1 
            while j >= 0 and nums[j]+nums[j+1] < nums[j+1]+nums[j]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                j -= 1
                    
        return ("".join(nums))
        