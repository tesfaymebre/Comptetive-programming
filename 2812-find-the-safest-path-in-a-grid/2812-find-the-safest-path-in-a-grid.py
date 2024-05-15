class Solution:

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        inbound = lambda r,c: -1 < r < n and -1 < c < n
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r,c))
                    grid[r][c] = 0
                else:
                    grid[r][c] = -1
                    
        while queue:
            size = len(queue)
            
            for _ in range(size):
                r,c = queue.popleft()
                
                for x,y in DIR:
                    nr = r + x
                    nc = c + y
                    
                    if inbound(nr,nc) and grid[nr][nc] == -1:
                        grid[nr][nc] = grid[r][c] + 1
                        queue.append((nr,nc))
        
        heap = [[-grid[0][0], 0, 0]]
        grid[0][0] = -1 #visited

       
        while heap:
            safeness, r, c = heapq.heappop(heap)
          
            if (r,c) == (n-1,n-1):
                return -safeness
            
            for x,y in DIR:
                nr = r + x
                nc = c + y
               
                if inbound(nr,nc) and grid[nr][nc] != -1:
                    heapq.heappush(heap, [-min(-safeness, grid[nr][nc]), nr, nc])
                    grid[nr][nc] = -1

        return -1
    
