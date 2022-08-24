class Solution:
    def minSteps(self, n: int) -> int:
        memo = [i for i in range(n+1)]
        memo[1] = 0
        
        
        for j in range(2, n//2 +1):
            k = 2
            temp = memo[j] + 2
            memo[j*k] = min(memo[j*k],temp)
            k += 1
            
            while k*j <= n:
                temp += 1
                memo[j*k] = min(memo[j*k],temp)
                k += 1
                
        return memo[n]