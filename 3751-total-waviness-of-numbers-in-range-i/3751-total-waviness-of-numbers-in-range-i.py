class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(num):
            s = str(num)

            return sum((a < b > c) or (a > b < c) for a, b, c in zip(s,s[1:],s[2:]))

        return sum(waviness(num) for num in range(num1, num2 + 1))