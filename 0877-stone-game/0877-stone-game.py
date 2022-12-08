class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def dp(i,j):
            if (i,j) not in memo:
                if i >= j:
                    return 0

                curr_score = max(piles[i]-dp(i+1,j),piles[j]-dp(i,j-1))
                memo[(i,j)] = curr_score
                
            return memo[(i,j)]
        
        memo = {}
        Alice_score = dp(0,len(piles)-1)
        
        return True if Alice_score > 0 else False