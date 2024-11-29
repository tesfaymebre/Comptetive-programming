class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        time = dict()
        time[(0,0)] = 0

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        DIR = [[0,1],[1,0],[0,-1],[-1,0]]
        inbound = lambda r,c: -1 < r < len(grid) and -1 < c < len(grid[0])

        heap = [(0,0,0)]

        while heap:
            curr_time,r,c = heapq.heappop(heap)

            for x,y in DIR:
                nr = r + x
                nc = c + y
                new_time = curr_time + 1
                if inbound(nr,nc):
                    if (nr,nc) not in time:
                        if new_time >= grid[nr][nc]:
                            heapq.heappush(heap,(new_time, nr, nc))
                            time[(nr,nc)] = new_time
                        elif (grid[nr][nc] - time[(r,c)]) & 1:
                            heapq.heappush(heap,(grid[nr][nc],nr,nc))
                            time[(nr,nc)] = grid[nr][nc]
                        else:
                            heapq.heappush(heap,(grid[nr][nc]+1,nr,nc))
                            time[(nr,nc)] = grid[nr][nc] + 1
                    else:
                        if new_time >= grid[nr][nc]:
                            if new_time < time[(nr,nc)]:
                                heapq.heappush(heap,(new_time, nr, nc))
                                time[(nr,nc)] = new_time
                        elif (grid[nr][nc] - time[(r,c)]) & 1:
                            new_time = grid[nr][nc]
                            if new_time < time[(nr,nc)]:
                                heapq.heappush(heap,(new_time,nr,nc))
                                time[(nr,nc)] = new_time
                        else:
                            new_time = grid[nr][nc] + 1
                            if new_time < time[(nr,nc)]:
                                heapq.heappush(heap,(new_time,nr,nc))
                                time[(nr,nc)] = new_time

        return time[(len(grid)-1,len(grid[0])-1)]


        
