class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(num):
            total = 0

            while num:
                digit = num % 10
                total += digit ** 2
                num //= 10

            return total

        visited = set()

        while n not in visited:
            visited.add(n)

            if n == 1:
                return True

            n = sumOfSquares(n)

        return False