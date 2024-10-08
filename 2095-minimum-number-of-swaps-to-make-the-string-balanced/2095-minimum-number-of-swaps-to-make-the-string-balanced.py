class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        stack = []

        for b in s:
            if b == '[':
                stack.append(b)
            elif stack:
                stack.pop()
            else:
                count += 1

        return ceil(count/2)
            
        