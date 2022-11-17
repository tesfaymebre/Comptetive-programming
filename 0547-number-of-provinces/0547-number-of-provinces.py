class DSU:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [1]*size
        
    def find(self,city):
        if self.parent[city] != city:
            self.parent[city] = self.find(self.parent[city])
            
        return self.parent[city]
    
    def union(self,city_a, city_b):
        parent_a = self.find(city_a)
        parent_b = self.find(city_b)
        
        if parent_a == parent_b:
            return 0
        
        if self.rank[parent_a] < self.rank[parent_b]:
            parent_a,parent_b = parent_b,parent_a
            
        self.parent[parent_a] = parent_b
        return 1
    
class Solution:
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        
        union_find = DSU(size)
        province = size
        
        for i in range(size):
            for j in range(size):
                if i!=j and isConnected[i][j]:
                    province -= union_find.union(i,j)
                    
        return province
        
        """
        # bfs solution
        
        def bfs(queue):
            
            while queue:
                temp = queue.popleft()
                
                if temp not in seen:
                    seen.add(temp)
                    
                    for col in range(len(isConnected)):
                        if col not in seen and isConnected[temp][col] == 1:
                            queue.append(col)
            return
            
        queue = deque()
        seen = set()
        province = 0
        
        for row in range(len(isConnected)):
            if row not in seen:
                queue.append(row)
                bfs(queue)
                province += 1
                
        return province
        """
        
        
        
        """
        # dfs solution
        
        def dfs(row):
            visited.add(row)
            
            for col in range(len(isConnected[row])):
                if col not in visited and isConnected[row][col] == 1:
                    dfs(col)
                    
            return
        
        visited = set()
        self.province = 0
        
        for row in range(len(isConnected)):
            if row not in visited:
                self.province += 1
                dfs(row)
           
        return self.province
        
        """
            