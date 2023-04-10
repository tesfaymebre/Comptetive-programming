class Solution:
    def isValid(self, s: str) -> bool:
        open_close = {"(":")","{":"}","[":"]"}
        stack = []
        for x in s:
            if x in open_close:
                stack.append(open_close[x])
            elif len(stack) > 0 :
                val = stack.pop()
                if val != x:
                    return False
            else:
                return False
                   
        return len(stack) == 0
            