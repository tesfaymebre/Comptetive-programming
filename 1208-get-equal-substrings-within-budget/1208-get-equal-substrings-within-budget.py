class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_len = 0
        
        left = 0
        for right in range(len(s)):
            diff = abs(ord(s[right]) - ord(t[right]))
            
            while left <= right and diff > maxCost:
                maxCost += abs(ord(s[left]) - ord(t[left]))
                left += 1
                
            if diff > maxCost:
                left += 1
                continue
                
            maxCost -= diff
                
            max_len = max(max_len, right - left + 1)
            
        return max_len