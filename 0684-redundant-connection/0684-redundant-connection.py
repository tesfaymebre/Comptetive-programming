class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]
    
    def union(self,u,v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        
        self.parent[parent_v] = parent_u
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        dsu = DSU(n)
        
        for u,v in edges:
            if dsu.find(u) == dsu.find(v):
                return [u,v]
            
            dsu.union(u,v)
        