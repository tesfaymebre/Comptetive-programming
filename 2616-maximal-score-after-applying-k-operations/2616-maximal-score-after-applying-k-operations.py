class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        score = 0

        while k:
            temp = -nums[0]
            score += temp
            k -= 1
            heapq.heapreplace(nums,- ceil(temp/3))

        return score