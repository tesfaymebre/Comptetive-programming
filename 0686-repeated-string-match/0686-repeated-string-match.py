class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        q = ceil(len(b) / len(a))

        temp = a * q

        if b in temp:
            return q

        temp += a

        if b in temp:
            return q + 1

        return -1
        