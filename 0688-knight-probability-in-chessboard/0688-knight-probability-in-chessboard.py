class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        #bottom up dp solution
        DIR = [(1, 2), (1, -2), (-1, 2), (-1, -2),(2, 1), (2, -1), (-2, 1), (-2, -1)]
        inbound = lambda row, col: -1 < row < n and -1 < col < n

        # Initialize a 3D DP table to store the number of paths
        dp = [[[0 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
        
        #base case
        for r in range(n):
            for j in range(n):
                dp[r][j][0] = 1

        for move in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    curr_probability = 0

                    for x,y in DIR:
                        nx = r+x
                        ny = c+y

                        if inbound(nx,ny):
                            curr_probability += dp[nx][ny][move-1]

                    dp[r][c][move] = curr_probability / 8
                    
        return dp[row][column][k]
        
        """
        #top down dp solution
        DIR = [(1, 2), (1, -2), (-1, 2), (-1, -2),(2, 1), (2, -1), (-2, 1), (-2, -1)]
        inbound = lambda row,col: -1 < row < n and -1 < col < n
        memo = {}

        def dp(r,c,k):
            if (r,c,k) not in memo:
                if k == 0:
                    return 1

                curr_probability = 0

                for x,y in DIR:
                    nx = r+x
                    ny = c+y

                    if inbound(nx,ny):
                        curr_probability += dp(nx,ny,k-1)

                memo[(r,c,k)] = curr_probability / 8

            return memo[(r,c,k)]

        return dp(row,column,k)
        """