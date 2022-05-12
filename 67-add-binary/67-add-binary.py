class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p_a, p_b = len(a) - 1, len(b) - 1
        total = ""
        carry = 0
        
        while p_a > -1 and p_b > -1:
            total += str(int(a[p_a]) ^ int(b[p_b]) ^ carry)
            carry = (int(a[p_a]) & int(b[p_b])) | ((int(a[p_a]) ^ int(b[p_b])) & carry)
            p_a -= 1
            p_b -= 1
        
        while p_a > -1:
            total += str(int(a[p_a]) ^ carry)
            carry = int(a[p_a]) & carry
            p_a -= 1
            
        while p_b > -1:
            total += str(int(b[p_b]) ^ carry)
            carry = int(b[p_b]) & carry
            p_b -= 1
        
        if carry:
            total += str(carry)
            
        return total[::-1]
        