class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
#         dp = []
#         for index in range(query_row+2):
#             temp = []
#             for j in range(index+1):
#                 temp.append(0)

#             dp.append(temp)

#         dp[0][0] = poured

        dp = [[0] * (query_row + 2) for _ in range(query_row + 2)]
        dp[0][0] = poured
        
        lengthRow = query_row + 2
        for row in range(lengthRow):
            lengthCol = row+1
            for col in range(lengthCol):
                if row + 1 < lengthRow:
                    if dp[row][col] >= 1:
                        flow = dp[row][col] - 1
                        dp[row][col] -= flow
                        dp[row + 1][col] += flow/2
                        if col + 1 < row+2:
                            dp[row+1][col+1] += flow/2

       

        return dp[query_row][query_glass]