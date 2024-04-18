class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j,visited):
            visited.add((i,j))
            
            perimeter = 0
            for x,y in DIR:
                r,c = i+x, j+y
                
                if not in_bound(r,c) or grid[r][c] == 0:
                    perimeter += 1
                elif (r,c) not in visited:
                    perimeter += dfs(r, c,visited)
                    
            return perimeter
                
        r,c = len(grid),len(grid[0])
        in_bound = lambda i,j: 0 <= i < r and 0 <= j < c
        DIR = [[0,1],[1,0],[-1,0],[0,-1]]
        
        visited = set()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    return dfs(i,j,visited)
                    
        return -1