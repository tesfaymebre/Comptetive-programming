class Solution:
    def similarPairs(self, words: List[str]) -> int:
        freq = {}
        
        for word in words:
            chars = set(word)
            chars = "".join(sorted(list(chars)))
            freq[chars] = freq.get(chars,0) + 1
            
        ans = 0
        
        for val in freq.values():
            ans += val*(val - 1) // 2
            
        return ans
        