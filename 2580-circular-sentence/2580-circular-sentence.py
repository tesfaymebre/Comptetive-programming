class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        
        for i in range(1,len(words)):
            if words[i-1][-1] != words[i][0]:
                return False
            
        return True if words[-1][-1] == words[0][0] else False