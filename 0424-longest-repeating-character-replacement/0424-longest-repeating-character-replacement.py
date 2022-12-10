class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]*26
        longest = 0
        max_count = 0
        
        left = 0
        
        for right in range(len(s)):
            count[ord(s[right])%ord('A')] += 1
            window_size = right - left + 1
            
            while left <= right and window_size - max(count) > k:
                count[ord(s[left])%ord('A')] -= 1
                left += 1
                window_size = right - left + 1
                
            longest = max(longest,window_size)
            
        return longest
                
            