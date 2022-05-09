class TrieNode:
    
    def __init__(self):
        self.children = dict()
        self.isWord = False
        
class Solution:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        
        if word == "" and word not in curr.children:
            curr.children[word] = TrieNode()
        
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        
        curr.isWord = True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        for word in strs:
            self.insert(word)
        
        curr = self.root
        common = []
        
        while len(curr.children) == 1 and not curr.isWord:
            for key,val in curr.children.items():
                common.append(key)
            curr = curr.children[common[-1]]
        
        return "".join(common)