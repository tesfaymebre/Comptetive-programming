class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word):
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
            
        curr.is_word = True
        
    def search(self, word):
        def dfs(node, i):
            if i == len(word): return node.is_word
               
            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i+1): return True
                    
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            
            return False
    
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)