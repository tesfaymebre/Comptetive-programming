class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        exponent = abs(n)

        result = 1

        while exponent > 0:
            if exponent & 1:
                result *= x

            x *= x
            exponent >>= 1

        return result if n > 0 else 1 / result

        