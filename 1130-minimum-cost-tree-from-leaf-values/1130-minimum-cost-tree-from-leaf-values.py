class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        def dp(i,j):
            if (i,j) not in memo:
                
                if j-i+1 == 2:
                    return arr[i]*arr[j]
                elif j-i+1 < 2:
                    return 0
                
                ans = float('inf')
                
                for k in range(i+1,j):
                    left = dp(i,k)+dp(k+1,j)+max(arr[i:k+1])*max(arr[k+1:j+1])
                    right = dp(i,k-1)+dp(k,j)+max(arr[i:k])*max(arr[k:j+1])
                    ans = min(ans,left,right)
                    
                memo[(i,j)] = ans
                
            return memo[(i,j)]
        
        memo = {}
        
        return dp(0,len(arr)-1)