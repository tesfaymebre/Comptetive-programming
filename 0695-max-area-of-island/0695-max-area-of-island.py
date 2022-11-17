class DSU:
    def __init__(self,grid):
        self.parent = {}
        self.size = {}
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.parent[(i,j)] = (i,j)
                    self.size[(i,j)] = 1
                    
    def find(self,cell):
        if self.parent[cell] != cell:
            self.parent[cell] = self.find(self.parent[cell])
            
        return self.parent[cell]
    
    def union(self,a,b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            return 0
        
        if self.size[root_a] < self.size[root_b]:
            root_a,root_b = root_b,root_a
            
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        
        return self.size[root_a]
    
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #union find solution
        union_find = DSU(grid)
        
        inbound = lambda r,c: -1<r<len(grid) and -1<c<len(grid[0])
        DIR = [[0,1],[1,0],[0,-1],[-1,0]]
        
        max_area = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    curr_area = 1
                    
                    for x,y in DIR:
                        new_r = r+x
                        new_c = c+y
                        
                        if inbound(new_r,new_c) and grid[new_r][new_c] == 1:
                            curr_area = union_find.union((r,c),(new_r,new_c))
                        
                        max_area = max(max_area,curr_area)
                            
        return max_area
                            
        """
        # dfs solution
        
        def dfs(row,col):
            if (row,col) not in visited and inbound(row,col) and grid[row][col] == 1:
                # self.count += 1
                visited.add((row,col))
                    
                return 1 + dfs(row, col + 1) + dfs(row + 1, col) \
                         +  dfs(row, col - 1) + dfs(row - 1, col)
            return 0 
        
        self.area = 0
        visited = set()
        inbound = lambda row, col : 0 <= row < len(grid) and 0 <= col < len(grid[row])
        
        for rw in range(len(grid)):
            for cl in range(len(grid[rw])):
                self.area = max(self.area, dfs(rw,cl))
            
        return self.area
        """