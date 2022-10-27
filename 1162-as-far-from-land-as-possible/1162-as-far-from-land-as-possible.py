class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        max_distance = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        in_bound = lambda r,c: 0 <= r < n and 0 <= c < n
        
        ones = 0
        
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    grid[row][col] = -1
                    queue.append((row,col))
                    ones += 1

        while queue:
            size = len(queue)
            for i in range(size):
                row,col = queue.popleft()

                for d in directions:
                    new_r = row+d[0]
                    new_c = col+d[1]

                    if in_bound(new_r,new_c) and grid[new_r][new_c] == 0:
                        grid[new_r][new_c] = -1
                        queue.append((new_r,new_c))
                        
            max_distance += 1

        return max_distance-1 if ones > 0 and ones < n*n else -1