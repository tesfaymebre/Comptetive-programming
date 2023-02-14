class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = []
        counter = 0
        
        for c in s:
            if c == 'b':
                counter += 1
                
            b_count.append(counter)


        def dp(i):
            if i not in memo:
                if i == 0:
                    return 0 

                if s[i] == 'a':
                    memo[i] = min(dp(i-1)+1, b_count[i]) 
                else:
                    memo[i] = dp(i-1)
                    
            return memo[i]
        
        memo = {}
        
        return dp(len(s)-1) 