class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        in_bound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        memo = {}
        
        def dp(r,c):
            if (r,c) == (len(grid)-1, len(grid[0])-1):
                return grid[-1][-1]
            if (r,c) in memo:
                return memo[(r,c)]

            if not in_bound(r, c):
                return float('inf')
            
            memo[(r,c)] = grid[r][c] + min(dp(r,c+1),dp(r+1,c))      
            return memo[(r,c)]
        
        return dp(0,0)