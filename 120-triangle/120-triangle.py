class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #solution 1 using bottom-up dp approach
        dp = triangle[-1]
        
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
                
        return dp[0]
    
    
    # solution 2 using top-down dp approach
#         memo = dict()
        
#         def dp(i,j):
#             if i == len(triangle) - 1:
#                 return triangle[i][j]
            
#             if (i,j) in memo:
#                 return memo[(i,j)]
            
#             memo[(i,j)] = triangle[i][j] + min(dp(i+1,j),dp(i+1,j+1))
#             return memo[(i,j)]
        
#         return dp(0,0)