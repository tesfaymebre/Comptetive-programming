class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        size = min(len(word1),len(word2))
        
        for i in range(size):
            ans.append(word1[i])
            ans.append(word2[i])
            
        if len(word1) > len(word2):
            ans.append(word1[size:])
        else:
            ans.append(word2[size:])
            
        return ''.join(ans)