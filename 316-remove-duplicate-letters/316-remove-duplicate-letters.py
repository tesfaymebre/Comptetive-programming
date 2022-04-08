class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_pos = dict()
        
        for i in range(len(s)):
            last_pos[s[i]] = i
        
        seen = set()
        stack = []
        
        for j in range(len(s)):
            if s[j] not in seen:
                while stack and stack[-1] > s[j] and last_pos[stack[-1]] > j:
                    seen.remove(stack.pop())
                    
                stack.append(s[j])
                seen.add(s[j])
                
        return "".join(stack)
                
        
            