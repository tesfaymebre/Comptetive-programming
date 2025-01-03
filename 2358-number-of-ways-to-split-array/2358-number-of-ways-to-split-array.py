class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        count = 0

        for i in range(len(nums)-1):
            left_sum += nums[i]

            if left_sum >= total - left_sum:
                count += 1

        return count
    """
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        count = 0

        for i in range(1,len(nums)):
            if prefix[i] >= prefix[-1] - prefix[i]:
                count += 1

        return count
    """