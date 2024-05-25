class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        
        def back_t(idx, path):
            if idx == len(s):
                res.append(" ".join(path))
                return
            
            for i in range(idx ,len(s)):
                temp = s[idx:i+1]
                
                if temp in wordDict:
                    path.append(temp)
                    back_t(i+1,path)
                    path.pop()
                    
            return
        
        back_t(0, [])
        
        return res