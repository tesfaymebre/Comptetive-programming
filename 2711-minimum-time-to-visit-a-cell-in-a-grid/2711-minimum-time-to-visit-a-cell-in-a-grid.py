class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        DIR = [[0,1],[1,0],[0,-1],[-1,0]]
        inbound = lambda r,c: -1 < r < rows and -1 < c < cols

        heap = [(0,0,0)]
        visited = set()
        visited.add((0,0))

        while heap:
            curr_time,r,c = heapq.heappop(heap)

            if (r,c) == (rows - 1, cols - 1):
                    return curr_time

            for x,y in DIR:
                nr = r + x
                nc = c + y

                if inbound(nr,nc) and (nr,nc) not in visited:
                    if (grid[nr][nc] - curr_time) & 1:
                        new_time = max(curr_time + 1, grid[nr][nc])
                        heapq.heappush(heap,(new_time,nr,nc))
                    else:
                        new_time = max(curr_time + 1, grid[nr][nc] + 1)
                        heapq.heappush(heap,(new_time,nr,nc))
                
                visited.add((nr,nc))       
