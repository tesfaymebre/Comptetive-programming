class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # solution 2 bottom up dp approach
        n = len(nums)
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for i in range(n):
            dp[i][i] = nums[i]
            
        for i in range(n-1, -1, -1):
            for j in range(i+1,n):
                dp[i][j] = max(nums[i] - dp[i+1][j],nums[j] - dp[i][j-1])
        
        return True if dp[0][n-1] >= 0 else False
                
        """
        # solution 1 top down dp approach
        memo = {}
        
        def dp(i,j):
            if (i,j) not in memo:
                if i == j:
                    return nums[i]

                memo[(i,j)] = max(nums[i] - dp(i+1,j),nums[j] - dp(i,j-1))
                
            return memo[(i,j)]
        
        player_1_score = dp(0,len(nums)-1)
        
        return True if player_1_score >= 0 else False
        """
        
        