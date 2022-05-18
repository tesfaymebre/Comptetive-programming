class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0]*n for i in range(m)]
        in_bound = lambda r,c : 0 <= r < m and 0 <= c < n
        
        for i in range(m):
            for j in range(n):
                if not in_bound(i-1,j) or not in_bound(i,j-1):
                    paths[i][j] = 1
                    
                else:
                    paths[i][j] += paths[i][j-1] + paths[i-1][j]
                    
        return paths[-1][-1]