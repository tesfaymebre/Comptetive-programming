class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans = [0]
        row = len(grid)
        col = len(grid[0])
        
        total = row*col
        start = None
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    start = (i,j)
                elif grid[i][j] == -1:
                    total -= 1
        
        DIR = [[0,1],[1,0],[-1,0],[0,-1]]
        inbound = lambda r,c: -1<r<row and -1<c<col
        
        def dfs(r,c,curr,visited):
            if grid[r][c] == 2 and curr == total:
                ans[0]+= 1
                return
                
            if grid[r][c] == -1 or grid[r][c] == 2:
                return
            
            for d in DIR:
                new_r = r+d[0]
                new_c = c+d[1]
                
                if inbound(new_r,new_c) and (new_r,new_c) not in visited:
                    visited.add((new_r,new_c))
                    dfs(new_r,new_c,curr+1,visited)
                    visited.remove((new_r,new_c))
                    
        visited = set()
        visited.add(start)
        dfs(start[0],start[1],1,visited)
        return ans[0]
            
            
        