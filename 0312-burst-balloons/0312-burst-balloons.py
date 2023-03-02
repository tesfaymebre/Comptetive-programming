class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [1] + nums + [1]

        @cache
        def dfs(left, right):
            if left > right:
                return 0

            res = 0
            for ind in range(left + 1, right):
                res = max(res, arr[left] * arr[ind] * arr[right] + dfs(left, ind) + dfs(ind, right))
            return res

        return dfs(0, n + 1)