class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #solution 1
        memo = {}
        
        def dp(m,n,r,c):
            if r == 0 or c == 0:
                memo[(r,c)] = 1
                return memo[(r,c)]
            elif (r,c) in memo:
                return memo[r,c]
            else:
                memo[(r,c)] = dp(m,n,r-1,c) + dp(m,n,r,c-1)
                return memo[(r,c)]
        
        return dp(m,n,m-1,n-1)
    
        #solution 2
        
#         paths = [[0]*n for i in range(m)]
#         in_bound = lambda r,c : 0 <= r < m and 0 <= c < n
        
#         for i in range(m):
#             for j in range(n):
#                 if not in_bound(i-1,j) or not in_bound(i,j-1):
#                     paths[i][j] = 1
                    
#                 else:
#                     paths[i][j] += paths[i][j-1] + paths[i-1][j]
                    
#         return paths[-1][-1]