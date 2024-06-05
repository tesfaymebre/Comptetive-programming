class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = Counter(words[0])
        
        for i in range(1,len(words)):
            count = Counter(words[i])
            
            for j in range(26):
                c = chr(ord('a') + j)
                freq[c]= min(freq[c],count[c])
       
        res = []
        
        for key,val in freq.items():
            if val > 0:
                for i in range(val):
                    res.append(key)
                    
        return res