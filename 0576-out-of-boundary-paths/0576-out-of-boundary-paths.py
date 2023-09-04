class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        M = 10**9 + 7
        DIR = [[0,1],[1,0],[-1,0],[0,-1]]
        inbound = lambda row,col: -1 < row < m and -1 < col < n
        memo = {}
        
        def dp(r,c,maxMove):
            if (r,c,maxMove) not in memo:
                if not inbound(r,c):
                        return 1
                
                if maxMove == 0:
                    return 0
                
                paths = 0
                
                for x,y in DIR:
                    nx = r+x
                    ny = c+y
                    paths += dp(nx,ny,maxMove-1)
                    
                memo[(r,c,maxMove)] = paths % M
                
            return memo[(r,c,maxMove)]
        
        return dp(startRow,startColumn,maxMove)
                    
                
        