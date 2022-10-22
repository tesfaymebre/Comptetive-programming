class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_freq = Counter(t)
        s_freq = defaultdict(int)
        seen = set()
        ans = ''
        ans_size = float('inf')
        
        left = 0
        for right in range(len(s)):
            if s[right] in target_freq:
                seen.add(s[right])
                s_freq[s[right]] += 1
            
            while len(seen) == len(target_freq): 
                flag = True
                for key,val in target_freq.items():
                    if s_freq[key] < val:
                        flag = False
                        break
                        
                if not flag:
                    break
                    
                if ans_size > right-left+1:
                    ans = s[left:right+1]
                    ans_size = right-left+1

                if s_freq[s[left]] == 1:
                    seen.remove(s[left])
                s_freq[s[left]] -= 1
                left += 1
                
        return ans
                    
                    
                    
                
                         
        