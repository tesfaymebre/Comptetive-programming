class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backTrack(left,right,path):
            if len(path)//2 == n:
                res.append("".join(path))
                return
            
            if left < n:
                backTrack(left+1,right,path + ['('])
            
            if right < left:
                backTrack(left,right+1, path + [')'])
            
        backTrack(0,0,[])
        return res