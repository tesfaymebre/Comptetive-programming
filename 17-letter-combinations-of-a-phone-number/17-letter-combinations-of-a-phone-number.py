class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {'2':"abc",'3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        def backT(indx,path):
            if not digits:
                return
            if indx >= len(digits):
                res.append("".join(path))
                return
            
            for c in letters[digits[indx]]:
                backT(indx+1,path + [c])
            
        res = []
        backT(0,[])
        return res