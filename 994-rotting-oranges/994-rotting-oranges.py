class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIR = [[0,1],[1,0],[0,-1],[-1,0]]
        in_bound = lambda row,col: 0 <= row < len(grid) and 0 <= col < len(grid[row])
        queue = deque()
        timer = 0
        fresh = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
                    
        while queue and fresh:
            n = len(queue)
            timer += 1
            
            for k in range(n):
                curr = queue.popleft()
                for direction in DIR:
                    new_row, new_col = curr[0] + direction[0], curr[1] + direction[1] 
                    if in_bound(new_row,new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row,new_col)) 
                        fresh -= 1
                        
        return timer if not fresh else -1
                   
        
        