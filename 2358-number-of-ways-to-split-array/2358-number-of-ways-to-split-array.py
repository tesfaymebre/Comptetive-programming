class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        count = 0

        for i in range(1,len(nums)):
            if prefix[i] >= prefix[-1] - prefix[i]:
                count += 1

        return count