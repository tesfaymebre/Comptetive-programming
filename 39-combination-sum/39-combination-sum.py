class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backT(indx,total,path):
            if total == target:
                res.append(path)
                return
            if total > target:
                return
            
            for i in range(indx,len(candidates)):
                backT(i,total+candidates[i],path + [candidates[i]])
        
        backT(0,0,[])
        return res