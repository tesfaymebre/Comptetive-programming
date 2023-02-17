class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        
        for idx,c in enumerate(s):
            if freq[c] == 1:
                return idx
            
        return -1