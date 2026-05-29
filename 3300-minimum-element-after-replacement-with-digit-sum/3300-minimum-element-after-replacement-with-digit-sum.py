class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sumDigit(num):
            total = 0

            while num > 0:
                total += num % 10
                num = num // 10

            return total

        mini = float('inf')

        for num in nums:
            mini = min(mini, sumDigit(num))

        return mini