class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
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
            