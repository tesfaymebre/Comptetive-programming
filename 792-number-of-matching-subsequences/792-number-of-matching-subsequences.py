class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        def insert_in_trie(word: str):
            curr = trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            if None in curr:
                curr[None] += 1  
            else:
                curr[None] = 1
            
        S = len(s)
        trie = {}
        for word in words:
            insert_in_trie(word)
        ans = 0
		
        queue = [(trie, 0)]
        while queue:
            curr, i = queue.pop()
            for char in curr:
                if char == None:
                    ans += curr[None]
                else:
                    for j in range(i, S):
                        if s[j] == char:
                            queue.append((curr[char], j + 1))
                            break
        return ans