class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #solution 1 using bottom up dp
        
        r,c = len(text1) + 1,len(text2) + 1
        dp = [[0]*c for _ in range(r)]
        
        for i in range(1,r):
            for j in range(1,c):
                dp[i][j] = dp[i-1][j-1] + 1 if text1[i-1] == text2[j-1] else max(dp[i-1][j],dp[i][j-1])       
        return dp[-1][-1]
        
        #solution 2 using top down dp
        
#         self.memo = dict()
#         self.n1, self.n2 = len(text1), len(text2)
        
#         def recur(idx1,idx2):
#             if (idx1,idx2) in self.memo:
#                 return self.memo[(idx1,idx2)]
#             elif  idx1 >= self.n1 or idx2 >= self.n2:
#                 return 0
#             elif text1[idx1] == text2[idx2]:
#                 self.memo[(idx1,idx2)] = 1 + recur(idx1 + 1,idx2 + 1)
#                 return self.memo[(idx1,idx2)]
#             else:
#                 self.memo[(idx1,idx2)] = max(recur(idx1 + 1,idx2),recur(idx1,idx2 + 1))
#                 return self.memo[(idx1,idx2)]
        
#         return recur(0,0)