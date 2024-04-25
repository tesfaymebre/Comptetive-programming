class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
            
        return x
    
    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        
        if parent_u != parent_v:
            if self.size[parent_u] < self.size[parent_v]:
                parent_u, parent_v = parent_v, parent_u
                
            self.size[parent_u] += self.size[parent_v]
            self.parent[parent_v] = parent_u
            
        return

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key = lambda x: x[2])
        queries = sorted((limit, p, q, idx) for idx,(p,q,limit) in enumerate(queries))
        
        union_find = DSU(n)
        
        res = [False] * len(queries)
        edge_idx = 0
        for limit,p,q,idx in queries:
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < limit:
                u,v,dist = edgeList[edge_idx]
                union_find.union(u,v)
                edge_idx += 1
            
            if union_find.find(p) == union_find.find(q):
                res[idx] = True
                
        return res