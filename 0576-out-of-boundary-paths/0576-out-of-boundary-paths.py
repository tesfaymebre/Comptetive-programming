class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        M = 10**9 + 7
        DIR = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        inbound = lambda row, col: -1 < row < m and -1 < col < n

        # Initialize a 3D DP table to store the number of paths
        dp = [[[0 for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]

        # Initialize the base case: starting position has 1 path
        # dp[startRow][startColumn][0] = 1

        for move in range(1, maxMove + 1):
            for r in range(m):
                for c in range(n):
                    paths = 0
                    for x, y in DIR:
                        nx = r + x
                        ny = c + y
                        if inbound(nx, ny):
                            paths += dp[nx][ny][move - 1]
                        else:
                            paths += 1  # Increment count for out-of-bounds moves
                            
                    dp[r][c][move] = paths % M
                    
        return dp[startRow][startColumn][maxMove] % M
        
        """
        #top down dp solution
        
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
        """
                    
                
        