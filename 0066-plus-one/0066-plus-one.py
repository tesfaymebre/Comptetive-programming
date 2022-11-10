class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        hold = 0
        
        if digits[-1] + 1 > 9:
            digits[-1] = 0
            hold = 1
        else:
            digits[-1] += 1
            
        right = len(digits)-2
        
        while hold and right > -1:
            if digits[right]+hold > 9:
                digits[right] = 0
            else:
                digits[right] = digits[right]+hold
                hold = 0
                
            right -= 1
            
        if hold:
            digits = [1]+digits
            
        return digits