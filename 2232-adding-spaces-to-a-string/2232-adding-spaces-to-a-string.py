class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = []
        left = 0
        
        for idx in spaces:
            words.append(s[left:idx])
            left = idx

        words.append(s[left:])
        
        return " ".join(words)