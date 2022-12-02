class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #top down dp solution
        def helper(idx,weight):
            if (idx,weight) not in memo:
                if idx >= len(stones):
                    return abs(weight)

                memo[(idx,weight)]= min(helper(idx+1,weight + stones[idx]),helper(idx+1,weight-stones[idx]))
                
            return memo[(idx,weight)]
        
        memo = {}
        
        return helper(0,0)
        