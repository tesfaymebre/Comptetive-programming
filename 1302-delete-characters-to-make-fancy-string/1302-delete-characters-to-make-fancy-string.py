class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for c in s:
            if (len(stack) <= 1) or (len(stack) > 1 and (stack[-1] != c or stack[-2] != c)):
                stack.append(c)
        
        return "".join(stack)