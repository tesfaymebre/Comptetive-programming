class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = [0]*26
        freq2 = [0]*26
        
        for c in word1:
            freq1[ord(c)%ord('a')] += 1
        
        for c in word2:
            freq2[ord(c)%ord('a')] += 1
            
        freq1.sort()
        freq2.sort()
        
        return freq1 == freq2 and set(word1) == set(word2)