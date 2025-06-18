class DSU:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, target):
        if self.parent[target] != target:
            self.parent[target] = self.find(self.parent[target])

        return self.parent[target]

    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)

        if p_x == p_y:
            return False

        if self.rank[p_y] > self.rank[p_x]:
            p_x, p_y = p_y, p_x

        self.parent[p_y] = p_x
        self.rank[p_x] += self.rank[p_y]
        
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dsu = DSU(rows * cols)

        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        in_bound = lambda r,c: -1 < r < rows and -1 < c < cols

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1

                    for x,y in DIR:
                        nr = r + x
                        nc = c + y

                        if in_bound(nr,nc) and grid[nr][nc] == '1':
                            if dsu.union(r * cols + c, nr * cols + nc):
                                islands -= 1

        return islands

"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #1 bfs solution
        def bfs(que):
            while que:
                n = len(que)
                for j in range(n):
                    row,col = que.popleft()
                    
                    for direction in DIR:
                        new_row, new_col = row + direction[0], col + direction[1]
                        if in_bound(new_row, new_col) and grid[new_row][new_col] == '1':
                            que.append((new_row,new_col))
                            grid[new_row][new_col] = '0'
        
        DIR = [[1,0],[0,1],[-1,0],[0,-1]]
        in_bound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[row])
        self.count = 0
        que = deque()
        for rw in range(len(grid)):
            for cl in range(len(grid[rw])):
                if grid[rw][cl] == "1":
                    que.append((rw,cl))
                    grid[rw][cl] = '0'
                    bfs(que)
                    self.count += 1
                
        return self.count
                
        #2/ dfs solution
#         def dfs(row,col):
#             if grid[row][col] == "0":
#                 return 
            
#             grid[row][col] = "0"
#             for direction in DIR:
#                 new_row, new_col = row + direction[0], col + direction[1]
#                 if in_bound(new_row, new_col):
#                     dfs(new_row, new_col)
        
       
#         DIR = [[1,0],[0,1],[-1,0],[0,-1]]
#         in_bound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[row])
#         self.count = 0
#         for rw in range(len(grid)):
#             for cl in range(len(grid[rw])):
#                 if grid[rw][cl] == "1":
#                     dfs(rw,cl)
#                     self.count += 1
                    
#         return self.count
"""