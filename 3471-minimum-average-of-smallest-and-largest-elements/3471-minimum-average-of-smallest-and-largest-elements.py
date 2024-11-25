class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        mini = float('inf')

        for i in range(len(nums)//2):
            mini = min(mini, (nums[i] + nums[-(i+1)]) / 2 )

        return mini