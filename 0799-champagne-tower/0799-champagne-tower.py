class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (query_row + 2) for _ in range(2)]
        dp[0][0] = poured
        
        lengthRow = query_row + 2
        for row in range(lengthRow):
            lengthCol = row+1
            
            if row + 1 < lengthRow:
                 dp[(row + 1)&1][0] = 0
                
            for col in range(lengthCol):
                if row + 1 < lengthRow:
                    if dp[row&1][col] >= 1:
                        flow = dp[row&1][col] - 1
                        dp[row&1][col] -= flow
                        dp[(row + 1)&1][col] += flow/2
                        if col + 1 < row+2:
                            dp[(row+1)&1][col+1] = flow/2
                            
                    elif col + 1 < row+2:
                        dp[(row+1)&1][col+1] = 0
                            
            if row == query_row:
                return dp[row&1][query_glass]
    
  