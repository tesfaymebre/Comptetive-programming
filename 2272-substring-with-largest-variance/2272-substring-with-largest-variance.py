class Solution:
    def helper(self,s):
        ans = 0 
        seen = set(s)
        
        for x in seen: 
            for y in seen: 
                
                if x != y: 
                    freq_1 = 0
                    freq_2 = 0
                    
                    for ch in s:
                        if ch == x:
                            freq_1 += 1
                        elif ch == y:
                            freq_2 += 1
                        else:
                            continue
                            
                        if freq_1 < freq_2:
                            freq_1 = 0
                            freq_2 = 0
                        elif freq_1 > 0 and freq_2 > 0:
                            ans = max(ans, freq_1 - freq_2)
        return ans 
    
    def largestVariance(self, s: str) -> int:
        return max(self.helper(s),self.helper(s[::-1]))