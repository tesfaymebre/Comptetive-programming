class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backT(path,opening,closing):
            if len(path) == 2*n:
                result.append(''.join(path))
                return
            
            if opening < n:
                path.append('(')
                backT(path,opening+1,closing)
                path.pop()
                
            if closing < n and closing < opening:
                path.append(')')
                backT(path,opening,closing+1)
                path.pop()
                
            return
        
        backT([],0,0)
        return result
        