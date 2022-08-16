class TrieNode():
    def __init__(self):
        self.children = dict()
        self.isWord = False
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        curr = self.root
        
        for l in word:
            if l not in curr.children:
                curr.children[l] = TrieNode()
            
            curr = curr.children[l]
        
        curr.isWord = True
    
    
    def search(self,s,cache={}):
        if s in cache:
            return cache[s]
        
        curr = self.root
        found = False
        for indx,l in enumerate(s):
            if curr.isWord:
                found |= self.search(s[indx:],cache)
            if l not in curr.children:
                cache[s] = found
                return found
            curr = curr.children[l]
            
        cache[s] = found or curr.isWord
        return cache[s]
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            self.insert(word)
        
        cc = {}
        return self.search(s,cc)
         