class Solution:
    def arrangeCoins(self, n: int) -> int:
        curr = 0
        
        for i in range(n+2):
            curr += i
            
            if curr > n:
                return i-1
            
        