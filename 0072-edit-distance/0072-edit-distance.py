class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
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