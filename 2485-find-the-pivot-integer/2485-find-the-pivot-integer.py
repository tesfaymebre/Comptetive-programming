class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 0
        right = sum([i for i in range(1,n+1)])
        
        for j in range(1,n+1):
            right -= j
            
            if left == right:
                return j
            
            left += j
            
        return -1