class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = [d for d in str(num)]
        
        for i in range(len(digits)):
            if digits[i] == '6':
                digits[i] = '9'
                return int(''.join(digits))
            
        return int(''.join(digits))