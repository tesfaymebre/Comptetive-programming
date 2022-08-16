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
    @cache
    def search(self,s):
        curr = self.root
        found = False
        for indx,l in enumerate(s):
            if curr.isWord:
                found |= self.search(s[indx:])
                
            if l not in curr.children:
                return False or found

            curr = curr.children[l]
            if found: return found
        return found or curr.isWord
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            self.insert(word)
        
        return self.search(s)
        