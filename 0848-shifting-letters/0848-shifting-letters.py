class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        result = ['']*len(s)
        cur_sum = 0
        
        for i in range(len(shifts)-1,-1,-1):
            cur_sum += shifts[i]
            result[i] = chr((ord(s[i]) - ord('a') + cur_sum)%26 + ord('a'))
         
        return ''.join(result)