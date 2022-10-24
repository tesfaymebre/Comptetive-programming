class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def dp(pos):
            if pos == n:
                return 1
            elif pos > n:
                return 0
            
            if pos in memo:
                return memo[pos
                           ]
            memo[pos] = dp(pos+1) + dp(pos+2)
            return memo[pos]
        
        return dp(0)