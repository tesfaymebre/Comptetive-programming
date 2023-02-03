class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for name in path.split('/'):
            if stack and name == '..':
                stack.pop()
                
            if name and name != '..' and name != '.':
                stack.append('/'+name)
               
        ans = ''.join(stack)
       
        if ans:
            return ans
        else:
            return '/'