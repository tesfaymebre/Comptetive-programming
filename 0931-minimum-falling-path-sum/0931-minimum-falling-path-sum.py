class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        def dp(r,c):
            if (r,c) not in memo:
                if r == row:
                    return 0

                if c < 0 or c >= col:
                    return float('inf')

                memo[(r,c)] = matrix[r][c] + min(dp(r+1,c-1),dp(r+1,c),dp(r+1,c+1))
            
            return memo[(r,c)]
        
        row = len(matrix)
        col = len(matrix[0])
        memo = {}
        
        min_sum = float('inf')
        
        for c in range(len(matrix)):
            min_sum = min(min_sum,dp(0,c))
            
        return min_sum
        