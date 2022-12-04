class Solution:
    def minCut(self, s: str) -> int:
        #bottom up dp solution
        size = len(s)
        
        dp = [float('inf')]*(size)+[0]
        
        for left in range(size-1,-1,-1):
            count = float('inf')
            
            for right in range(left,size):
                if s[left:right+1] == s[left:right+1][::-1]:
                    count = min(count,1+dp[right+1])
                    
            dp[left] = count
            
        return dp[0]-1
        
        """
        #top down dp
        def helper(left):
            if left not in memo:
                if left == len(s):
                    return 0

                count = float('inf')

                for right in range(left,len(s)):

                    if s[left:right+1] == s[left:right+1][::-1]:
                        count = min(count,1 + helper(right+1))

                memo[left] = count
                
            return memo[left]
        
        memo = {}
        
        return helper(0) - 1
        
        """
                    
                