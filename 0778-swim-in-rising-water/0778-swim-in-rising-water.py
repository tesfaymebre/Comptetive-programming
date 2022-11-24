class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        DIR = [[0,1],[1,0],[0,-1],[-1,0]]
        inbound = lambda r,c: -1 < r < row and -1 < c < col
        
        heap = [[grid[0][0],0,0]]
        visited = set([(0,0)])
        
        t = grid[0][0]
        
        while heap:
            depth,r,c = heapq.heappop(heap)
            t = max(t,depth)
            
            if r == row-1 and c == col-1:
                return t
            
            for x,y in DIR:
                nr = r+x
                nc = c+y
                
                if inbound(nr,nc) and (nr,nc) not in visited:
                    heapq.heappush(heap,[grid[nr][nc],nr,nc])
                    visited.add((nr,nc))
                    
        return t
                    
                
        