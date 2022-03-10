class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if grid[row][col] == 0:
                return
            
            grid[row][col] = 0
            self.count += 1
            for direction in DIR:
                new_row, new_col = row + direction[0], col + direction[1]
                if in_bound(new_row,new_col):
                    print(new_row,new_col,"ss")
                    dfs(new_row,new_col)
            
        DIR = [[1,0],[0,1],[-1,0],[0,-1]]
        in_bound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[row])
        
        self.count = 0
        for i in range(len(grid[0]) - 1):
            dfs(0, i)
            dfs(len(grid) - 1, i)
            
        for j in range(len(grid)):
            dfs(j,0)
            dfs(j, len(grid[0]) - 1)
        
        ones = 0
        for k in range(len(grid)):
            for l in range(len(grid[k])):
                if grid[k][l] == 1:
                    ones += 1
        return ones
                