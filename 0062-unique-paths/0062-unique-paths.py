class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # using permutuation
        return factorial(m+n - 2) // (factorial(m-1)*factorial(n-1))

        """
        # further space optimized solution
        
        dp = [0]*(n+1)
        dp[n-1] = 1
        
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if r == m-1 and c==n-1:
                    continue
                    
                dp[c] += dp[c+1] 
                
        return dp[0]
        """
        
        """
        # space optimized solution
        
        dp = [[0]*(n+1) for _ in range(2)]
        dp[(m-1)&1][n-1] = 1
        
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if r == m-1 and c==n-1:
                    continue
                    
                dp[r&1][c] = dp[r&1][c+1] + dp[(r+1)&1][c]
                
        return dp[0&1][0]
        """
        """
        # bottom up solution
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1
        
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if r == m-1 and c==n-1:
                    continue
                    
                dp[r][c] = dp[r][c+1] + dp[r+1][c]
                
        return dp[0][0]
        """
                
        
        
        """
        # top down solution
        memo = {}
        
        def dp(r,c):
            if (r,c) not in memo:
                if r == m-1 and c == n-1:
                    return 1
                
                if r == m or c == n:
                    return 0
                
                memo[(r,c)] = dp(r,c+1) + dp(r+1,c)
                
            return memo[(r,c)]
        
        return dp(0,0)
        """
                