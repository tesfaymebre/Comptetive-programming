class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0

        for c in s:
            if c == ')' and stack:
                stack.pop()
            elif c == ')':
                count += 1
            else:
                stack.append(c)

        return count + len(stack)