class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        buttons = {'2':'abc','3':'def','4':'ghi','5':'jkl',
                   '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        result = []
        
        def backT(index,path):
            if index == len(digits):
                if path:
                    result.append(''.join(path))
                return
            
            for c in buttons[digits[index]]:
                backT(index+1,path + [c])
                
        backT(0,[])
        return result
        
                
   