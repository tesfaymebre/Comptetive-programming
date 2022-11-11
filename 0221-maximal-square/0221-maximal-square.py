class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #space optimized bottom up dp solution
        row = len(matrix)
        col = len(matrix[0])
        
        dp = [[0]*(col+1) for _ in range(2)]
        max_length = 0
        
        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                if matrix[r][c] == '1':
                    dp[r&1][c] = min(dp[r&1][c+1],dp[(r+1)&1][c],dp[(r+1)&1][c+1]) + 1
                else:
                    dp[r&1][c] = 0
                    
                max_length = max(max_length,dp[r&1][c])
                    
        return max_length**2
    
        """
        #bottom up dp solution
        row = len(matrix)
        col = len(matrix[0])
        
        dp = [[0]*(col+1) for _ in range(row+1)]
        max_length = 0
        
        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                if matrix[r][c] == '1':
                    dp[r][c] = min(dp[r][c+1],dp[r+1][c],dp[r+1][c+1]) + 1
                    max_length = max(max_length,dp[r][c])
                    
        return max_length**2
        """
        
        """
        #top down dp solution
        def dp(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            
            if inbound(r,c) and matrix[r][c] == '1':
                memo[(r,c)] = min(dp(r,c+1),dp(r+1,c),dp(r+1,c+1))+1
                return memo[(r,c)]
            
            memo[(r,c)] = 0
            return memo[(r,c)]
            
        row = len(matrix)
        col = len(matrix[0])
        
        inbound = lambda r,c: -1 < r < row and -1 < c < col
        
        max_length = 0
        memo = {}
        
        for r in range(row):
            for c in range(col):
                max_length = max(max_length,dp(r,c))
                
        return max_length**2
        """