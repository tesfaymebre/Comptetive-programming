class Solution:
    def findComplement(self, num: int) -> int:
        #solution 2 with out using strig
        complement = 0
        shift_count = 0
        
        while num:
            if num&1 == 0:
                complement |= 1<<shift_count
            
            num = num >> 1
            shift_count += 1
            
        return complement
        """
        #solution 1
        complement = ""
        
        while num:
            temp = num&1
            num = num>>1
            
            if temp:
                complement = '0'+complement
            else:
                complement = '1'+complement
                
        return int(complement,2)
        """