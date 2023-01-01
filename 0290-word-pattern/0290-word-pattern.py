class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        pattern_word = {}
        word_pattern = {}
        
        if len(words) != len(pattern):
            return False
        
        for idx,word in enumerate(words):
            if word in word_pattern and word_pattern[word] != pattern[idx]:
                return False
            
            if pattern[idx] in pattern_word and pattern_word[pattern[idx]] != words[idx]:
                return False
            
            pattern_word[pattern[idx]] = word
            word_pattern[word] = pattern[idx]
            
        return True