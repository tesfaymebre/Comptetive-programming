class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.area = 0
        self.count = 0
        visited = set()
        DIR = [[0,1],[1,0],[0,-1],[-1,0]]
        inbound = lambda row, col : 0 <= row < len(grid) and 0 <= col < len(grid[row])
        
        def dfs(row,col):
            if (row,col) not in visited and inbound(row,col) and grid[row][col] == 1:
                self.count += 1
                visited.add((row,col))
                    
                for direction in DIR:
                    new_row,new_col = row + direction[0] , col + direction[1]
                    dfs(new_row, new_col)
            return 
        
        for rw in range(len(grid)):
            for cl in range(len(grid[rw])):
                dfs(rw,cl)
                self.area = max(self.area, self.count)
                self.count = 0
            
        return self.area