class Solution:
    def climbStairs(self, n: int) -> int:
       
    #top down dp solution
        memo = {}
        
        def dp(pos):
            if pos == 1:
                return 1
            elif pos == 2:
                return 2
            
            if pos in memo:
                return memo[pos]
            
            memo[pos] = dp(pos-1) + dp(pos-2)
            return memo[pos]
        
        return dp(n)
    