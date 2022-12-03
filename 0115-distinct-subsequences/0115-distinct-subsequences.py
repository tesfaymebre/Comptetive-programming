class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #bottom up dp solution
        size_s = len(s)
        size_t = len(t)
        
        dp = [[0]*size_t + [1] for _ in range(size_s+1)]
        
        for idx_s in range(size_s-1,-1,-1):
            for idx_t in range(size_t-1,-1,-1):
                count = 0
                
                if s[idx_s] == t[idx_t]:
                    count += dp[idx_s+1][idx_t+1]
                    
                count += dp[idx_s+1][idx_t]
                dp[idx_s][idx_t] = count
                
        return dp[0][0]
        
        """
        #top down dp solution
        
        def helper(idx_s, idx_t):
            if (idx_s, idx_t) not in memo:
                if idx_t == len(t):
                    return 1

                if idx_s == len(s):
                    return 0

                count = 0

                if s[idx_s] == t[idx_t]:
                    count += helper(idx_s+1, idx_t + 1)


                count += helper(idx_s+1,idx_t)

                memo[(idx_s, idx_t)] = count
                
            return memo[(idx_s, idx_t)]
        
        memo = {}
        
        return helper(0,0)
        """