class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j):
            if (i,j) in self.visited:
                return
            
            self.visited.add((i,j))
                
            for x,y in DIR:
                r,c = i+x, j+y
                
                if not in_bound(r,c) or grid[r][c] == 0:
                    self.perimeter += 1
                else:
                    dfs(r, c)
                
        self.visited = set()
        self.perimeter = 0
        r,c = len(grid),len(grid[0])
        in_bound = lambda i,j: 0 <= i < r and 0 <= j < c
        DIR = [[0,1],[1,0],[-1,0],[0,-1]]
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    dfs(i,j)
                    break
                    
        return self.perimeter