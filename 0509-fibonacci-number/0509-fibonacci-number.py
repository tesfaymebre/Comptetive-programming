class Solution:
    def fib(self, n: int) -> int:
        #bottom up dp space optimized solution 1
        prev = 1
        prev2 = 0
        
        for i in range(1,n+1):
            curr = prev+prev2
            prev2 = prev
            prev = curr
            
        return prev2
    
    
        #bottom up dp solution 2
#         dp = [0]*(n+1)
#         dp[1] = 1
        
#         for i in range(2,n+1):
#             dp[i] = dp[i-2]+dp[i-1]
            
#         return dp[n]
        
    
    
        #top down dp solution 3
#         memo = {0: 0, 1: 1}
        
#         def dp(n):
#             if n in memo:
#                 return memo[n]
            
#             memo[n] = dp(n-1) + dp(n-2)
#             return memo[n]
        
#         return dp(n)
    
    