class DSU:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [1]*size
        
    def find(self,pc):
        if self.parent[pc] != pc:
            self.parent[pc] = self.find(self.parent[pc])
            
        return self.parent[pc]
    
    def union(self,x,y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        
        if parent_x == parent_y:
            return 0
        
        if self.rank[parent_x] < self.rank[parent_y]:
            parent_x,parent_y = parent_y,parent_x
            
        self.parent[parent_y] = parent_x
        self.rank[parent_x] += self.rank[parent_y]
        return 1
        
        
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        union_find = DSU(n)
        connected = 0
        
        for a,b in connections:
            connected += union_find.union(a,b)
        
        ans = n-1 - connected
        return ans if len(connections) >= n-1 else -1
        