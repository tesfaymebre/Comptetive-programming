class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        count = 1
        
        for i in range(len(s)):
            if s[i] in seen:
                count += 1
                seen = set()
                
            seen.add(s[i])
            
        return count