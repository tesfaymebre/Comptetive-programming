class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for idx,c in enumerate(s):
            temp = ''
            while stack and stack[-1] == c:
                temp = stack.pop()
                
            if temp != c:
                stack.append(c)
                
        return ''.join(stack)