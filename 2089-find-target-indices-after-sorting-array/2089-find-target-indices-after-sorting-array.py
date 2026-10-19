class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)

        return [i for i in range(left, right)] if left != -1 else []