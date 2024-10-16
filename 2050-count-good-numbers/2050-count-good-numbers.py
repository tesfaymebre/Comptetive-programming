class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        def binaryExponentiation(base, exponent):
            result = 1
            while exponent > 0:
                if exponent & 1:
                    result *= base
                    result %= mod

                base *= base
                base %= mod
                exponent >>= 1

            return result
        
        evens = ceil(n / 2)
        odds = n - evens

        return (binaryExponentiation(5,evens)  * binaryExponentiation(4,odds)) % mod