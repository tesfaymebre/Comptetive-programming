class Solution:
    def longestPrefix(self, s: str) -> str:
        m = len(s)
        LPS = [0] * m

        i = 0
        j = 1

        while j < m:
            if s[i] == s[j]:
                LPS[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    j += 1
                else:
                    i = LPS[i-1]

        return s[:LPS[-1]]