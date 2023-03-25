class DSU:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [1]*size
        
    def find(self,target):
        if self.parent[target] != target:
            self.parent[target] = self.find(self.parent[target])
            
        return self.parent[target]
    
    def union(self,x,y):
        p_x = self.find(x)
        p_y = self.find(y)
        
        if p_x == p_y:
            return
        
        if self.rank[p_x] < self.rank[p_y]:
            p_x, p_y = p_y, p_x
            
        self.parent[p_y] = p_x
        self.rank[p_x] += self.rank[p_y]
        
        return
    
    def get_parent_list(self):
        for i in range(len(self.parent)):
            self.find(i)
           
        return self.parent
    
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        union_find = DSU(n)
        
        for a,b in edges:
            union_find.union(a,b)
            
        groups = Counter(union_find.get_parent_list())
        
        cur_sum = 0
        count = 0
        
        for key,val in groups.items():
            count += cur_sum*val
            cur_sum += val
            
        return count
            
        
        
            
        
        
        