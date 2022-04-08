class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = dict()
        
        def dp(i,j):
            if i == len(triangle):
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            memo[(i,j)] = triangle[i][j] + min(dp(i+1,j),dp(i+1,j+1))
            return memo[(i,j)]
        
        return dp(0,0)