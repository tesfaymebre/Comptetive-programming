class Solution:
    def reverseBits(self, n: int) -> int:
        temp =  '{:032b}'. format(n) 
        return(int(temp[::-1], 2))