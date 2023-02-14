class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n = sorted(str(n))
        
        for i in range(32):
            num = 1 << i
            
            if n == sorted(str(num)):
                return True
            
        return False