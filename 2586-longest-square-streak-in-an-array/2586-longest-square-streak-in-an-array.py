class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        h = defaultdict(int)

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] ** 2 in h:
                h[nums[i]] = h[nums[i] ** 2] + 1
            else:
                h[nums[i]] = 1
        
        res = max(h.values())

        return res if res != 1 else -1