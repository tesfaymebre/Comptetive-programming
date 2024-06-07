class TrieNode():
    def __init__(self):
        self.children = dict()
        self.isWord = False
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        
        curr.isWord = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        
        for indx,letter in enumerate(word):
            if curr.isWord:
                return word[:indx]
            
            if letter not in curr.children:
                return word
            
            curr = curr.children[letter]
            
        return word
        
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word)
        
        ans = []
        
        for word in sentence.split():
            ans.append(self.search(word))
        
        return " ".join(ans)
        