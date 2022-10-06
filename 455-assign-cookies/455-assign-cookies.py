class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        j = 0
        count = 0
        
        for i in range(len(s)):
            if j == len(g):
                return count
            
            if j < len(g) and s[i] >= g[j]:
                count += 1
                j += 1
                
        return count
        