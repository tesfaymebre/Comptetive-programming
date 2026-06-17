class Solution:
    def processStr(self, s: str, k: int) -> str:
        size = 0
        for c in s:
            if c == "*":
                if size:
                    size -= 1
            elif c == "#":
                size *= 2
            elif c == "%":
                pass
            else:
                size += 1
        if k + 1 > size:
            return "."
       
        for c in s[::-1]:
            if c == '*':
                size += 1
            elif c == '#':
                if k + 1 > size // 2:
                    k -= size // 2

                size //= 2
            elif c == '%':
                k = size - k - 1
            else:
                if size == k + 1:
                    return c
                
                size -= 1

        return '.'