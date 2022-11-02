class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        complement = 0
        shift_count = 0
        
        while n:
            if n&1 == 0:
                complement |= 1<<shift_count
            
            n = n >> 1
            shift_count += 1
            
        return complement