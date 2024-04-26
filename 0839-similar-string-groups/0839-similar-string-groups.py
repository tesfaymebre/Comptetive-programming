class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
            
        return x
    
    def union(self,u,v):
        p_u = self.find(u)
        p_v = self.find(v)
        
        if p_u != p_v:
            if self.size[p_u] < self.size[p_v]:
                p_u, p_v = p_v, p_u
                
            self.size[p_u] += self.size[p_v]
            self.parent[p_v] = p_u
        
        return
    
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        dsu = DSU(len(strs))
        
        for i in range(len(strs)):
            for j in range(len(strs)):
                word = strs[j]
                count = 0
                for c in range(len(word)):
                    if strs[i][c] != word[c]:
                        count += 1

                if count == 2 or count == 0:
                    dsu.union(i,j)
        
        for i in range(len(strs)):
            dsu.find(i)
            
        return len(set(dsu.parent))