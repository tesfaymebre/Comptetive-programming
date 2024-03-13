class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 0
        right = n * (n + 1) // 2
        
        for j in range(1,n+1):
            right -= j
            
            if left == right:
                return j
            
            left += j
            
        return -1