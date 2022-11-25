class Solution:
    def arrangeCoins(self, n: int) -> int:
        curr = 0
        
        for i in range(n+1):
            curr += i
            
            if curr > n:
                return i-1
            
            if curr == n:
                return i
            
        