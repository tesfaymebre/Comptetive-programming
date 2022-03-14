class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIR = [[0,1],[1,0],[0,-1],[-1,0]]
        in_bound = lambda row,col: 0 <= row < len(grid) and 0 <= col < len(grid[row])
        queue = deque()
        visited = set()
        time = 0
        fresh = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visited.add((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        while queue and fresh:
            n = len(queue)
            time += 1
            
            for k in range(n):
                curr = queue.popleft()
                for direction in DIR:
                    new_row, new_col = curr[0] + direction[0], curr[1] + direction[1] 
                    if (new_row,new_col) not in visited and in_bound(new_row,new_col) and \
                        grid[new_row][new_col] == 1:
                        queue.append((new_row,new_col))
                        visited.add((new_row, new_col)) 
                        fresh -= 1
        if fresh:
            return -1
        return time
                   
        
        