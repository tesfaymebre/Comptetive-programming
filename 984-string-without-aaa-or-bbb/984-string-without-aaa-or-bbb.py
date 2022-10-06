class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        maxx = [max(a,b), 'a' if max(a,b) == a else 'b']
        minn = [min(a,b), 'b' if min(a,b) == b else 'a']
        ans = ""
        
        while maxx[0] - minn[0] >= 2 and minn[0] > 0:
            ans += maxx[1]*2
            maxx[0] -= 2
            ans += minn[1]
            minn[0] -= 1
            
        while maxx[0] > 0 and minn[0] > 0:
            ans += maxx[1] + minn[1]
            maxx[0] -= 1
            minn[0] -= 1
            
        if maxx[0] > 0:
            ans += maxx[1] * maxx[0]
            
        return ans