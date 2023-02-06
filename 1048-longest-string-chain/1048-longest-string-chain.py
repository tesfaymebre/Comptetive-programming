class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        uniqWords = set(words)
        memo = {}
        
        def dp(word):
            if word not in memo:

                if len(word) == 1: 
                    return 1

                count = 1
                
                for i in range(len(word)):
                    nextWord = word[:i] + word[i+1:]
                    
                    if nextWord in uniqWords:
                        count = max(count, 1+dp(nextWord))
                        
                memo[word] = count

            return memo[word]
            
        max_count = 1
        
        for word in words:
            max_count = max(max_count,dp(word))
            
        return max_count