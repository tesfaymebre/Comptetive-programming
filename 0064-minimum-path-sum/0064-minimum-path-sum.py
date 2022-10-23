class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #bottom up dp solution
       
        dp = [[grid[0][0]]*(len(grid[0])) for _ in range(len(grid))]
        
        for r in range(1,len(grid)):
            dp[r][0] = grid[r][0]+dp[r-1][0]
            
        for c in range(1,len(grid[0])):
            dp[0][c] = grid[0][c] + dp[0][c-1]
        
        for r in range(1,len(grid)):
            for c in range(1,len(grid[0])):
                dp[r][c] = grid[r][c] + min(dp[r][c-1],dp[r-1][c])
        
        return dp[-1][-1]
        
        #top down dp solution
#         in_bound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
#         memo = {}
        
#         def dp(r,c):
#             if (r,c) == (len(grid)-1, len(grid[0])-1):
#                 return grid[-1][-1]
            
#             if (r,c) in memo:
#                 return memo[(r,c)]

#             if not in_bound(r, c):
#                 return float('inf')
            
#             memo[(r,c)] = grid[r][c] + min(dp(r,c+1),dp(r+1,c))      
#             return memo[(r,c)]
        
#         return dp(0,0)