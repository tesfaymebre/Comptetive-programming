class Solution:
    def romanToInt(self, s: str) -> int:
        valuHolder = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,

        }

        result = 0

        for i in range(len(s)):
            if i + 1 < len(s):
                if valuHolder[s[i]] < valuHolder[s[i+1]]:
                    result = result - valuHolder[s[i]]
                else:
                    result = result + valuHolder[s[i]]

            else:
                result = result + valuHolder[s[i]]

        return result