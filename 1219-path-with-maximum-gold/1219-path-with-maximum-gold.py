class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        inbound = lambda r,c: -1 < r < rows and -1 < c < cols
        DIR = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def back_t(r,c, seen):
            temp = 0
            
            for x,y in DIR:
                nr = r + x
                nc = c + y
                
                if inbound(nr,nc) and (nr,nc) not in seen and grid[nr][nc] != 0:
                    seen.add((nr,nc))
                    temp = max(temp, grid[nr][nc] + back_t(nr,nc, seen))
                    seen.remove((nr,nc))
                    
            return temp
        
        max_gold = 0
        seen = set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    seen.add((r,c))
                    max_gold = max(max_gold, grid[r][c] + back_t(r,c, seen))
                    seen.remove((r,c))            
                    
        return max_gold
            