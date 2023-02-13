class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        inbound = lambda r,c: -1 < r < n and -1 < c < n
        DIR = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        
        queue = deque()
        visited = set()
        count = 0
        
        if grid[0][0] == 0:
            queue.append((0,0))
            visited.add((0,0))
            count += 1
            
        while queue:
            size = len(queue)
            
            for i in range(size):
                row,col = queue.popleft()
                
                if (row,col) == (n-1,n-1):
                    return count
                
                for x,y in DIR:
                    new_r = row + x
                    new_c = col + y
                    
                    if inbound(new_r,new_c) and (new_r,new_c) not in visited and grid[new_r][new_c] == 0:
                        queue.append((new_r,new_c))
                        visited.add((new_r,new_c))
                        
            count += 1
            
        return -1
            
        