class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count_T = 0
        count_F = 0
        
        maxx = 0
        left = 0
        for right in range(len(answerKey)):
            if answerKey[right] == 'T':
                count_T += 1
            else:
                count_F += 1
                
            while count_T > k and count_F > k:
                if answerKey[left] == 'T':
                    count_T -= 1
                else:
                    count_F -= 1
                    
                left += 1
                
            maxx = max(maxx,right - left + 1)
            
        return maxx