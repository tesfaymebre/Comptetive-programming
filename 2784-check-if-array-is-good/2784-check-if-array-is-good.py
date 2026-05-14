class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] != i + 1:
                return False

        return nums[-1] == len(nums) - 1