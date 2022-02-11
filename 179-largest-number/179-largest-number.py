class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        nums = list(map(str,nums))
        for j in range(len(nums)):
            for i in range(len(nums)-1):
                if nums[i] + nums[i+1] < nums[i+1] + nums[i]:
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1]= temp
        return ("".join(nums))
        