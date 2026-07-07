class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        sum = 0
        pow10 = 0

        while n > 0:
            temp = n % 10
            sum += temp

            if temp > 0:
                x += temp * 10 ** pow10
                pow10 += 1

            n //= 10

        return x * sum