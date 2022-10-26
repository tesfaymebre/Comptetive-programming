class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #bottom up dp solution
        row = len(grid)
        col = len(grid[0])
        
        dp = [[float('inf')]*(col+1) for _ in range(row+1)]
        dp[row-1][col] = 0
        dp[row][col-1] = 0
        
        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                dp[r][c] = grid[r][c] + min(dp[r][c+1],dp[r+1][c])
                
        return dp[0][0]
        
        """
        #top down dp solution
        in_bound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        memo = {}
        
        def dp(r,c):
            if not in_bound(r, c):
                return float('inf')
                
            if (r,c) == (len(grid)-1, len(grid[0])-1):
                return grid[-1][-1]
            
            if (r,c) in memo:
                return memo[(r,c)]

            memo[(r,c)] = grid[r][c] + min(dp(r,c+1),dp(r+1,c))      
            return memo[(r,c)]
        
        return dp(0,0)
        """