class Solution:
    def largestVariance(self, s: str) -> int:
        f1 =0
        f2 = 0
        ans = 0
        
        pairs = [(l1,l2) for l1 in set(s) for l2 in set(s) if l1 != l2]
        
        for _ in range(2):
            for pair in pairs:
                f1 = f2 = 0
                
                for ch in s:
                    if ch not in pair:
                        continue
                        
                    if ch == pair[0]: f1 += 1
                    elif ch == pair[1]: f2 += 1
                        
                    if f1 < f2: f1 = f2 = 0
                    elif f1 > 0 and f2 > 0:
                        ans = max(ans,f1 - f2)
                        
            s = s[::-1]
            
        return ans