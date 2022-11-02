class Solution:
    def findComplement(self, num: int) -> int:
        complement = ""
        
        while num:
            temp = num&1
            num = num>>1
            
            if temp:
                complement = '0'+complement
            else:
                complement = '1'+complement
                
        return int(complement,2)