class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def checker(mid):
            count = 0

            for num in nums:
                count += ceil(num / mid) - 1

            return count <= maxOperations

        left = 1
        right = max(nums)
        best = right

        while left <= right:
            mid = left + (right - left) // 2

            if checker(mid):
                right = mid - 1
                best = mid
            else:
                left = mid + 1

        return best
