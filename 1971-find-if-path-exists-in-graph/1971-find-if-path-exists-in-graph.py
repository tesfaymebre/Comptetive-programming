class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
        
    def find(self,x):
        if self.parent[x] == x:
            return x
        
        self.parent[x] = self.find(self.parent[x])
         
        return self.parent[x]
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1
            
        return
    
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        union_find = DSU(n)
        
        for u,v in edges:
            union_find.union(u,v)
        
        if union_find.find(source) == union_find.find(destination):
            return True
        
        return False