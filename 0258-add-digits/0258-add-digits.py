class Solution:
    def addDigits(self, num: int) -> int:
        # solution 2
        if num == 0:
            return 0
        
        if num % 9 == 0:
            return 9
        
        return num % 9
        
        """
        # solution 1
        digital_root = 0
        while num > 0:
            digital_root += num % 10
            num = num // 10
            
            if num == 0 and digital_root > 9:
                num = digital_root
                digital_root = 0
                
        return digital_root
        """