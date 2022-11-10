class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
    
        def dp(row,col):
            if (row,col) in memo:
                return memo[(row,col)]
            
            if (row,col) in ((m-1,n),(m,n-1)):
                return 1
            
            if row >= m or col >= n:
                return float('inf')
            
            right = dp(row,col+1)
            down = dp(row+1,col)
            health = min(right,down)-dungeon[row][col]
            
            memo[(row,col)] = max(health,1)
            return memo[(row,col)]
            
        m = len(dungeon)
        n = len(dungeon[0])
        memo = {}
        
        return dp(0,0)
        
            
            