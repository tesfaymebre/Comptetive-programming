class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        st_concat = ''
        count = 0
        
        for i in range(len(s)-1,-1,-1):
        
            if s[i].isdigit():
                count += 1
            elif count > 0:
                stack.pop()
                
                while stack[-1] != ']':
                    st_concat += stack.pop()
                
                stack.pop()
                
                stack.append(st_concat * int(s[i+1: i + 1 + count]))
                st_concat = ''
                count = 0
                
            if not s[i].isdigit():    
                stack.append(s[i])
            
        if count > 0:
            stack.pop()
                
            while stack[-1] != ']':
                print(stack)
                st_concat += stack.pop()
            
            stack.pop()
                
            stack.append(st_concat*int(s[0 : count]))
        
        return "".join(stack[::-1])
                
            