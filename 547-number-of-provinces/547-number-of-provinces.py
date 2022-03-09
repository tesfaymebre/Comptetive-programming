class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(row):
            visited.add(row)
            
            for col in range(len(isConnected[row])):
                if col in visited or isConnected[row][col] == 0:
                    continue
                    
                dfs(col)
            return
        
        visited = set()
        self.province = 0
        
        for row in range(len(isConnected)):
            if row not in visited:
                self.province += 1
                dfs(row)
           
        return self.province
        
            