class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_sub = defaultdict(int)
        
        seen = set()
        shortest = (float('inf'),'')
        
        left = 0
        for right in range(len(s)):
            count_sub[s[right]] += 1
            
            if s[right] in count_t and count_sub[s[right]] >= count_t[s[right]]:
                seen.add(s[right])
            
            while left <= right and len(seen) == len(count_t):
                shortest = min(shortest,(right-left+1,s[left:right+1]))
                count_sub[s[left]] -= 1
                
                if s[left] in count_t and count_sub[s[left]] < count_t[s[left]]:
                    seen.remove(s[left])
                    
                left += 1
                
        return shortest[1]
                
            
        
        