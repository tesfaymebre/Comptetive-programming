class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros = 0
        steps = 0

        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                zeros += 1
            else:
                steps += zeros

        return steps