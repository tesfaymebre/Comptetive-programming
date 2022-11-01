class Solution:
    def inbound(self,row,col,m,n):
        return 0 <= row < m and 0 <= col < n
    
    def dfs(self,row,col,grid):
        if not self.inbound(row,col,len(grid),len(grid[0])):
            return (0,col)
        
        curr_diagonal = grid[row][col]
        
        if curr_diagonal == 1 and col+1 < len(grid[0]) and grid[row][col+1] == 1:
            right = self.dfs(row+1,col+1,grid)
            return (1+right[0],right[1])
        elif curr_diagonal == -1 and col-1 >= 0 and grid[row][col-1] == -1:
            left = self.dfs(row+1,col-1,grid)
            return (1+left[0],left[1])
        else:
            return (0,col)
        
    def findBall(self, grid: List[List[int]]) -> List[int]:
        res = []
        
        for col in range(len(grid[0])):
            level,curr_col = self.dfs(0,col,grid)
            
            if level == len(grid):
                res.append(curr_col)
            else:
                res.append(-1)
                
        return res