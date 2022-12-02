class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        def helper(idx,weight):
            if (idx,weight) not in memo:
                if idx >= len(stones):
                    if weight >= 0:
                        return weight
                    else:
                        return float('inf')

                memo[(idx,weight)]= min(helper(idx+1,weight + stones[idx]),helper(idx+1,weight-stones[idx]))
                
            return memo[(idx,weight)]
        
        memo = {}
        
        return helper(0,0)