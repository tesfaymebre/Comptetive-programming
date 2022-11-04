class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque([(beginWord,1)])
        visited = set(beginWord)
        
        while queue:
            node,steps = queue.popleft()
            
            if node == endWord:
                return steps

            for i in range(len(node)):
                for c in range(26):
                    neighbour = node[:i] + chr(ord('a')+c) + node[i+1:]
                    
                    if neighbour not in visited and neighbour in wordList:
                        queue.append((neighbour,steps+1))
                        visited.add(neighbour)
                        
        return 0