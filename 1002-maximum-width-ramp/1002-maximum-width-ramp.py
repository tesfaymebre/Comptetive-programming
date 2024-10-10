class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        _max = 0
        stack = []

        for i,num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)

        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] <= nums[i]:
                _max = max(_max, i - stack[-1])
                stack.pop()

        return _max