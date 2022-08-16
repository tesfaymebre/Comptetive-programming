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
        new_word = []
        
        for letter in word:
            if letter not in curr.children:
                return word
            
            curr = curr.children[letter]
            new_word.append(letter)
            
            if curr.isWord:
                return "".join(new_word)
            
            
        
        return "".join(new_word)
        
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word)
        
        ans = []
        
        for word in sentence.split():
            ans.append(self.search(word))
        
        return " ".join(ans)
        