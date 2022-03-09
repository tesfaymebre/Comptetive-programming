class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
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
        
            