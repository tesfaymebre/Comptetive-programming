class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row,col):
            if (row,col) in visited or grid[row][col] == "0":
                return 
            
            visited.add((row,col))
            for direction in DIR:
                new_row, new_col = row + direction[0], col + direction[1]
                if (new_row, new_col) not in visited and in_bound(new_row, new_col):
                    dfs(new_row, new_col)
          
            
            
        visited = set()
        DIR = [[1,0],[0,1],[-1,0],[0,-1]]
        in_bound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[row])
        
        self.count = 0
        for rw in range(len(grid)):
            for cl in range(len(grid[rw])):
                if (rw,cl) not in visited and grid[rw][cl] == "1":
                    dfs(rw,cl)
                    self.count += 1
        
        return self.count