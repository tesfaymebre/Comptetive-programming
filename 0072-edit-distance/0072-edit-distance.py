class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #space optimized bottom up dp soltution
        size1 = len(word1)
        size2 = len(word2)
        
        if not word1:
            return size2
        elif not word2:
            return size1
        
        dp = [[0]*(size2 + 1) for _ in range(2)]
            
        for idx1 in range(size1 - 1,-1,-1):
            for idx2 in range(size2 - 1,-1,-1):
                if idx2+1 == size2:
                    dp[idx1 & 1][-1] = size1-idx1
                
                if idx1+1 == size1:
                    dp[(idx1+1)& 1][idx2] += size2-idx2
                    
                if word1[idx1] == word2[idx2]:
                    dp[idx1&1][idx2] = dp[(idx1+1)&1][idx2+1]
                else:
                    insert = dp[(idx1)&1][idx2+1]
                    delete = dp[(idx1+1)&1][idx2]
                    replace = dp[(idx1+1)&1][idx2+1]
                    
                    dp[(idx1)&1][idx2] = 1 + min(insert,delete,replace)
                    
        return dp[0][0]
    
        """
        #bottom up dp soltution
        size1 = len(word1)
        size2 = len(word2)
        
        dp = [[0]*(size2 + 1) for _ in range(size1 + 1)]
        
        for idx1 in range(size1 + 1):
            dp[idx1][-1] += size1-idx1
            
        for idx2 in range(size2 + 1):
            dp[-1][idx2] += size2-idx2
            
        for idx1 in range(size1 - 1,-1,-1):
            for idx2 in range(size2 - 1,-1,-1):
                if word1[idx1] == word2[idx2]:
                    dp[idx1][idx2] = dp[idx1+1][idx2+1]
                else:
                    insert = dp[idx1][idx2+1]
                    delete = dp[idx1+1][idx2]
                    replace = dp[idx1+1][idx2+1]
                    
                    dp[idx1][idx2] = 1 + min(insert,delete,replace)
                    
        return dp[0][0]
        """
        
        """
        #top down dp solution
        
        size1 = len(word1)
        size2 = len(word2)
        
        def helper(idx1,idx2):
            if (idx1,idx2) not in memo:
                if idx1 == size1 or idx2 == size2:
                    return (size1-idx1) + (size2-idx2)

                if word1[idx1] == word2[idx2]:
                    memo[(idx1,idx2)] = helper(idx1+1,idx2+1)
                else:
                    insert = helper(idx1,idx2+1)
                    delete = helper(idx1+1,idx2)
                    replace = helper(idx1+1,idx2+1)
                    
                    memo[(idx1,idx2)] = 1 + min(insert,delete,replace)
                    
            return memo[(idx1,idx2)]
        
        memo = {}
        
        return helper(0,0)
        """