class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0]*26
        s2_count = [0]*26
        
        for c in s1:
            s1_count[ord(c)%97] += 1
       
        k = len(s1)
        l = 0
        
        for idx,c in enumerate(s2):
            s2_count[ord(c)%97] += 1
            
            if (idx - l + 1) == k:
                
                if s1_count == s2_count:
                    return True
                
                s2_count[ord(s2[l])%97] -= 1
                l += 1
                
        return False