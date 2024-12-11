class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        prefix = [0] * (maxi + 2)

        for num in nums:
            prefix[max(0,num - k)] += 1
            prefix[min(maxi,num + k) + 1] -= 1

        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]

        return max(prefix)