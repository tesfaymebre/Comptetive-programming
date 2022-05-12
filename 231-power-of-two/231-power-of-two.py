class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        binary = str(bin(n)[2:])
        return True if binary.count('1') == 1 else False