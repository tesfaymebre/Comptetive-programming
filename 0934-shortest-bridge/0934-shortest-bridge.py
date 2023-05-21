class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        DIR = [[0,1],[1,0],[-1,0],[0,-1]]
        inbound = lambda r,c: -1 < r < rows and -1 < c < cols
        seen = set()
        
        def find(rows,cols):
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        queue.append((i,j))
                        seen.add((i,j))
                        dfs(i,j)
                        return
        
        def dfs(r,c):
            for x,y in DIR:
                nr = r + x
                nc = c + y
                
                if inbound(nr,nc) and (nr,nc) not in seen and grid[nr][nc]:
                    queue.append((nr,nc))
                    seen.add((nr,nc))
                    dfs(nr,nc)
            
        queue = deque()
        find(rows,cols)
        
        level = 0
        while queue:
            size = len(queue)
            
            for _ in range(size):
                r,c = queue.popleft()
                
                for x,y in DIR:
                    nr = r + x
                    nc = c + y
                    
                    if inbound(nr,nc) and (nr,nc) not in seen:
                        if grid[nr][nc]:
                            return level
                    
                        if grid[nr][nc] == 0:
                            queue.append((nr,nc))
                            seen.add((nr,nc))
                        
            level += 1
            
        return level