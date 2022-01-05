class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tracker = 0

        for i in range(len(nums)):
            if  nums[tracker] != nums[i]:
                nums[tracker + 1] = nums[i]
                tracker += 1

        return tracker + 1
