class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        arr = [0]*(n+1)
        arr[1] = 1
        i = 1
        
        while 2*i <= n:
            arr[2*i] = arr[i]
            
            if 2 * i + 1 <= n:
                arr[2*i+1] = arr[i] + arr[i+1]
                
            i += 1
                
        return max(arr)
        