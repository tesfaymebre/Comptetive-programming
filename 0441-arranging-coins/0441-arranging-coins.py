class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        best = 1

        while left <= right:
            mid = left + (right - left) // 2
            coins = mid * (mid + 1) // 2

            if coins > n:
                right = mid - 1
            else:
                best = mid
                left = mid + 1

        return best