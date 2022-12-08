class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #space optimized bottom up dp solution
        
        size = len(piles)
        dp = [0]*(size+1)
        
        for i in range(size-1,-1,-1):
            for j in range(i,size):
                dp[j] = max(piles[i]-dp[j],piles[j]-dp[j-1])
                
        return dp[size-1]
    
        #time complexity: O(n^2)
        #space complexity: O(n)
        
        """
        #bottom up dp solution
        
        size = len(piles)
        dp = [[0]*(size+1) for _ in range(size+1)]
        
        for i in range(size-1,-1,-1):
            for j in range(i,size):
                dp[i][j] = max(piles[i]-dp[i+1][j],piles[j]-dp[i][j-1])
                
        return dp[0][size-1]
        
        #time complexity: O(n^2)
        #space complexity: O(n^2)
        """
    
        """
        #top down dp solution
        
        def dp(i,j):
            if (i,j) not in memo:
                if i >= j:
                    return 0

                curr_score = max(piles[i]-dp(i+1,j),piles[j]-dp(i,j-1))
                memo[(i,j)] = curr_score
                
            return memo[(i,j)]
        
        memo = {}
        Alice_score = dp(0,len(piles)-1)
        
        return True if Alice_score > 0 else False
        
        #time complexity: O(n^2)
        #space complexity: O(n^2)
        """