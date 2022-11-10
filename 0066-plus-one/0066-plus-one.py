class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        right = len(digits)-1
        
        while right > -1:
            if digits[right] != 9:
                break
            
            digits[right] = 0
            right -= 1
            
        if right > -1:
            digits[right] += 1
        else:
            digits = [1]+digits
            
        return digits
                