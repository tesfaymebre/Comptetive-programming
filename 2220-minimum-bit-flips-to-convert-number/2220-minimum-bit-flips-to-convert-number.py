class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = bin(start ^ goal)[2:]
        return xor.count("1")
       