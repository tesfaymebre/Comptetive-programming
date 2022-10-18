class Solution:
    def freq(self,digits):
        frequency = []
        
        left = 0
        right = 0
        while right < len(digits):
            if digits[left] != digits[right]:
                frequency.append([str(right-left),digits[left]])
                left = right
            right += 1
            
        frequency.append([str(right-left),digits[left]])
        
        return frequency
    
    def say(self,frequency_pair):
        new_integer = ''
        for pair in frequency_pair:
            new_integer += ''.join(pair)
        
        return new_integer
    
    def countAndSay(self, n: int) -> str:
        digits = '1'
        for i in range(n-1):
            frequency_pair = self.freq(digits)
            digits = self.say(frequency_pair)
            
        return digits