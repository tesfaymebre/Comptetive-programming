class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')]*n
        
        for i in range(1,n+1):
            dp[i] = min(dp[i-j*j] for j in range(1,floor(sqrt(i))+1)) + 1
            
        return dp[n]