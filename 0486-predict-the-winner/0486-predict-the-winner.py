class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        #space optimized bottom up dp solution
        
        size = len(nums)
        dp = [[0]*(size+1) for _ in range(2)]
        
        
        dp[0][0] = nums[0]
            
        for i in range(size-1,-1,-1):
            dp[i&1][i&1] = nums[i]
            
            for j in range(i,size):
                dp[i&1][j] = max(nums[i]-dp[(i+1)&1][j],nums[j]-dp[i&1][j-1])
                
        return True if dp[0][size-1] >= 0 else False
    
        #time complexity: O(n^2)
        #space complexity: O(2n) = O(n)
    
        """
        #bottom up dp solution
        
        size = len(nums)
        dp = [[0]*(size+1) for _ in range(size+1)]
        
        for i in range(size):
            dp[i][i] = nums[i]
            
        for i in range(size-1,-1,-1):
            for j in range(i,size):
                dp[i][j] = max(nums[i]-dp[i+1][j],nums[j]-dp[i][j-1])
                
        return True if dp[0][size-1] >= 0 else False
        
        #time complexity: O(n^2)
        #space complexity: O(n^2)
        """
    
        """
        #top down dp solution
        
        def dp(i,j):
            if (i,j) not in memo:
                if i == j:
                    return nums[i]

                curr_score = max(nums[i] - dp(i+1,j),nums[j] - dp(i,j-1))
                memo[(i,j)] = curr_score
                
            return memo[(i,j)]
        
        memo = {}
        player_1_score = dp(0,len(nums)-1)
        
        return True if player_1_score >= 0 else False
        
        #time complexity: O(n^2)
        #space complexity: O(n^2)
        """
        
        