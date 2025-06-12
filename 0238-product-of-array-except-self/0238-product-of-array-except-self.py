class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]

        for i in range(len(nums)-1):
            prefix.append(prefix[-1] * nums[i])

        postfix = 1

        for j in range(len(nums)-1,-1,-1):
            prefix[j] = prefix[j] * postfix
            postfix *= nums[j]

        return prefix