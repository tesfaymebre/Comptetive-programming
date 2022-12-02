class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #bottom up dp solution
        total = sum(stones)
        
        dp = [[weight for weight in range(total+max(stones)+1)] for _ in range(len(stones)+1)]
        
        for idx in range(len(stones)-1,-1,-1):
            for weight in range(total+1):
                dec = dp[idx+1][abs(weight - stones[idx])]
                dp[idx][abs(weight)] = min(dp[idx+1][abs(weight+stones[idx])],dec)
                
        return dp[0][0]
    
        """
        #top down dp solution
        def helper(idx,weight):
            if (idx,weight) not in memo:
                if idx >= len(stones):
                    return abs(weight)

                memo[(idx,weight)]= min(helper(idx+1,weight + stones[idx]),helper(idx+1,weight-stones[idx]))
                
            return memo[(idx,weight)]
        
        memo = {}
        
        return helper(0,0)
        """
        