class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class Solution(object):
    def longestWord(self, words):
        self.root = TrieNode()    
        words = sorted(set(words), key = lambda word:(-len(word), word))
        for word in words:
            cur = self.root
            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]
            cur.end = True
        for word in words:
            flag = True
            cur = self.root
            for letter in word:
                if cur.children[letter].end == False:
                    flag = False
                    break
                else:
                    cur = cur.children[letter]
            if flag:
                return word
        return ''