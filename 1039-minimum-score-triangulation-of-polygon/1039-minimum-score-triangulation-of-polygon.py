class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        #bottom up dp solution
        size = len(values)
        dp = [[float('inf')]*(size+1) for _ in range(size+1)]
        
        for i in range(size-1,-1,-1):
            for j in range(size):
                for k in range(i+1,j):
                    dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j]+values[i]*values[k]*values[j])
                    
                if dp[i][j] == float('inf'):
                    dp[i][j] = 0
                    
        return dp[0][size-1]
        """
        #top down dp solution
    
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                ans = float('inf')
                
                for k in range(i+1,j):
                    ans = min(ans,dp(i,k)+dp(k,j)+values[i]*values[k]*values[j])
                
                if ans == float('inf'):
                    return 0
                
                memo[(i,j)] = ans
            
            return memo[(i, j)]
        return dp(0, len(values) - 1)
        
        #time complexity: O(n^3)
        # space complexity: O(n^2)
        """