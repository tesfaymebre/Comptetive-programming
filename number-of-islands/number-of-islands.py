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