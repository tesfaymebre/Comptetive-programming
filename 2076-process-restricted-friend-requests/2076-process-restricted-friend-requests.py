class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [0]*n
    
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        
        if px == py:
            return
        
        if self.size[py] > self.size[px]:
            px,py = py,px
            
        self.parent[py] = px
        self.size[px] += self.size[py]
        return
    
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        union_find = DSU(n)
        ans = []
        for x,y in requests:
            px = union_find.find(x)
            py = union_find.find(y)
            
            group = set()
            
            for i in range(n):
                pi = union_find.find(i)
                
                if pi == px or pi == py:
                    group.add(i)
                    
            for rx,ry in restrictions:
                if rx in group and ry in group:
                    ans.append(False)
                    break
            else:
                ans.append(True)
                union_find.union(x,y)
                
        return ans
        
        
       